# Phase 4 Review

Status: complete.

## Scope

Phase 4 handled the selected `print_final_scores` global-state bug.

The fix was implemented in importable target modules committed to this submission repository:

- `src/target_project/mathsquiz/mathsquiz_step2.py`
- `src/target_project/mathsquiz/mathsquiz_step3.py`

The original broken source evidence remains documented in:

- `artifacts/source_evidence/print_final_scores_source.md`
- `artifacts/logs/bug_reproduction_before.md`
- `artifacts/before_after/before.md`

## Review Gates

| Gate | Status | Evidence |
|---|---|---|
| Bug reproduced | Pass | `artifacts/logs/bug_reproduction_before.md` and `artifacts/before_after/before.md` |
| Root cause verified | Pass | `reports/bug_analysis_report.md`, `obsidian/hot.md`, and `artifacts/source_evidence/print_final_scores_source.md` |
| Minimal fix implemented | Pass | `src/target_project/mathsquiz/mathsquiz_step2.py` and `src/target_project/mathsquiz/mathsquiz_step3.py` |
| Regression tests added | Pass | `tests/unit/test_print_final_scores_fix.py` |
| Verification passed | Pass | `artifacts/logs/test_after_fix.md` |
| Before/after evidence documented | Pass | `artifacts/before_after/before.md`, `after.md`, and `fix.diff` |
| Reports updated | Pass | `reports/bug_analysis_report.md` and `reports/fix_verification_report.md` |
| Obsidian updated | Pass | `obsidian/hot.md`, `obsidian/tests_and_verification.md`, and `obsidian/bug_investigation.md` |

## Root-Cause Timeline

1. Graph artifacts marked `print_final_scores` in step2 and step3 as reading global `score`.
2. Phase 1 probe proved the behavior: non-zero `final_score` values still printed `0` when global `score=0`.
3. Phase 2 diagrams showed the hidden state edge from `print_final_scores(...)` back to module-level `score`.
4. Phase 3 agent workflow selected the same function and risk nodes from graph evidence.
5. Phase 4 fixed the function boundary so output and feedback use `final_score`.
6. Regression tests verified the fix with global `score` intentionally different from `final_score`.

## Verification Commands

```powershell
python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow
python -m compileall src tests
```

Results:

- Unit tests: 6 tests passed.
- Compile check: passed.

`pytest` could not be run in the current local environment because it is not installed. The final project-standard command remains:

```powershell
uv run pytest
```

after installing dependencies with:

```powershell
python -m pip install uv
uv sync --group dev
```

## Token-Efficiency Follow-Up

Phase 5 compares:

- Naive investigation: broad/manual reading of source files and broken baseline context.
- Graph-guided investigation: Obsidian + graph report + graph JSON + focused source evidence.

The graph-guided token inputs are recorded in:

- `artifacts/logs/graph_guided_agent_log.md`
