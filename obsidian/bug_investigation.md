# Bug Investigation

## Timeline

- Phase 0: selected `martinpeck/broken-python` as lecturer-approved exception.
- Phase 0: selected `mathsquiz` as primary subsystem.
- Phase 1: generated Graphify-style static graph artifacts for `mathsquiz`.
- Phase 1: selected the functional score-state coupling bug as the official path.
- Phase 3: executed graph-guided workflow and selected `print_final_scores` graph/risk nodes as suspects.
- Phase 4: fixed `print_final_scores` in importable target modules and verified with regression tests.

## Hypotheses

- H1 accepted: fix `print_final_scores` state coupling because it best demonstrates architecture and modular design.
- H2 rejected for primary path: fix `mathsquiz.py` baseline syntax/logic issues because they are more obvious and less modular.
- H3 deferred: add input validation for non-numeric answers because `int(answer)` can crash.

## Evidence

- `GRAPH_REPORT.md` lists syntax and conditional defects in `mathsquiz.py`.
- `GRAPH_REPORT.md` detects unused `final_score` parameter in step2/step3.
- `GRAPH_REPORT.md` detects reads of global `score` in `print_final_scores`.
- `phase1_print_final_scores_probe.md` confirms the failure mode: output follows global `score=0` even when `final_score` is non-zero.
- `graph_guided_agent_log.md` records the Phase 3 agent workflow: Obsidian first, graph artifacts second, ranked `print_final_scores` suspects third.

## Rejected Hypotheses

- Baseline syntax/logic bug in `mathsquiz.py`: rejected as official target because it is too broad and mostly syntactic.
- Input-conversion crash in `ask_question(...)`: deferred because it is a robustness improvement rather than the central modular architecture bug.

## Official Root-Cause Claim

`print_final_scores(...)` exposes a parameterized interface but ignores the score parameter in favor of global state. The function therefore violates modular design and can report incorrect results when called outside the exact module-level execution path.

## Phase 4 Fix

- Fixed files:
  - `../src/target_project/mathsquiz/mathsquiz_step2.py`
  - `../src/target_project/mathsquiz/mathsquiz_step3.py`
- Regression tests:
  - `../tests/unit/test_print_final_scores_fix.py`
- Verification:
  - `python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow`
  - Result: 6 tests passed.
