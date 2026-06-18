# EX04 Knowledge Vault Index

## Project

EX04 - Graph-Guided Reverse Engineering, Debugging, and Token-Efficient Agentic AI

## Current Status

Phases 1-7 are complete for the official `print_final_scores` investigation path.

Repository choice: `martinpeck/broken-python`

Selection status: instructor-approved exception to the general repository-size threshold.

Selected subsystem: [[mathsquiz]]

Selected bug: [[print_final_scores_global_state_bug]]

Official investigation target:

- `print_final_scores` accepts explicit score parameters but reads global `score`.
- Primary files: `mathsquiz/mathsquiz-step2.py` and `mathsquiz/mathsquiz-step3.py`.
- This is the official bug path because it demonstrates hidden state coupling and modular boundary failure.

## Navigation

- [[hot]] - Focused bug investigation context
- [[print_final_scores_global_state_bug]] - Official selected bug path
- [[mathsquiz]] - Selected subsystem notes
- [[architecture]] - Architecture notes and diagrams
- [[components]] - Component map
- [[bug_investigation]] - Investigation timeline
- [[tests_and_verification]] - Reproduction and verification
- [[token_efficiency]] - Naive vs graph-guided comparison
- [[original_extension]] - Extension beyond minimum requirements
- [[hot.generated]] - Generated hot context from suspicious-node ranking

## Required Artifacts

- Graphify output: `../artifacts/graphify/`
- Main graph report: `../artifacts/graphify/GRAPH_REPORT.md`
- Machine-readable graph: `../artifacts/graphify/graph.json`
- Reports: `../reports/`
- Diagrams: `../artifacts/diagrams/`
- Architecture diagram: `../artifacts/diagrams/architecture_block_diagram.md`
- OOP/module diagram: `../artifacts/diagrams/oop_diagram.md`
- Score-state flow diagram: `../artifacts/diagrams/score_state_flow_diagram.md`
- Agent workflow diagram: `../artifacts/diagrams/agent_workflow_diagram.md`
- Logs: `../artifacts/logs/`
- Token efficiency report: `../reports/token_efficiency_report.md`
- Token comparison CSV: `../artifacts/token_measurements/token_comparison.csv`
- Original extension report: `../reports/original_extension_report.md`
- Suspicious-node ranking: `../reports/suspicious_nodes.md`
- Generated hot context: `hot.generated.md`
- Final submission report: `../reports/final_submission_report.md`
- Rubric checklist: `../reports/rubric_submission_checklist.md`
- Successful LangGraph run: `../artifacts/logs/langgraph_run_output.md`
- Visual evidence note: `../artifacts/screenshots/README.md`

## Architecture Status

Phase 2 is complete. The architecture block diagram, module/OOP substitute diagram, score-state flow diagram, and Graphify-style architecture graph exist and are linked from the README and reports.

The score-state flow diagram isolates the exact modularity failure: `print_final_scores(...)` receives explicit parameters but follows a hidden global-state path.

## Resolved Handoff Decisions

- Resolved: the focused Phase 1 probe proves that non-zero `final_score` is ignored when global `score=0`.
- Resolved: Phase 4 fixed both importable target modules, `mathsquiz_step2.py` and `mathsquiz_step3.py`.
- Resolved: graph node references are documented in `artifacts/graphify/GRAPH_REPORT.md`, `reports/suspicious_nodes.md`, and `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md`.

## Phase 5 Status

Phase 5 measured naive raw-code reading against graph-guided investigation.

Best operational result:

- Naive raw-code baseline: 2074 estimated input tokens, 4 text units, 4 iterations.
- Graph-guided hot-context workflow: 1713 estimated input tokens, 2 text units, 2 iterations.
- Reduction: 17.4% fewer estimated input tokens, 50% fewer text units, and 50% fewer iterations.

The full graph-guided audit workflow is documented separately because it includes the complete `graph.json`. It improves traceability, but it is not token-cheaper for this tiny instructor-approved exception repository.

## Phase 6 Status

Phase 6 adds an executable original extension:

- `src/analysis/suspicious_nodes.py` ranks graph nodes by degree, keyword matches, explicit risk labels, and proximity to selected files.
- `src/analysis/hot_md_generator.py` generates `hot.generated.md` from the ranked nodes.
- The ranking prioritizes `print_final_scores` risk nodes and the two selected implementation files.

The extension is complete and included in final packaging.

## Final Submission Path

For grading, start with:

1. `../README.md`
2. `../reports/rubric_submission_checklist.md`
3. `../reports/final_submission_report.md`
4. `[[hot]]`
5. `[[bug_investigation]]`
6. `[[architecture]]`
7. `[[token_efficiency]]`
