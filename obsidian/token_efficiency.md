# Token Efficiency

## Baseline Mode

Naive raw-code baseline:

- Reads all four `mathsquiz` source files.
- Does not use Graphify.
- Does not use Obsidian.
- Estimated input tokens: 2074.
- Iterations: 4.
- Quality: 3/5.

Log: `../artifacts/logs/naive_baseline_log.md`

## Graph-Guided Mode

Operational hot-context mode:

- Reads `hot.md`.
- Reads focused source evidence for `print_final_scores`.
- Estimated input tokens: 1713.
- Iterations: 2.
- Quality: 5/5.

Full audit mode:

- Reads Obsidian context, Graphify report, full `graph.json`, and focused evidence.
- Estimated input tokens: 15924.
- Useful for traceability but not token-cheaper in this tiny repository.

## Comparison

Best operational comparison:

- Token reduction: 17.4%.
- Text-unit reduction: 50%.
- Iteration reduction: 50%.

Full report: `../reports/token_efficiency_report.md`

CSV: `../artifacts/token_measurements/token_comparison.csv`

