# Phase 1 print_final_scores Probe

Date: 2026-06-18

## Purpose

This Phase 1 probe validates the selected graph finding before moving into Phase 2 diagrams and Phase 3 agent workflow design.

The probe does not modify the target code. It isolates the behavior of the two relevant `print_final_scores(...)` functions so the hidden global-state dependency can be demonstrated without running the interactive quiz scripts.

## Command

```powershell
python tests\reproduction\print_final_scores_probe.py
```

## Result

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

The probe confirms the graph finding:

- In the step2 behavior, `final_score=2` is ignored and output follows global `score=0`.
- In the step3 behavior, `final_score=10` is ignored and both score output and feedback follow global `score=0`.
- The bug is therefore not only a style issue. The function interface can produce misleading behavior when the function is called outside the exact original module-level execution path.

## Phase 1 Decision

Proceed to Phase 2 with this official bug-critical path:

```text
module-level quiz flow
-> ask_question(...)
-> score accumulation
-> print_final_scores(final_score, ...)
-> hidden global score read
```
