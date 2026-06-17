# Bug Investigation

## Timeline

- Phase 0: selected `martinpeck/broken-python` as lecturer-approved exception.
- Phase 0: selected `mathsquiz` as primary subsystem.
- Phase 1: generated Graphify-style static graph artifacts for `mathsquiz`.
- Phase 1: selected the functional score-state coupling bug as the official path.

## Hypotheses

- H1 accepted: fix `print_final_scores` state coupling because it best demonstrates architecture and modular design.
- H2 rejected for primary path: fix `mathsquiz.py` baseline syntax/logic issues because they are more obvious and less modular.
- H3 deferred: add input validation for non-numeric answers because `int(answer)` can crash.

## Evidence

- `GRAPH_REPORT.md` lists syntax and conditional defects in `mathsquiz.py`.
- `GRAPH_REPORT.md` detects unused `final_score` parameter in step2/step3.
- `GRAPH_REPORT.md` detects reads of global `score` in `print_final_scores`.

## Rejected Hypotheses

- Baseline syntax/logic bug in `mathsquiz.py`: rejected as official target because it is too broad and mostly syntactic.
- Input-conversion crash in `ask_question(...)`: deferred because it is a robustness improvement rather than the central modular architecture bug.

## Official Root-Cause Claim

`print_final_scores(...)` exposes a parameterized interface but ignores the score parameter in favor of global state. The function therefore violates modular design and can report incorrect results when called outside the exact module-level execution path.

## Phase 1 Handoff

- Keep `[[hot]]` centered on `print_final_scores`.
- Build Phase 2 diagrams around `module flow -> score accumulation -> print_final_scores`.
- In Phase 3, instruct the agent to inspect graph/Obsidian context before reading `mathsquiz-step2.py` and `mathsquiz-step3.py`.
- In Phase 4, reproduce by making global `score` differ from `final_score`.
