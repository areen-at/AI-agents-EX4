"""Optional LangGraph wrapper for the graph-guided investigation workflow.

The project keeps the deterministic workflow as the tested core so it can run in
minimal Python environments. When LangGraph is installed, this module exposes the
same investigation contract as a real LangGraph state graph.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .state import EvidenceItem, InvestigationState
from .tools import load_graph_json, read_text_unit, select_print_final_scores_suspects, write_agent_log
from .workflow import build_initial_state

try:  # pragma: no cover - exercised only when LangGraph is installed.
    from langgraph.graph import END, StateGraph
except ImportError:  # pragma: no cover - deterministic fallback is tested locally.
    END = "__end__"
    StateGraph = None


def langgraph_available() -> bool:
    """Return whether the optional LangGraph dependency is importable."""
    return StateGraph is not None


def _load_obsidian_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    for relative_path in state["obsidian_context"]:
        _, metric = read_text_unit(project_root / relative_path)
        state["text_units_read"].append(metric)
    state["status"] = "langgraph_obsidian_loaded"
    return state


def _load_graph_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    for relative_path in state["graph_artifacts"]:
        _, metric = read_text_unit(project_root / relative_path)
        state["text_units_read"].append(metric)
    state["status"] = "langgraph_graph_loaded"
    return state


def _select_suspects_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    graph = load_graph_json(project_root / "artifacts/graphify/graph.json")
    state["suspect_nodes"] = select_print_final_scores_suspects(graph)
    state["status"] = "langgraph_suspects_selected"
    return state


def _add_evidence_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    del project_root
    graph_evidence: EvidenceItem = {
        "claim": "print_final_scores is the graph-selected bug-critical function.",
        "source": "artifacts/graphify/GRAPH_REPORT.md and graph.json",
        "evidence_type": "graph",
        "confidence": "high",
        "verification_step": "Read step2 and step3 source before implementing the fix.",
    }
    source_evidence: EvidenceItem = {
        "claim": "Focused source evidence confirms final_score is ignored in step2 and step3.",
        "source": "artifacts/source_evidence/print_final_scores_source.md",
        "evidence_type": "source",
        "confidence": "high",
        "verification_step": "Use this evidence to create a Phase 4 regression test before fixing.",
    }
    state["evidence"].extend([graph_evidence, source_evidence])
    state["status"] = "langgraph_evidence_added"
    return state


def _plan_fix_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    del project_root
    state["proposed_fix"] = (
        "Replace reads of global score inside print_final_scores with final_score; "
        "in step3 compute percentage from final_score / max_possible_score."
    )
    state["verification_plan"] = (
        "Use a regression test where global score differs from final_score and assert output follows "
        "final_score."
    )
    state["status"] = "langgraph_fix_planned"
    return state


def _write_log_node(state: InvestigationState, project_root: Path) -> InvestigationState:
    state["status"] = "langgraph_executed"
    write_agent_log(state, project_root / "artifacts/logs/graph_guided_agent_log.md")
    return state


def build_langgraph_app(project_root: Path) -> Any:
    """Build and compile the LangGraph state graph.

    Raises:
        RuntimeError: if LangGraph is not installed.
    """
    if StateGraph is None:
        raise RuntimeError("LangGraph is not installed. Run `uv sync --group dev` first.")

    graph = StateGraph(InvestigationState)
    graph.add_node("load_obsidian", lambda state: _load_obsidian_node(state, project_root))
    graph.add_node("load_graph", lambda state: _load_graph_node(state, project_root))
    graph.add_node("select_suspects", lambda state: _select_suspects_node(state, project_root))
    graph.add_node("add_evidence", lambda state: _add_evidence_node(state, project_root))
    graph.add_node("plan_fix", lambda state: _plan_fix_node(state, project_root))
    graph.add_node("write_log", lambda state: _write_log_node(state, project_root))

    graph.set_entry_point("load_obsidian")
    graph.add_edge("load_obsidian", "load_graph")
    graph.add_edge("load_graph", "select_suspects")
    graph.add_edge("select_suspects", "add_evidence")
    graph.add_edge("add_evidence", "plan_fix")
    graph.add_edge("plan_fix", "write_log")
    graph.add_edge("write_log", END)
    return graph.compile()


def run_langgraph_workflow(project_root: Path) -> InvestigationState:
    """Run the LangGraph agent workflow when LangGraph is installed."""
    app = build_langgraph_app(project_root)
    return app.invoke(build_initial_state())

