"""Importable mathsquiz target subsystem."""

from .mathsquiz_step2 import print_final_scores as print_step2_final_scores
from .mathsquiz_step3 import print_final_scores as print_step3_final_scores

__all__ = ["print_step2_final_scores", "print_step3_final_scores"]
