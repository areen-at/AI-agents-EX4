# EX04 Knowledge Vault Index

## Project

EX04 - Graph-Guided Reverse Engineering, Debugging, and Token-Efficient Agentic AI

## Current Status

Phase 1 graph and initial knowledge-base setup is complete.

Repository choice: `martinpeck/broken-python`

Selection status: instructor-approved exception to the general repository-size threshold.

Selected subsystem: [[mathsquiz]]

Selected bug: TBD after final reproduction pass.

Current top candidates:

- Baseline syntax/logic failure in `mathsquiz/mathsquiz.py`.
- State-coupling bug in `print_final_scores` in `mathsquiz-step2.py` and `mathsquiz-step3.py`.

## Navigation

- [[hot]] - Focused bug investigation context
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
- Logs: `../artifacts/logs/`

## Open Questions

- Which exact `mathsquiz` script/behavior will become the primary bug target?
- Should the final fix target the obvious broken baseline or the subtler state-coupling bug?
- Which graph-risk node should become the root of the agent investigation?
