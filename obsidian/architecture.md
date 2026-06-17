# Architecture Notes

## Overview

Phase 1 static graph analysis shows `mathsquiz` as an evolving procedural-to-functional quiz program.

The subsystem has four relevant files:

- `mathsquiz.py`: broken baseline.
- `mathsquiz-step1.py`: fixed linear script.
- `mathsquiz-step2.py`: functional refactor.
- `mathsquiz-step3.py`: randomized functional quiz.

## Main Blocks

- Welcome/output layer: `welcome_message`, `print`.
- Question loop / script flow: repeated blocks in step1, module-level calls in step2/step3.
- Question execution: `ask_question`.
- Input parsing: `input` and `int`.
- Score state: global `score`, `points_awarded`, and score accumulation.
- Final feedback: `print_final_scores`.

## Bug-Critical Path

Official bug-critical path:

```text
module flow -> ask_question -> score accumulation -> print_final_scores(final_score, ...) -> global score read
```

Risk:

`print_final_scores(final_score, ...)` reads global `score` instead of the parameter, creating hidden state coupling.

## Modularity Violation

The function boundary says final-score reporting is controlled by parameters. The implementation contradicts that interface by reading module-level `score`. This mixes presentation, scoring state, and module execution state inside one function, making the function harder to test, reuse, and reason about.

## Expected Architectural Fix

Keep score ownership in the module-level quiz flow and pass the final value into `print_final_scores(...)`. The final-score function should become a pure reporting component over explicit inputs.

## Diagram Links

- `../artifacts/diagrams/architecture_block_diagram.md`
- `../artifacts/diagrams/oop_diagram.md`
- `../artifacts/diagrams/score_state_flow_diagram.md`

## Phase 2 Findings

- The architecture is script-first and procedural.
- `mathsquiz-step2.py` and `mathsquiz-step3.py` introduce functions, but module-level code still controls execution and state.
- No classes exist, so the required OOP view is represented as a module/function interaction diagram.
- `ask_question(...)` combines input, parsing, correctness checking, printing, and point calculation.
- `print_final_scores(...)` should be a reporting boundary, but it reaches into global `score`, which makes it the selected modularity failure.

## Phase 2 Diagram Interpretation

The architecture diagram shows the evolution from baseline to functional versions. The module/function diagram shows why the code looks modular at first but still contains hidden state coupling.

The score-state flow diagram was added during Phase 2 review because the first two diagrams did not isolate the exact state-flow defect. It shows the intended explicit parameter path and the actual hidden global-state path.
