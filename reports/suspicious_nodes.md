# Suspicious Node Ranking

Status: Phase 6 original extension output.

## Purpose

This report ranks Graphify-style nodes by how useful they are for investigating the selected `print_final_scores` global-state bug.

## Scoring Method

Each node receives a combined score from:

- Structural degree, capped to avoid over-rewarding generic utility calls.
- Keyword matches for `print_final_scores`, `final_score`, `score`, `global`, `unused`, `parameter`, and `percentage`.
- Explicit graph risk signals such as `global_score_instead_of_param` and `unused_arg`.
- Proximity to selected files and risk nodes.
- Small type bonuses for file, function, and state-variable nodes.

Generic calls such as `print`, `input`, `int`, `range`, and `randint` are dampened because they are central but not bug-specific.

## Top 10 Suspicious Nodes

| Rank | Node | Type | Source File | Total | Keywords | Risk | Proximity | Reasons |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:unused_arg:final_score` | bug_risk | `mathsquiz/mathsquiz-step2.py` | 52 | 5 | 12 | 14 | explicit graph risk signal; matches selected bug keywords; near selected files or risk nodes |
| 2 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:unused_arg:final_score` | bug_risk | `mathsquiz/mathsquiz-step3.py` | 52 | 5 | 12 | 14 | explicit graph risk signal; matches selected bug keywords; near selected files or risk nodes |
| 3 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:global_score_instead_of_param` | bug_risk | `mathsquiz/mathsquiz-step2.py` | 49 | 4 | 14 | 14 | explicit graph risk signal; matches selected bug keywords; near selected files or risk nodes |
| 4 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param` | bug_risk | `mathsquiz/mathsquiz-step3.py` | 49 | 4 | 14 | 14 | explicit graph risk signal; matches selected bug keywords; near selected files or risk nodes |
| 5 | `function:mathsquiz/mathsquiz-step2.py:print_final_scores` | function | `mathsquiz/mathsquiz-step2.py` | 40 | 3 | 0 | 14 | matches selected bug keywords; near selected files or risk nodes; architectural function node |
| 6 | `function:mathsquiz/mathsquiz-step3.py:print_final_scores` | function | `mathsquiz/mathsquiz-step3.py` | 40 | 3 | 0 | 14 | matches selected bug keywords; near selected files or risk nodes; architectural function node |
| 7 | `call:print_final_scores` | callable_reference | `n/a` | 24 | 3 | 0 | 7 | matches selected bug keywords; near selected files or risk nodes |
| 8 | `file:mathsquiz/mathsquiz-step2.py` | file | `mathsquiz/mathsquiz-step2.py` | 23 | 0 | 0 | 9 | near selected files or risk nodes; architectural file node |
| 9 | `file:mathsquiz/mathsquiz-step3.py` | file | `mathsquiz/mathsquiz-step3.py` | 23 | 0 | 0 | 9 | near selected files or risk nodes; architectural file node |
| 10 | `file:mathsquiz/mathsquiz.py` | file | `mathsquiz/mathsquiz.py` | 17 | 0 | 0 | 3 | near selected files or risk nodes; architectural file node |

## Top Source Files

- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

Only files connected to high-scoring nodes are listed here. Lower-scoring background files remain available in the graph, but they are not part of the recommended first context load.

## How This Improves Context Selection

The ranking turns the large graph artifact into a small, ordered suspect list. Instead of asking an LLM to read every source file or the entire `graph.json`, an agent can begin with the highest-ranked function and risk nodes, then load only the associated source evidence.

## Limitations

- The ranking is heuristic, not a formal proof.
- It depends on graph quality and risk-node naming.
- The selected repository is small, so the benefit is clearer as a method demonstration than as a large absolute token saving.
- Runtime behavior still requires tests or reproduction probes.
