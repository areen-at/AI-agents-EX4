# Reverse Engineering Report

Status: Phase 1 initial graph-based reverse-engineering report.

## Scope

Selected repository: `martinpeck/broken-python`

Selected subsystem: `mathsquiz`

Analyzed files:

- `mathsquiz/mathsquiz.py`
- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

## Graph Generation

Graphify executable was not available locally. Phase 1 therefore generated Graphify-style artifacts using a local AST/static-analysis workflow.

Generation log:

- `artifacts/logs/graphify_run.md`

Artifacts:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `artifacts/graphify/graph_metrics.json`
- `artifacts/graphify/graph.html`

## Graph Totals

- Nodes: 47
- Edges: 153
- Files: 4
- Functions: 6
- Bug risks: 14
- Syntax errors: 1

## Initial Architecture Understanding

`mathsquiz` evolves from a broken linear script into a more modular quiz implementation:

1. `mathsquiz.py`: baseline with syntax and logic defects.
2. `mathsquiz-step1.py`: repaired linear version with repeated question blocks.
3. `mathsquiz-step2.py`: functional refactor with `welcome_message`, `ask_question`, and `print_final_scores`.
4. `mathsquiz-step3.py`: randomized question generation and percentage-based feedback.

## Initial Bug-Risk Findings

- Official target: hidden state coupling in `print_final_scores` in `mathsquiz-step2.py` and `mathsquiz-step3.py`.
- Background candidate: baseline syntax and logic defects in `mathsquiz.py`.
- Background candidate: possible input-conversion crash path through unguarded `int(answer)`.

## Official Bug-Critical Path

```text
module-level quiz flow
-> ask_question(...)
-> score accumulation
-> print_final_scores(final_score, ...)
-> hidden read of global score
-> incorrect or non-isolated final-score output
```

## Next Reverse-Engineering Tasks

- Verify the `print_final_scores` global-state bug with a focused function-level reproduction.
- Build architecture and module interaction diagrams in Phase 2.
