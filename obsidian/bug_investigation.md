# Bug Investigation

## Timeline

- Phase 0: selected `martinpeck/broken-python` as lecturer-approved exception.
- Phase 0: selected `mathsquiz` as primary subsystem.
- Phase 1: generated Graphify-style static graph artifacts for `mathsquiz`.
- Phase 1: identified two candidate bug paths: baseline syntax/logic defects and functional score-state coupling.

## Hypotheses

- H1: Fix `mathsquiz.py` as the primary bug because it is the most visibly broken script.
- H2: Fix `print_final_scores` state coupling because it better demonstrates architecture and modular design.
- H3: Add input validation for non-numeric answers because `int(answer)` can crash.

## Evidence

- `GRAPH_REPORT.md` lists syntax and conditional defects in `mathsquiz.py`.
- `GRAPH_REPORT.md` detects unused `final_score` parameter in step2/step3.
- `GRAPH_REPORT.md` detects reads of global `score` in `print_final_scores`.

## Rejected Hypotheses

TBD
