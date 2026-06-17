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

Current candidate path:

```text
module flow -> ask_question -> score accumulation -> print_final_scores
```

Risk:

`print_final_scores(final_score, ...)` reads global `score` instead of the parameter, creating hidden state coupling.

## Diagram Links

- `../artifacts/diagrams/architecture_block_diagram.md`
- `../artifacts/diagrams/oop_diagram.md`
