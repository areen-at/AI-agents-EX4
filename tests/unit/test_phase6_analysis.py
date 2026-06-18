"""Tests for the Phase 6 graph-analysis extension."""

from __future__ import annotations

import unittest
from pathlib import Path

from src.analysis.hot_md_generator import generate_hot_context
from src.analysis.suspicious_nodes import rank_suspicious_nodes


PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Phase6AnalysisTests(unittest.TestCase):
    def test_ranking_prioritizes_selected_bug_risk_nodes(self) -> None:
        graph = {
            "nodes": [
                {
                    "id": "call:print",
                    "label": "print",
                    "type": "callable_reference",
                    "degree": 99,
                    "in_degree": 99,
                    "out_degree": 0,
                },
                {
                    "id": "risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param",
                    "label": "reads global score instead of final_score",
                    "type": "bug_risk",
                    "source_file": "mathsquiz/mathsquiz-step3.py",
                    "degree": 1,
                    "in_degree": 1,
                    "out_degree": 0,
                },
                {
                    "id": "function:mathsquiz/mathsquiz-step3.py:ask_question",
                    "label": "ask_question",
                    "type": "function",
                    "source_file": "mathsquiz/mathsquiz-step3.py",
                    "degree": 8,
                    "in_degree": 4,
                    "out_degree": 4,
                },
            ],
            "edges": [
                {
                    "source": "function:mathsquiz/mathsquiz-step3.py:ask_question",
                    "target": "risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param",
                    "relation": "near",
                }
            ],
        }

        ranked = rank_suspicious_nodes(graph)

        self.assertGreaterEqual(len(ranked), 2)
        self.assertIn("global_score_instead_of_param", ranked[0].node_id)
        self.assertGreater(ranked[0].total_score, ranked[-1].total_score)

    def test_generated_hot_context_contains_ranked_bug_guidance(self) -> None:
        graph = {
            "nodes": [
                {
                    "id": "function:mathsquiz/mathsquiz-step2.py:print_final_scores",
                    "label": "print_final_scores",
                    "type": "function",
                    "source_file": "mathsquiz/mathsquiz-step2.py",
                    "degree": 9,
                    "in_degree": 3,
                    "out_degree": 6,
                }
            ],
            "edges": [],
        }
        ranked = rank_suspicious_nodes(graph)

        hot_context = generate_hot_context(ranked)

        self.assertIn("Generated Hot Context", hot_context)
        self.assertIn("print_final_scores", hot_context)
        self.assertIn("mathsquiz/mathsquiz-step2.py", hot_context)
        self.assertIn("Fix-Diff Integration", hot_context)
        self.assertIn("intentionally limited", hot_context)


if __name__ == "__main__":
    unittest.main()
