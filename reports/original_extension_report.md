# Original Extension Report

Status: Phase 6 complete.

## Extension Title

Suspicious Node Ranking and Dynamic Hot-Context Generation.

## Motivation

The assignment asks for more than a manual bug fix. It asks for agent instructions, modular architecture, graph-guided investigation, and original thinking about how to reduce unnecessary LLM context.

This extension adds a reusable bridge between Graphify output and agent context selection. Instead of manually deciding which graph nodes matter, the project now ranks suspicious nodes and generates a focused Obsidian note that an agent can use before reading raw code.

## Inputs

- `artifacts/graphify/graph.json`
- Selected bug keywords:
  - `print_final_scores`
  - `final_score`
  - `score`
  - `global`
  - `unused`
  - `parameter`
  - `percentage`
- Selected files:
  - `mathsquiz/mathsquiz-step2.py`
  - `mathsquiz/mathsquiz-step3.py`
- Phase 4 diff summary:
  - `artifacts/before_after/fix.diff`

## Implementation

Code:

- `src/analysis/graph_loader.py`
- `src/analysis/suspicious_nodes.py`
- `src/analysis/hot_md_generator.py`

Commands:

```bash
python -m src.analysis.suspicious_nodes --graph artifacts/graphify/graph.json --output reports/suspicious_nodes.md
python -m src.analysis.hot_md_generator --graph artifacts/graphify/graph.json --output obsidian/hot.generated.md
```

## Algorithm

The ranking combines:

- Structural degree, capped so generic call nodes do not dominate.
- Keyword matches against the selected bug vocabulary.
- Explicit graph risk signals, especially `global_score_instead_of_param` and `unused_arg`.
- Proximity to selected files and risk nodes.
- Small type bonuses for file, function, and state-variable nodes.

Generic calls such as `print`, `input`, `int`, `range`, and `randint` are dampened. They are structurally common but not bug-specific.

## Outputs

- `reports/suspicious_nodes.md`
- `obsidian/hot.generated.md`
- `tests/unit/test_phase6_analysis.py`

## Example Result

The top suspicious nodes are:

1. `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:unused_arg:final_score`
2. `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:unused_arg:final_score`
3. `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:global_score_instead_of_param`
4. `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param`
5. `function:mathsquiz/mathsquiz-step2.py:print_final_scores`
6. `function:mathsquiz/mathsquiz-step3.py:print_final_scores`

This matches the official bug path and confirms that the graph can point an agent to the correct repair boundary.

## How It Improves Context Selection

The extension turns the full graph into a short ranked suspect list. An agent can now start with:

1. `obsidian/hot.generated.md`
2. `reports/suspicious_nodes.md`
3. `artifacts/source_evidence/print_final_scores_source.md`

This supports Phase 5's token-efficiency conclusion: the best workflow is not to load the whole graph, but to distill it into hot context and focused source evidence.

## How It Exceeds Minimum Requirements

The minimum assignment could be satisfied with manual diagrams, reports, and a bug fix. This extension adds executable analysis code that generates new investigation artifacts from the graph. It is reusable for future bug paths because the ranking logic is data-driven and separated from the reports.

## Limitations

- The ranking is heuristic.
- It depends on the quality and naming of graph risk nodes.
- The repository is small, so the absolute token saving is modest.
- The method should be tested on larger repositories before treating the scores as general-purpose suspiciousness metrics.

## Future Improvements

- Add runtime traceback keywords to the ranking.
- Add test-name proximity.
- Generate a before/after graph diff.
- Tune weights across multiple bug paths.
- Export the ranking as JSON for downstream agent workflows.
