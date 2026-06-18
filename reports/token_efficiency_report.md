# Token Efficiency Report

Status: Phase 5 complete.

## Purpose

This report compares a naive raw-code reading workflow with graph-guided workflows for the selected `print_final_scores` bug.

The goal is not to claim magic token savings in every situation. The goal is to measure what happened transparently and explain where graph-guided context helps.

## Measurement Method

Text units counted:

- Source files.
- Obsidian notes.
- Graph reports.
- Graph JSON when used.
- Focused source-evidence files.

Token estimate:

```text
estimated_tokens = characters / 4
```

Counts are estimates because no API token logs are available.

Iteration estimate:

An iteration is one investigation cycle:

1. Read context.
2. Form or update hypothesis.
3. Inspect evidence.
4. Decide next step.

Quality rating:

- 1: unclear or unsupported.
- 3: correct but noisy.
- 5: focused, evidence-backed, and fix-ready.

## Baseline: Naive Raw-Code Reading

Log:

- `artifacts/logs/naive_baseline_log.md`

Process:

- Read all four `mathsquiz` source files directly.
- Do not use Graphify.
- Do not use Obsidian.
- Identify root cause by manually comparing scripts and functions.

Measured input:

- Text units: 4.
- Characters: 8303.
- Estimated input tokens: 2074.
- Iterations: 4.
- Root cause reached: yes.
- Fix reached: yes.
- Quality rating: 3/5.

## Graph-Guided Hot-Context Workflow

Process:

- Use Obsidian `hot.md` as the active graph-guided context.
- Use focused source evidence for only the selected bug-critical functions.
- Avoid reading unrelated baseline and step1 code during the active fix path.

Measured input:

- Text units: 2.
- Characters: 6855.
- Estimated input tokens: 1713.
- Iterations: 2.
- Root cause reached: yes.
- Fix reached: yes.
- Quality rating: 5/5.

Reduction compared with naive baseline:

- Token reduction: 17.4%.
- Text-unit reduction: 50%.
- Iteration reduction: 50%.

## Graph-Guided Full Audit Workflow

Log:

- `artifacts/logs/graph_guided_agent_log.md`

Process:

- Read Obsidian context.
- Read `GRAPH_REPORT.md`.
- Read full `graph.json`.
- Read focused source evidence.

Measured input:

- Text units: 5.
- Characters: 61615.
- Estimated input tokens: 15403.
- Iterations: 2.
- Root cause reached: yes.
- Fix reached: yes.
- Quality rating: 5/5.

Important limitation:

The full audit workflow is not token-cheaper than naive reading for this tiny repository. It is more traceable and structured, but `graph.json` dominates the token count.

## Comparison Table

| Mode | Text Units | Characters | Input Tokens | Iterations | Root Cause | Fix | Quality | Notes |
|---|---:|---:|---:|---:|---|---|---:|---|
| Naive raw-code baseline | 4 | 8303 | 2074 | 4 | Yes | Yes | 3 | Reads all source files, including unrelated baseline noise |
| Graph-guided hot-context workflow | 2 | 6855 | 1713 | 2 | Yes | Yes | 5 | Uses `hot.md` and focused source evidence |
| Graph-guided full audit workflow | 5 | 61615 | 15403 | 2 | Yes | Yes | 5 | Includes full `graph.json`; useful but costly here |

CSV:

- `artifacts/token_measurements/token_comparison.csv`

## Interpretation

The best operational workflow is the graph-guided hot-context workflow. It saves tokens, reads fewer units, and reaches the root cause in fewer investigation cycles.

The full graph-guided audit workflow is intentionally heavier because it loads the whole machine-readable graph. This is valuable for traceability and reproducibility, but for the small instructor-approved `broken-python` repository it is not token-efficient.

The key lesson is architectural: Graphify and Obsidian are most useful when the graph is distilled into `hot.md` and focused evidence before being sent to an LLM.

## Limitations

- Token counts are estimated with `characters / 4`.
- Output tokens are not measured.
- The target repository is much smaller than the general assignment scale; the lecturer-approved exception makes this project valid, but it limits the expected token advantage.
- The full graph JSON is oversized relative to the tiny source code.
- Time was not measured with a stopwatch; iteration count is used as a process proxy.

## Conclusion

Phase 5 shows that graph-guided debugging is most efficient when graph artifacts are used to build focused context rather than blindly sending the entire graph to the model.

For this project:

- Hot-context graph-guided mode reduced estimated input tokens by 17.4%.
- It reduced text units by 50%.
- It reduced investigation iterations by 50%.
- It produced a stronger, evidence-backed root-cause explanation.
