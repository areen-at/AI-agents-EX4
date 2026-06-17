# Bug Analysis Report

Status: Phase 0 placeholder updated with selected subsystem.

## Selected Subsystem

`mathsquiz`

## Candidate Files

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`
- `mathsquiz/mathsquiz.py`

## Next Phase 0 Task

Select the exact reproducible `mathsquiz` bug instance before starting the fix phase.

## Phase 1 Candidate Bug Paths

### Candidate A: `mathsquiz.py` baseline failure

Evidence:

- Syntax error under Python 3.
- Python 2 print syntax.
- Assignment inside conditions.
- Invalid `else if`.
- Wrong expected answers.
- Missing score increments.

### Candidate B: `print_final_scores` state-coupling bug

Evidence:

- `mathsquiz-step2.py::print_final_scores(final_score)` reads global `score`.
- `mathsquiz-step3.py::print_final_scores(final_score, max_possible_score)` reads global `score`.
- The `final_score` parameter is unused, violating modular function design.

### Candidate C: unguarded numeric input conversion

Evidence:

- `ask_question` directly calls `int(answer)`.
- Non-numeric input can crash the script.
