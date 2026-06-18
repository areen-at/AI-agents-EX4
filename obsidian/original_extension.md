# Original Extension

## Selected Extension

Recommended: suspicious-node ranking plus dynamic `hot.md` generation.

## Status

Complete.

## What Was Added

- `src/analysis/graph_loader.py`
- `src/analysis/suspicious_nodes.py`
- `src/analysis/hot_md_generator.py`
- `reports/suspicious_nodes.md`
- `obsidian/hot.generated.md`
- `reports/original_extension_report.md`

## Why It Matters

The extension converts the Graphify artifact into a ranked suspect list and a generated hot-context note. This demonstrates how graph knowledge can drive agent context selection instead of relying on broad raw-code reading.

## Main Result

The ranking selected the official bug path as the highest-priority area:

- `print_final_scores` risk nodes.
- `global_score_instead_of_param` risk nodes.
- `unused_arg:final_score` risk nodes.
- `mathsquiz-step2.py` and `mathsquiz-step3.py` implementation files.

## Links

- [[hot.generated]]
- `../reports/suspicious_nodes.md`
- `../reports/original_extension_report.md`
