# Phase 1 Graph Generation Log

Date: 2026-06-18

## Tool Availability

`graphify` was checked with:

```powershell
where.exe graphify
```

Result:

```text
INFO: Could not find files for the given pattern(s).
```

Because the Graphify executable was not available locally, Phase 1 used a local Graphify-style static analyzer.

## Scope

Source root:

```text
C:\Users\LENOVO\Documents\Codex\2026-06-17\files-mentioned-by-the-user-l07\work\target_repos\broken-python\mathsquiz
```

Analyzed pattern:

```text
mathsquiz/*.py
```

## Generated Artifacts

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `artifacts/graphify/graph_metrics.json`
- `artifacts/graphify/graph.html`

## Result Summary

```json
{
  "nodes": 47,
  "edges": 153,
  "files": 4,
  "functions": 6,
  "bug_risks": 14,
  "syntax_errors": 1
}
```

## Selected Bug Path From Phase 1

Official target: `print_final_scores` global-state coupling.

Evidence:

- `mathsquiz-step2.py::print_final_scores(final_score)` reads global `score`.
- `mathsquiz-step3.py::print_final_scores(final_score, max_possible_score)` reads global `score`.
- The graph marks the `final_score` parameter as unused in both implementations.

## Limitation

This is a Graphify-style substitute, not an official Graphify execution. The limitation is documented in `GRAPH_REPORT.md`, `reports/graphify_local_run_report.md`, and the final README. The generated graph artifacts are used consistently as the project's graph evidence.
