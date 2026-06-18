# EX04 Knowledge Vault Index

## Project

EX04 - Graph-Guided Reverse Engineering, Debugging, and Token-Efficient Agentic AI

## Current Status

Phases 1-5 are complete for the official `print_final_scores` investigation path.

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

## Phase 2 Status

Phase 2 has started. The first architecture block diagram and module interaction diagram exist, and the reverse-engineering report now documents entry points, responsibilities, central nodes, bottlenecks, and the OOP assessment.

Phase 2 review added the missing bug-focused score-state flow diagram. The architecture set is now complete enough to move to Phase 3.

## Phase 2 Handoff Questions

- Resolved: the focused Phase 1 probe proves that non-zero `final_score` is ignored when global `score=0`.
- Should the Phase 4 fix change both step2 and step3, or use step3 as the main fixed artifact and step2 as comparative evidence?
- Which graph node references should be embedded in the final architecture diagram?

## Phase 5 Status

Phase 5 measured naive raw-code reading against graph-guided investigation.

Best operational result:

- Naive raw-code baseline: 2074 estimated input tokens, 4 text units, 4 iterations.
- Graph-guided hot-context workflow: 1713 estimated input tokens, 2 text units, 2 iterations.
- Reduction: 17.4% fewer estimated input tokens, 50% fewer text units, and 50% fewer iterations.

The full graph-guided audit workflow is documented separately because it includes the complete `graph.json`. It improves traceability, but it is not token-cheaper for this tiny instructor-approved exception repository.
