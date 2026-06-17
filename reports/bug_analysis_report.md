# Bug Analysis Report

Status: Phase 1 preparation updated with official bug path.

## Selected Subsystem

`mathsquiz`

## Official Bug Target

- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

Bug title: `print_final_scores` global-state coupling.

## Bug Description

`print_final_scores(...)` receives score data through its parameters, but the function body reads the module-level global variable `score`. This means the displayed score and feedback are controlled by hidden external state instead of by the function arguments.

In `mathsquiz-step2.py`, `print_final_scores(final_score)` should use `final_score`, but it prints and branches on `score`.

In `mathsquiz-step3.py`, `print_final_scores(final_score, max_possible_score)` should use `final_score`, but it prints `score` and calculates the percentage from `score`.

## Why This Violates Modular Design

- The function signature advertises explicit input, but the implementation depends on hidden module state.
- A caller cannot reason about the function from its parameters alone.
- The function is hard to test in isolation because test results depend on the global `score` variable.
- Reusing the function in another script or agent-generated module can silently produce incorrect output.
- The bug breaks the assignment's modular architecture goal: component behavior should be controlled through clear interfaces, not accidental globals.

## Expected Fix

- Replace reads of global `score` inside `print_final_scores(...)` with the provided `final_score` parameter.
- In `mathsquiz-step3.py`, calculate `percentage` from `final_score / max_possible_score`.
- Preserve the existing public behavior when the function is called from the current script.
- Add a focused regression test or reproduction script that proves `final_score` controls the output even when global `score` has a different value.

## Files and Functions Involved

| File | Function | Role |
|---|---|---|
| `mathsquiz/mathsquiz-step2.py` | `print_final_scores(final_score)` | Prints score and basic feedback |
| `mathsquiz/mathsquiz-step3.py` | `print_final_scores(final_score, max_possible_score)` | Prints score and percentage-based feedback |
| `mathsquiz/mathsquiz-step2.py` | `ask_question(...)` | Produces score increments used by module flow |
| `mathsquiz/mathsquiz-step3.py` | `ask_question(...)` | Produces score increments used by module flow |
| `mathsquiz/mathsquiz-step2.py`, `mathsquiz/mathsquiz-step3.py` | module-level flow | Accumulates global `score` and calls `print_final_scores(...)` |

## Phase 1 Evidence

Evidence:

- `mathsquiz-step2.py::print_final_scores(final_score)` reads global `score`.
- `mathsquiz-step3.py::print_final_scores(final_score, max_possible_score)` reads global `score`.
- The `final_score` parameter is unused, violating modular function design.

## Rejected or Background Candidates

- `mathsquiz.py` baseline syntax/logic failure: valid bug cluster, but less useful for modular design analysis.
- `ask_question(...)` unguarded numeric conversion: valid robustness concern, but less central to architecture than hidden score-state coupling.

## Exact Next Steps for Phase 1

1. Update `obsidian/hot.md` so the focused context names `print_final_scores` as the active bug.
2. Record the graph evidence linking the bug-risk nodes to `mathsquiz-step2.py` and `mathsquiz-step3.py`.
3. Inspect the source lines for both `print_final_scores(...)` implementations.
4. Define a direct reproduction where `final_score` and global `score` intentionally differ.
5. Add the reproduction plan to `obsidian/tests_and_verification.md`.
6. Carry this focused context into Phase 2 architecture diagrams and Phase 3 agent workflow prompts.
