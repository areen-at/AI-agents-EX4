"""Small deterministic tools for the Phase 3 graph-guided workflow."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .state import SuspectNode, TextUnitMetric


def read_text_unit(path: Path) -> tuple[str, TextUnitMetric]:
    text = path.read_text(encoding="utf-8")
    metric: TextUnitMetric = {
        "path": str(path),
        "characters": len(text),
        "estimated_tokens": max(1, len(text) // 4),
    }
    return text, metric


def load_graph_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def select_print_final_scores_suspects(graph: dict[str, Any]) -> list[SuspectNode]:
    suspects: list[SuspectNode] = []
    for node in graph.get("nodes", []):
        node_id = str(node.get("id", ""))
        label = str(node.get("label", ""))
        source_file = str(node.get("source_file", ""))
        if "print_final_scores" in node_id or label == "print_final_scores":
            suspects.append(
                {
                    "node_id": node_id,
                    "label": label,
                    "source_file": source_file,
                    "reason": "Selected bug target: final score reporting reads global score.",
                    "rank": 0,
                }
            )

    ranked_suspects = sorted(suspects, key=lambda item: item["node_id"])
    for index, suspect in enumerate(ranked_suspects, start=1):
        suspect["rank"] = index
    return ranked_suspects


def format_agent_log(state: dict[str, Any]) -> str:
    text_units = state.get("text_units_read", [])
    total_tokens = sum(int(item.get("estimated_tokens", 0)) for item in text_units)
    suspect_rows = "\n".join(
        (
            f"| {item['rank']} | `{item['node_id']}` | "
            f"`{item.get('source_file') or 'n/a'}` | {item['reason']} |"
        )
        for item in state.get("suspect_nodes", [])
    )
    text_unit_rows = "\n".join(
        f"| `{item['path']}` | {item['characters']} | {item['estimated_tokens']} |"
        for item in text_units
    )
    evidence_rows = "\n".join(
        (
            f"| {item['claim']} | `{item['source']}` | {item['evidence_type']} | "
            f"{item['confidence']} | {item['verification_step']} |"
        )
        for item in state.get("evidence", [])
    )

    return f"""# Graph-Guided Agent Log

Status: Phase 3 executed.

## Bug Target

{state['bug_summary']}

## Context Order Used

The workflow read Obsidian context first, then graph artifacts, then selected graph suspects.

## Text Units Read

| Text Unit | Characters | Estimated Tokens |
|---|---:|---:|
{text_unit_rows}

Total estimated input tokens: {total_tokens}

## Ranked Suspect Nodes

| Rank | Node | Source File | Reason |
|---:|---|---|---|
{suspect_rows}

## Evidence

| Claim | Source | Type | Confidence | Verification Step |
|---|---|---|---|---|
{evidence_rows}

## Proposed Fix

{state['proposed_fix']}

## Verification Plan

{state['verification_plan']}

## Run Status

{state['status']}
"""


def write_agent_log(state: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(format_agent_log(state), encoding="utf-8")
