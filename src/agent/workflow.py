"""Preparation workflow for the graph-guided EX04 agent.

This is intentionally deterministic for Phase 3 setup. A later LangGraph layer
can wrap these steps as nodes without changing the evidence contract.
"""

from __future__ import annotations

from pathlib import Path

from .state import EvidenceItem, InvestigationState
from .tools import (
    load_graph_json,
    read_text_unit,
    select_print_final_scores_suspects,
    write_agent_log,
)


def build_initial_state() -> InvestigationState:
    return {
        "bug_summary": "print_final_scores accepts final_score but reads global score.",
        "selected_files": [
            "mathsquiz/mathsquiz-step2.py",
            "mathsquiz/mathsquiz-step3.py",
        ],
        "graph_artifacts": [
            "artifacts/graphify/GRAPH_REPORT.md",
            "artifacts/graphify/graph.json",
            "artifacts/source_evidence/print_final_scores_source.md",
        ],
        "obsidian_context": [
            "obsidian/index.md",
            "obsidian/hot.md",
        ],
        "suspect_nodes": [],
        "evidence": [],
        "text_units_read": [],
        "proposed_fix": "",
        "verification_plan": "",
        "status": "prepared",
    }


def run_preparation_workflow(project_root: Path) -> InvestigationState:
    state = build_initial_state()

    for relative_path in [*state["obsidian_context"], *state["graph_artifacts"]]:
        _, metric = read_text_unit(project_root / relative_path)
        state["text_units_read"].append(metric)

    graph = load_graph_json(project_root / "artifacts/graphify/graph.json")
    state["suspect_nodes"] = select_print_final_scores_suspects(graph)

    evidence: EvidenceItem = {
        "claim": "print_final_scores is the graph-selected bug-critical function.",
        "source": "artifacts/graphify/GRAPH_REPORT.md and graph.json",
        "evidence_type": "graph",
        "confidence": "high",
        "verification_step": "Read step2 and step3 source before implementing the fix.",
    }
    state["evidence"].append(evidence)
    state["evidence"].append(
        {
            "claim": "Focused source evidence confirms final_score is ignored in step2 and step3.",
            "source": "artifacts/source_evidence/print_final_scores_source.md",
            "evidence_type": "source",
            "confidence": "high",
            "verification_step": "Use this evidence to create a Phase 4 regression test before fixing.",
        }
    )

    state["proposed_fix"] = (
        "Replace reads of global score inside print_final_scores with final_score; "
        "in step3 compute percentage from final_score / max_possible_score."
    )
    state["verification_plan"] = (
        "Use a regression test where global score differs from final_score and assert output follows "
        "final_score."
    )
    state["status"] = "phase3_prepared"
    return state


def run_graph_guided_workflow(project_root: Path) -> InvestigationState:
    state = run_preparation_workflow(project_root)
    state["status"] = "phase3_executed"
    write_agent_log(state, project_root / "artifacts/logs/graph_guided_agent_log.md")
    return state
