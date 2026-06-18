"""Rank suspicious graph nodes for the selected mathsquiz bug."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .graph_loader import graph_edges, graph_nodes, load_graph


DEFAULT_BUG_KEYWORDS = (
    "print_final_scores",
    "final_score",
    "score",
    "global",
    "unused",
    "parameter",
    "percentage",
)

RISK_TYPES = {"bug_risk", "syntax_error"}
SIGNAL_TYPES = {"function", "state_variable", "file"}
NOISY_CALLS = {"print", "input", "int", "range", "randint"}


@dataclass(frozen=True)
class RankedNode:
    rank: int
    node_id: str
    label: str
    node_type: str
    source_file: str
    degree: int
    in_degree: int
    out_degree: int
    keyword_score: int
    proximity_score: int
    risk_score: int
    total_score: int
    reasons: tuple[str, ...]


def _node_text(node: dict[str, Any]) -> str:
    values = [
        str(node.get("id", "")),
        str(node.get("label", "")),
        str(node.get("type", "")),
        str(node.get("source_file", "")),
    ]
    return " ".join(values).lower()


def _keyword_score(node: dict[str, Any], keywords: tuple[str, ...]) -> int:
    text = _node_text(node)
    return sum(1 for keyword in keywords if keyword.lower() in text)


def _edge_neighbors(edges: list[dict[str, Any]], node_id: str) -> set[str]:
    neighbors: set[str] = set()
    for edge in edges:
        source = str(edge.get("source", ""))
        target = str(edge.get("target", ""))
        if source == node_id:
            neighbors.add(target)
        if target == node_id:
            neighbors.add(source)
    return neighbors


def _proximity_score(
    node: dict[str, Any],
    edges: list[dict[str, Any]],
    risky_node_ids: set[str],
    selected_files: tuple[str, ...],
) -> int:
    node_id = str(node.get("id", ""))
    source_file = str(node.get("source_file", ""))
    score = 0

    if source_file in selected_files:
        score += 4
    if node_id in risky_node_ids:
        score += 5

    neighbors = _edge_neighbors(edges, node_id)
    if neighbors & risky_node_ids:
        score += 3
    if any(any(path in neighbor for path in selected_files) for neighbor in neighbors):
        score += 2
    return score


def _risk_score(node: dict[str, Any]) -> int:
    node_type = str(node.get("type", ""))
    node_id = str(node.get("id", "")).lower()
    label = str(node.get("label", "")).lower()
    score = 0
    if node_type in RISK_TYPES or node_id.startswith("risk:"):
        score += 8
    if "global_score_instead_of_param" in node_id:
        score += 6
    if "unused_arg" in node_id or "unused parameter" in label:
        score += 4
    if "syntax" in node_type or "syntax" in node_id:
        score += 2
    return score


def _degree_score(node: dict[str, Any]) -> int:
    degree = int(node.get("degree", 0))
    node_type = str(node.get("type", ""))
    label = str(node.get("label", ""))

    if node_type == "callable_reference" and label in NOISY_CALLS:
        return 0
    return min(degree, 12)


def _reasons(
    node: dict[str, Any],
    keyword_score: int,
    proximity_score: int,
    risk_score: int,
) -> tuple[str, ...]:
    reasons: list[str] = []
    node_type = str(node.get("type", ""))
    if risk_score:
        reasons.append("explicit graph risk signal")
    if keyword_score:
        reasons.append("matches selected bug keywords")
    if proximity_score:
        reasons.append("near selected files or risk nodes")
    if node_type in SIGNAL_TYPES:
        reasons.append(f"architectural {node_type} node")
    if not reasons:
        reasons.append("ranked by structural degree only")
    return tuple(reasons)


def rank_suspicious_nodes(
    graph: dict[str, Any],
    *,
    bug_keywords: tuple[str, ...] = DEFAULT_BUG_KEYWORDS,
    selected_files: tuple[str, ...] = (
        "mathsquiz/mathsquiz-step2.py",
        "mathsquiz/mathsquiz-step3.py",
    ),
) -> list[RankedNode]:
    """Rank graph nodes by bug relevance, structural centrality, and risk signals."""
    nodes = graph_nodes(graph)
    edges = graph_edges(graph)
    risky_node_ids = {
        str(node.get("id", ""))
        for node in nodes
        if _risk_score(node) or _keyword_score(node, bug_keywords) >= 2
    }

    ranked: list[RankedNode] = []
    for node in nodes:
        keyword_score = _keyword_score(node, bug_keywords)
        proximity_score = _proximity_score(node, edges, risky_node_ids, selected_files)
        risk_score = _risk_score(node)
        degree_score = _degree_score(node)
        node_type = str(node.get("type", ""))
        type_bonus = 2 if node_type in SIGNAL_TYPES else 0
        total_score = (keyword_score * 5) + proximity_score + risk_score + degree_score + type_bonus

        if total_score <= 0:
            continue

        ranked.append(
            RankedNode(
                rank=0,
                node_id=str(node.get("id", "")),
                label=str(node.get("label", "")),
                node_type=node_type,
                source_file=str(node.get("source_file", "")),
                degree=int(node.get("degree", 0)),
                in_degree=int(node.get("in_degree", 0)),
                out_degree=int(node.get("out_degree", 0)),
                keyword_score=keyword_score,
                proximity_score=proximity_score,
                risk_score=risk_score,
                total_score=total_score,
                reasons=_reasons(node, keyword_score, proximity_score, risk_score),
            )
        )

    ranked.sort(
        key=lambda item: (
            -item.total_score,
            -item.risk_score,
            -item.keyword_score,
            -item.degree,
            item.node_id,
        )
    )
    return [
        RankedNode(
            rank=index,
            node_id=item.node_id,
            label=item.label,
            node_type=item.node_type,
            source_file=item.source_file,
            degree=item.degree,
            in_degree=item.in_degree,
            out_degree=item.out_degree,
            keyword_score=item.keyword_score,
            proximity_score=item.proximity_score,
            risk_score=item.risk_score,
            total_score=item.total_score,
            reasons=item.reasons,
        )
        for index, item in enumerate(ranked, start=1)
    ]


def format_suspicious_nodes_report(ranked_nodes: list[RankedNode], limit: int = 10) -> str:
    """Format a Markdown report for the top suspicious graph nodes."""
    rows = "\n".join(
        (
            f"| {node.rank} | `{node.node_id}` | {node.node_type} | "
            f"`{node.source_file or 'n/a'}` | {node.total_score} | "
            f"{node.keyword_score} | {node.risk_score} | {node.proximity_score} | "
            f"{'; '.join(node.reasons)} |"
        )
        for node in ranked_nodes[:limit]
    )
    top_files = sorted({node.source_file for node in ranked_nodes[:limit] if node.source_file})
    top_file_lines = "\n".join(f"- `{path}`" for path in top_files)

    return f"""# Suspicious Node Ranking

Status: Phase 6 original extension output.

## Purpose

This report ranks Graphify-style nodes by how useful they are for investigating the selected `print_final_scores` global-state bug.

## Scoring Method

Each node receives a combined score from:

- Structural degree, capped to avoid over-rewarding generic utility calls.
- Keyword matches for `print_final_scores`, `final_score`, `score`, `global`, `unused`, `parameter`, and `percentage`.
- Explicit graph risk signals such as `global_score_instead_of_param` and `unused_arg`.
- Proximity to selected files and risk nodes.
- Small type bonuses for file, function, and state-variable nodes.

Generic calls such as `print`, `input`, `int`, `range`, and `randint` are dampened because they are central but not bug-specific.

## Top 10 Suspicious Nodes

| Rank | Node | Type | Source File | Total | Keywords | Risk | Proximity | Reasons |
|---:|---|---|---|---:|---:|---:|---:|---|
{rows}

## Top Source Files

{top_file_lines}

## How This Improves Context Selection

The ranking turns the large graph artifact into a small, ordered suspect list. Instead of asking an LLM to read every source file or the entire `graph.json`, an agent can begin with the highest-ranked function and risk nodes, then load only the associated source evidence.

## Limitations

- The ranking is heuristic, not a formal proof.
- It depends on graph quality and risk-node naming.
- The selected repository is small, so the benefit is clearer as a method demonstration than as a large absolute token saving.
- Runtime behavior still requires tests or reproduction probes.
"""


def write_suspicious_nodes_report(
    graph_path: Path,
    output_path: Path,
    *,
    limit: int = 10,
) -> list[RankedNode]:
    graph = load_graph(graph_path)
    ranked_nodes = rank_suspicious_nodes(graph)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        format_suspicious_nodes_report(ranked_nodes, limit=limit),
        encoding="utf-8",
    )
    return ranked_nodes


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank suspicious Graphify nodes.")
    parser.add_argument("--graph", default="artifacts/graphify/graph.json")
    parser.add_argument("--output", default="reports/suspicious_nodes.md")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    ranked_nodes = write_suspicious_nodes_report(
        Path(args.graph),
        Path(args.output),
        limit=args.limit,
    )
    print(f"Wrote {args.output}")
    print(f"Ranked nodes: {len(ranked_nodes)}")
    print(f"Top node: {ranked_nodes[0].node_id if ranked_nodes else 'none'}")


if __name__ == "__main__":
    main()

