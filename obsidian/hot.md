# Hot Context

## Bug Focus

Selected subsystem: `mathsquiz`

Official selected bug: [[print_final_scores_global_state_bug]]

Primary files:

- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

Supporting context files:

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz.py`

The official Phase 1 bug path is the `print_final_scores` global-state bug. The function accepts score parameters, but reads the module-level global `score`, so its behavior is controlled by hidden external state instead of by its explicit interface.

## Expected Behavior

`print_final_scores(...)` should report and evaluate the score value passed through `final_score`.

## Actual Behavior

`print_final_scores(...)` reads global `score`. If `final_score` and global `score` differ, the output follows the global value rather than the function argument.

## Reproduction Command

Phase 1 reproduction plan:

```text
Set or simulate module global score = 0.
Call print_final_scores(final_score=2) in step2.
Expected: output reports 2.
Actual before fix: output reports 0.

Set or simulate module global score = 0.
Call print_final_scores(final_score=10, max_possible_score=10) in step3.
Expected: output reports 10 and 100%.
Actual before fix: output reports 0 and 0%.
```

## Current Suspects

Active suspects:

- `mathsquiz-step2.py::print_final_scores(final_score)`
- `mathsquiz-step3.py::print_final_scores(final_score, max_possible_score)`
- Module-level global `score`
- Final call sites that pass score values into `print_final_scores(...)`

## Graph Evidence

- `artifacts/graphify/GRAPH_REPORT.md` was generated in Phase 1.
- `artifacts/graphify/graph.json` contains 47 nodes and 153 edges for `mathsquiz`.
- `mathsquiz-step2.py::print_final_scores` has an extracted risk: reads global `score` instead of the `final_score` parameter.
- `mathsquiz-step3.py::print_final_scores` has the same extracted risk.
- `mathsquiz/mathsquiz.py` has syntax and logic risks, but those are rejected/background candidates for this official path.
- `call:print`, `call:input`, `call:int`, and `call:ask_question` are central callable-reference nodes.

## Source Evidence

Initial source evidence from Phase 1 static analysis:

- `mathsquiz-step1.py` is a repaired linear implementation and documents several baseline bug categories in comments.
- `mathsquiz-step2.py` introduces functions: `welcome_message`, `ask_question`, and `print_final_scores`.
- `mathsquiz-step3.py` adds random question generation and `max_possible_score`.
- In both step2 and step3, `print_final_scores` accepts score-related parameters but reads global `score`, creating hidden coupling.
- `mathsquiz.py` cannot parse under Python 3 because of Python 2 print syntax and invalid conditional syntax; this remains background evidence, not the official fix target.

## Root-Cause Hypotheses

- H1 accepted: the final fix should target the architecture bug in `print_final_scores`, because it demonstrates why modular boundaries matter.
- H2 rejected for primary path: the baseline `mathsquiz.py` syntax/logic defects are visible but less useful for modular design analysis.
- H3 deferred: unguarded `int(answer)` remains a robustness issue, but it is not the official Phase 1 investigation target.

## Final Root Cause

`print_final_scores(...)` depends on global `score` despite accepting score data through parameters.

## Fix Summary

Phase 4 fixed the importable target modules:

- `../src/target_project/mathsquiz/mathsquiz_step2.py`
- `../src/target_project/mathsquiz/mathsquiz_step3.py`

Fix:

- Replace internal `score` reads with `final_score`.
- In step3, compute percentage from `final_score / max_possible_score`.

## Verification

Phase 1 probe completed:

- Script: `../tests/reproduction/print_final_scores_probe.py`
- Log: `../artifacts/logs/phase1_print_final_scores_probe.md`
- Result: when global `score=0`, step2 ignores `final_score=2` and step3 ignores `final_score=10`.

Use focused function-level reproduction before and after the fix. The key test condition is `global score != final_score`.

Phase 3 agent workflow completed:

- Command: `python -m src.agent.run_agent`
- Log: `../artifacts/logs/graph_guided_agent_log.md`
- Verification: `../artifacts/logs/phase3_verification.md`
- Result: graph-guided workflow selected 7 `print_final_scores` suspect/risk nodes and proposed the expected modular fix.

Phase 4 verification completed:

- Command: `python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow`
- Result: 6 tests passed.
- Report: `../reports/fix_verification_report.md`
- Before/after: `../artifacts/before_after/`

## Links

- [[index]]
- [[print_final_scores_global_state_bug]]
- [[bug_investigation]]
- [[tests_and_verification]]
