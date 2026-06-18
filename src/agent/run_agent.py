"""Command-line runner for the Phase 3 graph-guided agent workflow."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

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
    args = parser.parse_args()

    state = run_graph_guided_workflow(Path(args.project_root))

    if args.json:
        print(json.dumps(state, indent=2))
    else:
        print("Phase 3 graph-guided workflow executed.")
        print("Log: artifacts/logs/graph_guided_agent_log.md")
        print(f"Suspects selected: {len(state['suspect_nodes'])}")


if __name__ == "__main__":
    main()
