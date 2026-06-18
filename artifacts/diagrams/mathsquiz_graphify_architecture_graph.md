# Mathsquiz Architecture Graph

Status: generated during final Graphify local-run polish.

Source input:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`

Generation method:

- The course Graphify executable was not available locally.
- PyPI lookup for `graphify` returned no matching package.
- The graph below is generated from the existing Graphify-style graph artifacts produced earlier by Python AST/static analysis.

## Architecture Graph

```mermaid
flowchart TD
    User["User / Quiz Taker"]
    Step2["mathsquiz-step2.py<br/>Procedural quiz with helper functions"]
    Step3["mathsquiz-step3.py<br/>Randomized quiz with helper functions"]
    Ask2["ask_question(question, correct_answer)"]
    Ask3["ask_question(question, correct_answer)"]
    Score["module-level score state"]
    Final2["print_final_scores(final_score)"]
    Final3["print_final_scores(final_score, max_possible_score)"]
    RiskGlobal["Risk: reads global score instead of parameter"]
    RiskUnused["Risk: final_score parameter unused"]
    Fix["Fix: use explicit final_score parameter"]
    Evidence["Focused source evidence<br/>print_final_scores_source.md"]
    Tests["Regression tests<br/>test_print_final_scores_fix"]

    User --> Step2
    User --> Step3
    Step2 --> Ask2
    Step3 --> Ask3
    Ask2 --> Score
    Ask3 --> Score
    Score --> Final2
    Score --> Final3
    Final2 --> RiskGlobal
    Final3 --> RiskGlobal
    Final2 --> RiskUnused
    Final3 --> RiskUnused
    RiskGlobal --> Evidence
    RiskUnused --> Evidence
    Evidence --> Fix
    Fix --> Tests
```

## What This Shows

This graph shows the bug-critical architecture for the `mathsquiz` subsystem. Both `mathsquiz-step2.py` and `mathsquiz-step3.py` collect score state through quiz execution, then call `print_final_scores(...)`. The architectural defect is that the final-score functions expose parameterized interfaces but depend on hidden module-level `score`.

## Relation To The Fix

The fix changes the final-score boundary:

- Before: `print_final_scores(...) -> global score`
- After: `caller score -> final_score parameter -> print_final_scores(...)`

This reduces hidden coupling and makes the functions testable in isolation.

