# Graphify Local Install and Run Report

Status: completed with documented tool-availability limitation.

## Purpose

This report documents the final attempt to install and run Graphify locally, then records the architecture graph generated for the `mathsquiz` repository.

## Local Discovery

Commands checked:

```powershell
where.exe graphify
python -m pip show graphify
python -m pip show code-graph graphify-code graphify-cli
python -m pip index versions graphify
```

Results:

- No local `graphify` executable was found.
- No installed Python package named `graphify` was found.
- No installed Python packages named `code-graph`, `graphify-code`, or `graphify-cli` were found.
- PyPI returned no matching distribution for `graphify`.
- `npm` was not available in the local shell, so npm-based package probing could not be completed from this environment.

## Interpretation

The course PDF refers to Graphify/Grphify as the graph-generation tool, but the executable or package source was not included with the assignment files and was not discoverable as a standard PyPI package from this environment.

Because the real executable could not be installed locally, the project keeps the previously generated Graphify-style artifacts:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `artifacts/graphify/graph_metrics.json`
- `artifacts/graphify/graph.html`

These were generated from Python AST/static analysis plus syntax-fallback scanning and are documented as Graphify-style rather than official Graphify output.

## Architecture Graph Generated

Generated architecture graph:

- `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md`

The graph focuses on:

- `mathsquiz-step2.py`
- `mathsquiz-step3.py`
- `ask_question(...)`
- module-level score state
- `print_final_scores(...)`
- the `global_score_instead_of_param` and `unused_arg:final_score` risks
- the final fix boundary

## Conclusion

The local Graphify installation could not be completed because no installable tool source was available. The repository therefore documents the blocker transparently and provides a generated architecture graph from the existing Graphify-style artifacts.

If the lecturer provides a concrete Graphify executable, package URL, or command, the expected next command would be run against:

```text
work/target_repos/broken-python/mathsquiz
```

and the official outputs would replace or supplement the current `artifacts/graphify/` files.
