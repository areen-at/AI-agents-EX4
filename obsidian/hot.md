# Hot Context

## Bug Focus

Selected subsystem: `mathsquiz`

Candidate files:

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`
- `mathsquiz/mathsquiz.py`

The exact bug instance will be selected after a short reproduction pass. The investigation will focus on quiz behavior: question generation, input parsing, answer checking, score tracking, loop control, and user-facing behavior.

## Expected Behavior

TBD

## Actual Behavior

TBD

## Reproduction Command

TBD

## Current Suspects

Initial suspects before Graphify:

- Quiz loop control.
- User input validation.
- Answer comparison.
- Score state update.
- Differences between step scripts and final `mathsquiz.py`.

## Graph Evidence

- `artifacts/graphify/GRAPH_REPORT.md` was generated in Phase 1.
- `artifacts/graphify/graph.json` contains 47 nodes and 153 edges for `mathsquiz`.
- `mathsquiz/mathsquiz.py` has a syntax-error node and multiple extracted bug-risk nodes.
- `mathsquiz-step2.py::print_final_scores` has an extracted risk: reads global `score` instead of the `final_score` parameter.
- `mathsquiz-step3.py::print_final_scores` has the same extracted risk.
- `call:print`, `call:input`, `call:int`, and `call:ask_question` are central callable-reference nodes.

## Source Evidence

Initial source evidence from Phase 1 static analysis:

- `mathsquiz.py` cannot parse under Python 3 because of Python 2 print syntax and invalid conditional syntax.
- `mathsquiz-step1.py` is a repaired linear implementation and documents several baseline bug categories in comments.
- `mathsquiz-step2.py` introduces functions: `welcome_message`, `ask_question`, and `print_final_scores`.
- `mathsquiz-step3.py` adds random question generation and `max_possible_score`.
- In both step2 and step3, `print_final_scores` accepts score-related parameters but reads global `score`, creating hidden coupling.

## Root-Cause Hypotheses

- H1: The final fix could target the baseline `mathsquiz.py` because it has syntax errors and repeated logic defects.
- H2: The final fix could target the subtler architecture bug in `print_final_scores`, because it demonstrates why modular boundaries matter.
- H3: The quiz flow has repeated input-conversion risk because `int(answer)` is not protected against non-numeric input.

## Final Root Cause

TBD

## Fix Summary

TBD

## Verification

TBD after choosing exact bug instance.

## Links

- [[index]]
- [[bug_investigation]]
- [[tests_and_verification]]
