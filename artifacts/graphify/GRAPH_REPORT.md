# GRAPH_REPORT - mathsquiz
## Generation Method
Graphify executable was not available in PATH. This report was generated with a local Graphify-style static analyzer using Python AST parsing plus fallback line scanning for syntax-broken files.
## Scope
Source root: `C:\Users\LENOVO\Documents\Codex\2026-06-17\files-mentioned-by-the-user-l07\work\target_repos\broken-python\mathsquiz`
Analyzed files: `mathsquiz/*.py`
## Totals
- nodes: 47
- edges: 153
- files: 4
- functions: 6
- bug_risks: 14
- syntax_errors: 1

## File Metrics
| File | Parse Status | Total Lines | Meaningful Lines | Functions |
|---|---|---:|---:|---|
| `mathsquiz/mathsquiz-step1.py` | parsed | 158 | 93 | - |
| `mathsquiz/mathsquiz-step2.py` | parsed | 57 | 38 | welcome_message, ask_question, print_final_scores |
| `mathsquiz/mathsquiz-step3.py` | parsed | 62 | 37 | welcome_message, ask_question, print_final_scores |
| `mathsquiz/mathsquiz.py` | syntax_error | 94 | 53 | - |

## Top Nodes By Degree
| Node | Type | Degree |
|---|---|---:|
| `call:print` | callable_reference | 73 |
| `file:mathsquiz/mathsquiz-step1.py` | file | 72 |
| `file:mathsquiz/mathsquiz-step2.py` | file | 20 |
| `file:mathsquiz/mathsquiz-step3.py` | file | 20 |
| `call:input` | callable_reference | 12 |
| `call:int` | callable_reference | 12 |
| `file:mathsquiz/mathsquiz.py` | file | 12 |
| `call:ask_question` | callable_reference | 11 |
| `function:mathsquiz/mathsquiz-step2.py:print_final_scores` | function | 9 |
| `function:mathsquiz/mathsquiz-step3.py:print_final_scores` | function | 9 |

## Initial Bug-Risk Findings
- `unused parameter final_score` in `mathsquiz/mathsquiz-step2.py` line 23; type=bug_risk; degree=1
- `reads global score instead of final_score` in `mathsquiz/mathsquiz-step2.py` line 23; type=bug_risk; degree=1
- `unused parameter final_score` in `mathsquiz/mathsquiz-step3.py` line 27; type=bug_risk; degree=1
- `reads global score instead of final_score` in `mathsquiz/mathsquiz-step3.py` line 27; type=bug_risk; degree=1
- `SyntaxError line 3` in `mathsquiz/mathsquiz.py` line 3; type=syntax_error; degree=1
- `Python 2 print syntax` in `mathsquiz/mathsquiz.py` line 3; type=bug_risk; degree=1
- `Python 2 print syntax` in `mathsquiz/mathsquiz.py` line 4; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 14; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 25; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 36; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 47; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 58; type=bug_risk; degree=1
- `assignment in condition` in `mathsquiz/mathsquiz.py` line 70; type=bug_risk; degree=1
- `invalid else if` in `mathsquiz/mathsquiz.py` line 91; type=bug_risk; degree=1
- `invalid else if` in `mathsquiz/mathsquiz.py` line 93; type=bug_risk; degree=1

## Initial Interpretation
- `mathsquiz.py` appears to be the intentionally broken baseline with Python 2 print syntax, assignment inside conditions, invalid `else if`, incorrect answers, and missing score updates.
- `mathsquiz-step1.py` is a repaired linear version and documents the baseline bug categories in comments.
- `mathsquiz-step2.py` refactors the quiz into functions, introducing a likely state bug: `print_final_scores(final_score)` receives a parameter but reads global `score`.
- `mathsquiz-step3.py` adds randomness and max score handling, but `print_final_scores(final_score, max_possible_score)` still reads global `score` instead of `final_score`.

## Phase 1 Next Use
Use this graph to update `obsidian/index.md`, `obsidian/hot.md`, `obsidian/mathsquiz.md`, and the reverse-engineering report before choosing the final bug fix for Phase 4.
