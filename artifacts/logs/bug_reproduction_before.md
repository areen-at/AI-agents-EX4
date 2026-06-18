# Bug Reproduction Before Fix

## Command

```powershell
python tests\reproduction\print_final_scores_probe.py
```

## Output

```text
PHASE 1 BUG PROBE: print_final_scores global-state coupling

Step2 probe
Expected if modular: output uses final_score=2
Actual before fix:
That's all the questions done. So...what was your score...?
You scored 0 points out of a possible 10.
You need to practice your maths!

Step3 probe
Expected if modular: output uses final_score=10 and percentage=100
Actual before fix:
That's all the questions done. So...what was your score...?
You scored 0 points out of a possible 10
You need to practice your maths!
```

## Interpretation

The before-fix behavior proves that `print_final_scores(...)` follows global `score=0` instead of the non-zero `final_score` argument.
