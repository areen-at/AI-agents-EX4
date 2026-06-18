"""Tests for the Phase 3 graph-guided agent workflow."""

from __future__ import annotations

import unittest
from pathlib import Path

from src.agent.langgraph_workflow import build_langgraph_app, langgraph_available
from src.agent.tools import select_print_final_scores_suspects
from src.agent.workflow import build_initial_state, run_preparation_workflow


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class AgentWorkflowTests(unittest.TestCase):
    def test_initial_state_locks_selected_bug(self) -> None:
        state = build_initial_state()

        self.assertIn("print_final_scores", state["bug_summary"])
        self.assertEqual(
            state["selected_files"],
            ["mathsquiz/mathsquiz-step2.py", "mathsquiz/mathsquiz-step3.py"],
        )
        self.assertEqual(state["status"], "prepared")

    def test_select_print_final_scores_suspects_ranks_graph_nodes(self) -> None:
        graph = {
            "nodes": [
                {
                    "id": "function:mathsquiz/mathsquiz-step2.py:print_final_scores",
                    "label": "print_final_scores",
                    "source_file": "mathsquiz/mathsquiz-step2.py",
                },
                {
                    "id": "risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param",
                    "label": "reads global score instead of final_score",
                    "source_file": "mathsquiz/mathsquiz-step3.py",
                },
                {
                    "id": "function:mathsquiz/mathsquiz-step3.py:ask_question",
                    "label": "ask_question",
                    "source_file": "mathsquiz/mathsquiz-step3.py",
                },
            ]
        }

        suspects = select_print_final_scores_suspects(graph)

        self.assertEqual(len(suspects), 2)
        self.assertEqual([item["rank"] for item in suspects], [1, 2])
        self.assertTrue(all("print_final_scores" in item["node_id"] for item in suspects))

    def test_preparation_workflow_reads_graph_and_obsidian_first(self) -> None:
        state = run_preparation_workflow(PROJECT_ROOT)
        paths = [Path(item["path"]).as_posix() for item in state["text_units_read"]]

        expected_suffixes = [
            "obsidian/index.md",
            "obsidian/hot.md",
            "artifacts/graphify/GRAPH_REPORT.md",
            "artifacts/graphify/graph.json",
            "artifacts/source_evidence/print_final_scores_source.md",
        ]
        self.assertEqual(len(paths), len(expected_suffixes))
        for actual, expected_suffix in zip(paths, expected_suffixes, strict=True):
            self.assertTrue(actual.endswith(expected_suffix), actual)
        self.assertGreaterEqual(len(state["suspect_nodes"]), 4)
        self.assertEqual(len(state["evidence"]), 2)
        self.assertEqual(state["status"], "phase3_prepared")
        self.assertIn("final_score", state["proposed_fix"])

    def test_langgraph_wrapper_is_available_when_dependency_is_installed(self) -> None:
        if not langgraph_available():
            with self.assertRaises(RuntimeError):
                build_langgraph_app(PROJECT_ROOT)
            return

        app = build_langgraph_app(PROJECT_ROOT)
        state = app.invoke(build_initial_state())
        self.assertEqual(state["status"], "langgraph_executed")
        self.assertGreaterEqual(len(state["suspect_nodes"]), 4)


if __name__ == "__main__":
    unittest.main()
