# Mathsquiz Subsystem

## Status

Selected as the primary EX04 investigation subsystem.

## Source Files

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`
- `mathsquiz/mathsquiz.py`

## Why This Subsystem

- It contains several related scripts that show an evolving quiz program.
- It has enough behavior to support root-cause investigation: random question generation, input parsing, answer validation, score state, and loop control.
- It is compact enough for a complete investigation while still allowing Graphify and Obsidian to demonstrate focused navigation.
- It is more suitable than `polygons` as the primary path because it includes interactive stateful behavior.

## Initial Investigation Questions

- Which script contains the best bug candidate for a reproducible before/after fix?
- How do the step files relate to the final `mathsquiz.py`?
- Which functions or blocks are central to quiz flow?
- Where does user input enter the system?
- Where is the answer checked?
- Where is score state updated?

## Phase 1 Graph Summary

Generated artifacts:

- `../artifacts/graphify/graph.json`
- `../artifacts/graphify/GRAPH_REPORT.md`
- `../artifacts/graphify/graph_metrics.json`
- `../artifacts/graphify/graph.html`

Totals:

- Nodes: 47
- Edges: 153
- Files analyzed: 4
- Functions detected: 6
- Bug-risk nodes: 14
- Syntax-error nodes: 1

## File-Level Findings

| File | Parse Status | Role |
|---|---|---|
| `mathsquiz/mathsquiz.py` | syntax error | Intentionally broken baseline with syntax and logic defects |
| `mathsquiz/mathsquiz-step1.py` | parsed | Linear repaired version |
| `mathsquiz/mathsquiz-step2.py` | parsed | Functional refactor with score-state risk |
| `mathsquiz/mathsquiz-step3.py` | parsed | Randomized quiz version with score-state risk |

## Candidate Bug Paths

### Candidate A: Broken Baseline

Target: `mathsquiz/mathsquiz.py`

Evidence:

- Python 2 print syntax.
- Assignment inside `if` conditions.
- Invalid `else if`.
- Wrong expected answers.
- Missing score increments.

Value:

- Easy to reproduce.
- Clear before/after fix.
- Less architecturally subtle.

### Candidate B: Hidden State Coupling

Target: `print_final_scores` in `mathsquiz-step2.py` and/or `mathsquiz-step3.py`

Evidence:

- Function receives `final_score`.
- Function reads global `score`.
- The parameter is effectively unused.

Value:

- Better architectural discussion.
- Demonstrates modularity and function-boundary correctness.
- Stronger fit for agent-instruction architecture.

## Links

- [[index]]
- [[hot]]
- [[bug_investigation]]
- [[tests_and_verification]]
