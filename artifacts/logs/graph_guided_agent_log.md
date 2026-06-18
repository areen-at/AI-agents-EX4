# Graph-Guided Agent Log

Status: Phase 3 executed.

## Bug Target

print_final_scores accepts final_score but reads global score.

## Context Order Used

The workflow read Obsidian context first, then graph artifacts, then selected graph suspects.

## Text Units Read

| Text Unit | Characters | Estimated Tokens |
|---|---:|---:|
| `obsidian\index.md` | 2548 | 637 |
| `obsidian\hot.md` | 4345 | 1086 |
| `artifacts\graphify\GRAPH_REPORT.md` | 4628 | 1157 |
| `artifacts\graphify\graph.json` | 47584 | 11896 |
| `artifacts\source_evidence\print_final_scores_source.md` | 2038 | 509 |

Total estimated input tokens: 15285

## Ranked Suspect Nodes

| Rank | Node | Source File | Reason |
|---:|---|---|---|
| 1 | `call:print_final_scores` | `n/a` | Selected bug target: final score reporting reads global score. |
| 2 | `function:mathsquiz/mathsquiz-step2.py:print_final_scores` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 3 | `function:mathsquiz/mathsquiz-step3.py:print_final_scores` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |
| 4 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:global_score_instead_of_param` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 5 | `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:unused_arg:final_score` | `mathsquiz/mathsquiz-step2.py` | Selected bug target: final score reporting reads global score. |
| 6 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |
| 7 | `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:unused_arg:final_score` | `mathsquiz/mathsquiz-step3.py` | Selected bug target: final score reporting reads global score. |

## Evidence

| Claim | Source | Type | Confidence | Verification Step |
|---|---|---|---|---|
| print_final_scores is the graph-selected bug-critical function. | `artifacts/graphify/GRAPH_REPORT.md and graph.json` | graph | high | Read step2 and step3 source before implementing the fix. |
| Focused source evidence confirms final_score is ignored in step2 and step3. | `artifacts/source_evidence/print_final_scores_source.md` | source | high | Use this evidence to create a Phase 4 regression test before fixing. |

## Proposed Fix

Replace reads of global score inside print_final_scores with final_score; in step3 compute percentage from final_score / max_possible_score.

## Verification Plan

Use a regression test where global score differs from final_score and assert output follows final_score.

## Run Status

phase3_executed
