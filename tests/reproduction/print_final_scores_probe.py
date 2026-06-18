"""Phase 1 probe for the selected print_final_scores global-state bug.

This script does not fix the target project. It isolates the relevant behavior
from mathsquiz-step2.py and mathsquiz-step3.py so Phase 1 can document the bug
without importing the interactive quiz scripts.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO

score = 0


def step2_print_final_scores(final_score: int) -> None:
    print("That's all the questions done. So...what was your score...?")
    print("You scored", score, "points out of a possible 10.")
    if score < 5:
        print("You need to practice your maths!")
    elif score < 8:
        print("That's pretty good!")
    elif score < 10:
        print("You did really well! Try and get 10 out of 10 next time!")
    elif score == 10:
        print("Wow! What a maths star you are!! I'm impressed!")


def step3_print_final_scores(final_score: int, max_possible_score: int) -> None:
    print("That's all the questions done. So...what was your score...?")
    print("You scored", score, "points out of a possible", max_possible_score)

    percentage = (score / max_possible_score) * 100

    if percentage < 50:
        print("You need to practice your maths!")
    elif percentage < 80:
        print("That's pretty good!")
    elif percentage < 100:
        print("You did really well! Try and get 100% next time!")
    elif percentage == 100:
        print("Wow! What a maths star you are!! I'm impressed!")


def capture_output(callable_obj, *args: int) -> str:
    buffer = StringIO()
    with redirect_stdout(buffer):
        callable_obj(*args)
    return buffer.getvalue()


def main() -> None:
    global score

    score = 0
    step2_output = capture_output(step2_print_final_scores, 2)

    score = 0
    step3_output = capture_output(step3_print_final_scores, 10, 10)

    print("PHASE 1 BUG PROBE: print_final_scores global-state coupling")
    print()
    print("Step2 probe")
    print("Expected if modular: output uses final_score=2")
    print("Actual before fix:")
    print(step2_output.strip())
    print()
    print("Step3 probe")
    print("Expected if modular: output uses final_score=10 and percentage=100")
    print("Actual before fix:")
    print(step3_output.strip())


if __name__ == "__main__":
    main()
