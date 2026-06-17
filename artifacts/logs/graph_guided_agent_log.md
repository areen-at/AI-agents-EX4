# Graph-Guided Agent Log

Status: Phase 3 prepared, not yet executed end-to-end.

## Intended Context Order

1. `obsidian/index.md`
2. `obsidian/hot.md`
3. `artifacts/graphify/GRAPH_REPORT.md`
4. `artifacts/graphify/graph.json`
5. Focused source files:
   - `mathsquiz/mathsquiz-step2.py`
   - `mathsquiz/mathsquiz-step3.py`
6. Phase 1 reproduction probe:
   - `tests/reproduction/print_final_scores_probe.py`
   - `artifacts/logs/phase1_print_final_scores_probe.md`

## Expected Agent Outcome

- Confirm the root cause.
- Recommend replacing hidden global `score` reads with `final_score`.
- Propose a regression test where global `score` differs from `final_score`.
- Avoid unrelated fixes to `mathsquiz.py` and `ask_question(...)` during the primary bug path.

## Preparation Run

- `artifacts/logs/phase3_preparation_run.md`
