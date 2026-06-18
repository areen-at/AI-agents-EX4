"""Regression tests for the Phase 4 print_final_scores fix."""

from __future__ import annotations

import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.target_project.mathsquiz import mathsquiz_step2, mathsquiz_step3


def capture_output(callable_obj, *args: int) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        callable_obj(*args)
    return buffer.getvalue()


class PrintFinalScoresFixTests(unittest.TestCase):
    def test_step2_uses_final_score_not_global_score(self) -> None:
        mathsquiz_step2.score = 0

        output = capture_output(mathsquiz_step2.print_final_scores, 2)

        self.assertIn("You scored 2 points out of a possible 10.", output)
        self.assertNotIn("You scored 0 points out of a possible 10.", output)

    def test_step2_feedback_uses_final_score_thresholds(self) -> None:
        mathsquiz_step2.score = 0

        output = capture_output(mathsquiz_step2.print_final_scores, 8)

        self.assertIn("You did really well!", output)
        self.assertNotIn("You need to practice your maths!", output)

    def test_step3_uses_final_score_not_global_score(self) -> None:
        mathsquiz_step3.score = 0

        output = capture_output(mathsquiz_step3.print_final_scores, 10, 10)

        self.assertIn("You scored 10 points out of a possible 10", output)
        self.assertIn("Wow! What a maths star you are!! I'm impressed!", output)
        self.assertNotIn("You scored 0 points out of a possible 10", output)


if __name__ == "__main__":
    unittest.main()
