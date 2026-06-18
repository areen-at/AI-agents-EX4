"""Command-line runner for the Phase 3 graph-guided agent workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .langgraph_workflow import langgraph_available, run_langgraph_workflow
from .workflow import run_graph_guided_workflow


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the EX04 graph-guided agent workflow.")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Path to the EX04 submission project root.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the final workflow state as JSON.",
    )
    parser.add_argument(
        "--engine",
        choices=["auto", "deterministic", "langgraph"],
        default="auto",
        help="Workflow engine to use. auto uses LangGraph if installed, otherwise deterministic.",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root)
    engine_used = args.engine
    if args.engine == "langgraph":
        state = run_langgraph_workflow(project_root)
    elif args.engine == "auto" and langgraph_available():
        state = run_langgraph_workflow(project_root)
        engine_used = "langgraph"
    else:
        state = run_graph_guided_workflow(project_root)
        engine_used = "deterministic"

    if args.json:
        payload = dict(state)
        payload["engine_used"] = engine_used
        print(json.dumps(payload, indent=2))
    else:
        print(f"Phase 3 graph-guided workflow executed with {engine_used} engine.")
        print("Log: artifacts/logs/graph_guided_agent_log.md")
        print(f"Suspects selected: {len(state['suspect_nodes'])}")


if __name__ == "__main__":
    main()
