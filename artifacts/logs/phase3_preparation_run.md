# Phase 3 Preparation Run

Status: completed.

## Command

```powershell
python -c "from pathlib import Path; from src.agent.workflow import run_preparation_workflow; import json; state=run_preparation_workflow(Path('.')); print(json.dumps(state, indent=2))"
```

## Result Summary

The deterministic workflow scaffold reached status:

```text
phase3_prepared
```

## Context Units Read

| Text Unit | Characters | Estimated Tokens |
|---|---:|---:|
| `obsidian/index.md` | 2548 | 637 |
| `obsidian/hot.md` | 4032 | 1008 |
| `artifacts/graphify/GRAPH_REPORT.md` | 4628 | 1157 |
| `artifacts/graphify/graph.json` | 47584 | 11896 |

## Ranked Suspects

| Rank | Node | Source File | Reason |
|---:|---|---|---|
| 1 | `call:print_final_scores` | n/a | Selected bug target: final score reporting reads global score. |
| 2 | `function:mathsquiz/mathsquiz-step2.py:print_final_scores` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 3 | `function:mathsquiz/mathsquiz-step3.py:print_final_scores` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |
| 4 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:global_score_instead_of_param` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 5 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:unused_arg:final_score` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 6 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |
| 7 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:unused_arg:final_score` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |

## Proposed Fix

Replace reads of global `score` inside `print_final_scores(...)` with `final_score`; in step3 compute percentage from `final_score / max_possible_score`.

## Verification Plan

Use a regression test where global `score` differs from `final_score` and assert output follows `final_score`.
