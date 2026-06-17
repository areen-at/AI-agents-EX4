# EX04 Knowledge Vault Index

## Project

EX04 - Graph-Guided Reverse Engineering, Debugging, and Token-Efficient Agentic AI

## Current Status

Phase 1 graph and initial knowledge-base setup is complete.

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
- Logs: `../artifacts/logs/`

## Phase 2 Status

Phase 2 has started. The first architecture block diagram and module interaction diagram exist, and the reverse-engineering report now documents entry points, responsibilities, central nodes, bottlenecks, and the OOP assessment.

## Phase 2 Handoff Questions

- Resolved: the focused Phase 1 probe proves that non-zero `final_score` is ignored when global `score=0`.
- Should the Phase 4 fix change both step2 and step3, or use step3 as the main fixed artifact and step2 as comparative evidence?
- Which graph node references should be embedded in the final architecture diagram?
