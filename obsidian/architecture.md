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
