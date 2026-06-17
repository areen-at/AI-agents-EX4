# print_final_scores Global-State Bug

## Status

Official EX04 investigation target.

## Bug Description

`print_final_scores(...)` accepts score data through parameters but reads the module-level global variable `score`. The function therefore ignores the explicit value supplied by its caller and depends on hidden external state.

## Files and Functions

| File | Function |
|---|---|
| `mathsquiz/mathsquiz-step2.py` | `print_final_scores(final_score)` |
| `mathsquiz/mathsquiz-step3.py` | `print_final_scores(final_score, max_possible_score)` |

Related functions:

- `ask_question(...)`
- module-level score accumulation
- final module-level call to `print_final_scores(...)`

## Why This Is a Modularity Bug

- The function interface is misleading.
- Behavior depends on global state that is not visible in the signature.
- Isolated tests can fail or become order-dependent.
- Reuse by an agent or another module can produce incorrect output.
- Score calculation and score presentation are coupled through accidental shared state.

## Expected Fix

- Use `final_score` for printed score output.
- Use `final_score` for threshold checks in step2.
- Use `final_score / max_possible_score` for percentage calculation in step3.
- Keep `score` accumulation outside the reporting function.

## Phase 1 Reproduction Plan

1. Create a controlled test where global `score` is `0`.
2. Call the step2 function with `final_score=2`.
3. Capture output and prove it reports `0` before the fix.
4. Create a controlled test where global `score` is `0`.
5. Call the step3 function with `final_score=10` and `max_possible_score=10`.
6. Capture output and prove it reports `0` and `0%` before the fix.
7. Repeat after the fix and prove output follows `final_score`.

## Links

- [[index]]
- [[hot]]
- [[mathsquiz]]
- [[architecture]]
- [[bug_investigation]]
- [[tests_and_verification]]
