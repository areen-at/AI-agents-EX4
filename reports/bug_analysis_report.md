# Bug Analysis Report

Status: Phase 4 complete.

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

## Phase 4 Root Cause

Root cause:

`print_final_scores(...)` exposes a parameterized interface but ignores the score parameter internally. The function therefore depends on ambient module state, which breaks isolated use and testing.

Bug-critical source evidence:

- `mathsquiz-step2.py`: `print_final_scores(final_score)` printed and branched on global `score`.
- `mathsquiz-step3.py`: `print_final_scores(final_score, max_possible_score)` printed global `score` and calculated percentage from global `score`.

## Phase 4 Fix

Fixed importable target modules:

- `src/target_project/mathsquiz/mathsquiz_step2.py`
- `src/target_project/mathsquiz/mathsquiz_step3.py`

Fix summary:

- Step2 now prints `final_score` and branches on `final_score`.
- Step3 now prints `final_score` and calculates percentage from `final_score / max_possible_score`.
- The fix does not change `ask_question(...)` or the unrelated broken baseline file.

Regression test:

- `tests/unit/test_print_final_scores_fix.py`

Verification:

- `python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow`
- Result: 6 tests passed.

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
- `tests/reproduction/print_final_scores_probe.py` demonstrates the failure without modifying the target code.
- `artifacts/logs/phase1_print_final_scores_probe.md` records the before-fix output: both step2 and step3 report global `score=0` while non-zero `final_score` values are passed.

## Rejected or Background Candidates

- `mathsquiz.py` baseline syntax/logic failure: valid bug cluster, but less useful for modular design analysis.
- `ask_question(...)` unguarded numeric conversion: valid robustness concern, but less central to architecture than hidden score-state coupling.

## Phase 4 Completion Evidence

- Before evidence: `artifacts/before_after/before.md`
- After evidence: `artifacts/before_after/after.md`
- Fix summary diff: `artifacts/before_after/fix.diff`
- Verification report: `reports/fix_verification_report.md`
- Phase 4 review: `reports/phase4_review.md`
