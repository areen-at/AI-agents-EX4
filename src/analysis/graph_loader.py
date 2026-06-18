"""Load Graphify-style graph artifacts for Phase 6 analysis."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_graph(path: Path) -> dict[str, Any]:
    """Load a Graphify-style JSON graph from disk."""
    return json.loads(path.read_text(encoding="utf-8"))


def graph_nodes(graph: dict[str, Any]) -> list[dict[str, Any]]:
    """Return graph nodes as dictionaries."""
    return list(graph.get("nodes", []))


def graph_edges(graph: dict[str, Any]) -> list[dict[str, Any]]:
    """Return graph edges as dictionaries."""
    return list(graph.get("edges", []))

