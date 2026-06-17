# Tests and Verification

## Before Fix

TBD after exact bug selection.

Candidate checks:

- Run `mathsquiz.py` under Python 3 and capture syntax failure.
- Unit-style call to `print_final_scores(final_score=...)` after controlling global `score`, to expose global state coupling.
- Run `ask_question` with mocked input to verify score return.

## After Fix

TBD

## Test Commands

TBD after exact bug selection.
