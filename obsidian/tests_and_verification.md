# Tests and Verification

## Before Fix

Official bug: [[print_final_scores_global_state_bug]]

Phase 1 probe:

- Script: `../tests/reproduction/print_final_scores_probe.py`
- Log: `../artifacts/logs/phase1_print_final_scores_probe.md`
- Result: confirmed that both step2 and step3 output follow global `score=0` even when `final_score` is non-zero.

Focused reproduction checks:

- Load or copy the `print_final_scores(...)` implementation from `mathsquiz-step2.py`.
- Set module global `score` to a value different from the function argument.
- Call `print_final_scores(final_score=2)`.
- Capture stdout.
- Expected before fix: output incorrectly follows global `score`.
- Load or copy the `print_final_scores(...)` implementation from `mathsquiz-step3.py`.
- Set module global `score` to a value different from `final_score`.
- Call `print_final_scores(final_score=10, max_possible_score=10)`.
- Capture stdout.
- Expected before fix: output incorrectly reports the global score and global-score percentage.

## After Fix

The same checks should pass because all final-score output and percentage calculations use `final_score`.

## Test Commands

Phase 1 probe command:

```powershell
python tests\reproduction\print_final_scores_probe.py
```

Phase 4 should turn this into a repeatable pytest against the fixed implementation.
