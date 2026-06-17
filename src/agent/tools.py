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
