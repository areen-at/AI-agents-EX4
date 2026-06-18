# Naive Baseline Log

Status: Phase 5 baseline.

## Method

The naive baseline simulates a broad raw-code reading workflow without Graphify and without Obsidian.

The investigator reads every `mathsquiz` source file linearly:

1. `mathsquiz.py`
2. `mathsquiz-step1.py`
3. `mathsquiz-step2.py`
4. `mathsquiz-step3.py`

This mode does not start from graph risk nodes, hot context, or the selected bug note.

## Text Units Read

| Text Unit | Characters | Estimated Tokens |
|---|---:|---:|
| `mathsquiz.py` | 1539 | 384 |
| `mathsquiz-step1.py` | 3163 | 790 |
| `mathsquiz-step2.py` | 1717 | 429 |
| `mathsquiz-step3.py` | 1884 | 471 |

Total characters: 8303

Total estimated input tokens: 2074

## Investigation Result

- Root cause reached: yes.
- Fix reached: yes.
- Iterations estimated: 4.
- Quality rating: 3/5.

## Interpretation

The naive workflow eventually finds the bug, but it spends attention on unrelated baseline syntax defects and the linear step1 script before reaching the two relevant `print_final_scores(...)` implementations.

This baseline is relatively cheap only because the selected repository is a small lecturer-approved exception. In a larger codebase, broad raw-code reading would scale poorly.
