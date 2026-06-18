# AI-agents-EX4

Reverse Engineering, Debugging, and Token-Efficient Agentic AI with Graphify and Obsidian.

## Status

Phases 1-7 are complete for the official `print_final_scores` global-state bug in the `mathsquiz` subsystem. The project has graph artifacts, Obsidian notes, architecture diagrams, an executable graph-guided agent workflow, a verified fix, before/after evidence, token-efficiency measurements, an original graph-analysis extension, and final submission packaging.

## Quick Start

Clone and enter the repository:

```bash
git clone https://github.com/areen-at/AI-agents-EX4.git
cd AI-agents-EX4
```

Install dependencies if `uv` is available:

```bash
uv sync --group dev
```

Local fallback commands used for verification:

```bash
python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow tests.unit.test_phase6_analysis
python -m compileall src tests
```

Run the graph-guided agent workflow:

```bash
python -m src.agent.run_agent --json
```

Run the LangGraph engine explicitly after installing dependencies:

```bash
python -m src.agent.run_agent --engine langgraph --json
```

Run the Phase 6 original extension:

```bash
python -m src.analysis.suspicious_nodes --graph artifacts/graphify/graph.json --output reports/suspicious_nodes.md
python -m src.analysis.hot_md_generator --graph artifacts/graphify/graph.json --output obsidian/hot.generated.md
```

Browse the main deliverables:

- Start here: `obsidian/index.md`
- Final checklist: `reports/final_submission_checklist.md`
- Final submission report: `reports/final_submission_report.md`
- Bug analysis: `reports/bug_analysis_report.md`
- Token efficiency: `reports/token_efficiency_report.md`
- Original extension: `reports/original_extension_report.md`

## Assignment Goal

This project will demonstrate reverse engineering, debugging, and token-efficient agentic AI using Graphify, Obsidian, and a graph-guided AI workflow.

The final submission must prove that graph-guided investigation is more focused than naive raw-code reading.

## Repository Choice

Selected repository: [`martinpeck/broken-python`](https://github.com/martinpeck/broken-python)

Selection status: instructor-approved exception.

Minimum repository scale:

- Approximately 10,000+ lines of meaningful code.
- At least 70 source-code files.
- The code may come from our own repository or another approved repository.
- The repository must be large enough to make reverse engineering, graph navigation, modular architecture, and agent-guided context selection meaningful.

Selection strategy:

- Choose a substantial codebase, then select one focused bug, subsystem, or failure path inside it.
- Do not shrink the repository below the assignment scale just to make the bug easier.
- Do keep the investigation focused after Graphify identifies the relevant subgraph.
- Prefer a repository with modular structure, tests, classes/functions, and enough dependencies between components to justify Graphify and Obsidian.

Instructor-approved exception:

- The lecturer explicitly allowed using `martinpeck/broken-python` for this project.
- The repository does not meet the general 10,000+ LOC / 70+ files scale rule.
- Because it is approved, the project will document the size gap transparently and compensate with deeper graph-guided analysis, stronger agent-instruction architecture, and original extensions.

## Selected Bug

Selected subsystem: `mathsquiz`

Official bug path: `print_final_scores` global-state coupling

Primary investigation scope:

- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

Supporting context files:

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz.py`

Bug summary:

`print_final_scores(...)` accepts score data through parameters, but its implementation reads the module-level global variable `score` instead. This creates a hidden dependency between the final-score reporting function and the script's global state. If the function is reused, tested in isolation, or called with a score value that differs from the global variable, it reports the wrong result.

Files and functions involved:

- `mathsquiz/mathsquiz-step2.py`: `print_final_scores(final_score)`
- `mathsquiz/mathsquiz-step3.py`: `print_final_scores(final_score, max_possible_score)`
- Related flow: module-level quiz setup, calls to `ask_question(...)`, score accumulation, final call to `print_final_scores(...)`

Expected fix:

- Use the `final_score` parameter inside `print_final_scores(...)`.
- In `mathsquiz-step3.py`, calculate the percentage from `final_score` and `max_possible_score`.
- Remove the hidden dependency on global `score` from final-score reporting.

The chosen `mathsquiz` bug must support:

- Reproduction before the fix.
- Root-cause analysis.
- A minimal code fix.
- Verification after the fix.
- Graph-guided narrowing of relevant files.

## Research Questions

1. What is the actual architecture of the selected project?
2. What was not obvious from first reading the files?
3. Which modules, classes, or functions are most central?
4. Where are complexity centers, mixed responsibilities, or God nodes?
5. How can architecture and OOP structure be extracted from code?
6. How was the bug identified?
7. What was the root cause?
8. Which steps led to the root cause?
9. What advantage did Graphify provide compared with linear file reading?
10. What advantage did Obsidian provide as a navigation layer?
11. How did the AI agent save tokens or avoid unnecessary code reads?
12. What future improvements or agent mechanisms would be useful?

## Research Question Answers

| Question | Short Answer | Detailed Evidence |
|---|---|---|
| RQ1 architecture | Procedural quiz scripts with module-level execution and function extraction in step2/step3. | `reports/reverse_engineering_report.md`, `artifacts/diagrams/architecture_block_diagram.md` |
| RQ2 non-obvious discovery | `print_final_scores(...)` looks parameterized but secretly reads global `score`. | `obsidian/bug_investigation.md`, `reports/bug_analysis_report.md` |
| RQ3 central components | `ask_question(...)`, `print_final_scores(...)`, score state, and module-level quiz flow. | `obsidian/components.md`, `artifacts/graphify/GRAPH_REPORT.md` |
| RQ4 complexity centers | Score state is the main coupling point; `mathsquiz-step1.py` is a noisy procedural baseline. | `reports/reverse_engineering_report.md`, `reports/suspicious_nodes.md` |
| RQ5 architecture extraction | Static graph analysis plus Mermaid diagrams were used because the subsystem has no classes. | `artifacts/diagrams/oop_diagram.md`, `obsidian/architecture.md` |
| RQ6 bug identification | Graph risk nodes identified `global_score_instead_of_param` and `unused_arg:final_score`. | `reports/suspicious_nodes.md`, `artifacts/logs/graph_guided_agent_log.md` |
| RQ7 root cause | Final-score reporting depends on hidden global state instead of explicit parameters. | `reports/bug_analysis_report.md` |
| RQ8 investigation steps | Graphify-style scan, Obsidian hot context, focused source evidence, reproduction, fix, verification. | `obsidian/hot.md`, `reports/fix_verification_report.md` |
| RQ9 Graphify advantage | It surfaced risk nodes and narrowed attention to two functions and two files. | `artifacts/graphify/GRAPH_REPORT.md` |
| RQ10 Obsidian advantage | It provided a navigable human-readable investigation layer and hot context. | `obsidian/index.md`, `obsidian/hot.generated.md` |
| RQ11 token savings | Hot-context workflow reduced estimated input tokens by 17.4%, text units by 50%, and iterations by 50%. | `reports/token_efficiency_report.md` |
| RQ12 future work | Add traceback-aware ranking, graph diffing, prompt registry, and test-to-component traceability. | `reports/original_extension_report.md` |

## Project Structure

```text
README.md
pyproject.toml
.env-example
docs/
src/
tests/
obsidian/
reports/
artifacts/
data/
config/
notebooks/
```

## Updated Repository-Scale Requirement

The selected target repository must be substantial:

- Approximately 10,000+ meaningful source lines.
- At least 70 source-code files.
- Public, team-owned, or otherwise instructor-approved.

The repository-size evidence will be documented in `reports/repository_size_report.md`.

Current selected repository size:

- Source-code files counted: 5 Python files.
- Total Python lines: 446.
- Meaningful Python lines: 260.
- This is below the general threshold, so the selection relies on the lecturer-approved exception.

## Selected Investigation Subsystem

Subsystem: `mathsquiz`

Rationale:

- It contains multiple related Python scripts that represent an evolving quiz implementation.
- It is suitable for comparing versions/steps and extracting a small architecture from imperfect code.
- It supports focused debugging while still allowing Graphify/Obsidian to demonstrate navigation, hot-context construction, and token reduction.
- It is more suitable than `polygons` as the primary path because it provides a richer interaction flow: random question generation, input parsing, answer validation, score state, loop control, and user-facing behavior.

## Phase 1 Graph Artifacts

Graphify executable was not available locally, so Phase 1 generated Graphify-style static-analysis artifacts from Python AST plus syntax-fallback scanning.

Generation log:

- `artifacts/logs/graphify_run.md`

Generated artifacts:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `artifacts/graphify/graph_metrics.json`
- `artifacts/graphify/graph.html`
- Final architecture graph from graph artifacts: `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md`
- Graphify local install/run report: `reports/graphify_local_run_report.md`

Graph totals:

- Nodes: 47
- Edges: 153
- Files analyzed: 4 `mathsquiz` Python files
- Functions detected: 6
- Bug-risk nodes: 14
- Syntax-error nodes: 1

Official Phase 1 bug decision:

- Selected target: `mathsquiz-step2.py` and `mathsquiz-step3.py` `print_final_scores` global-state coupling.
- Reason: the bug violates modular function design and is directly visible in the graph as a score-state dependency risk.

Rejected/background candidates from Phase 1:

- `mathsquiz/mathsquiz.py`: syntax and baseline logic defects, including Python 2 `print`, assignment inside conditions, invalid `else if`, wrong expected answers, and missing score increments.
- `ask_question(...)`: unguarded `int(answer)` can crash on non-numeric input.

## Agent Instruction Architecture

Before implementing the agent workflow, the project defines explicit agent instructions in:

- `docs/PRD_agent_instruction_architecture.md`

This document specifies agent roles, allowed inputs/outputs, graph-first context rules, evidence format, and modular architecture constraints for agent-generated code.

## Phase 2 Architecture Understanding

Phase 2 reverse engineering has started and produced the first architecture diagrams.

Architecture summary:

- The selected subsystem is procedural and script-first.
- `mathsquiz-step2.py` and `mathsquiz-step3.py` introduce functions, but module-level code still controls score state and execution order.
- There are no classes, so the required OOP view is represented as a module/function interaction diagram.
- The main bug-critical path is `ask_question(...) -> score accumulation -> print_final_scores(...)`.
- The key modularity failure is that `print_final_scores(...)` accepts score parameters but reads global `score`.

Phase 2 artifacts:

- Architecture block diagram: `artifacts/diagrams/architecture_block_diagram.md`
- OOP/module interaction diagram: `artifacts/diagrams/oop_diagram.md`
- Score-state flow diagram: `artifacts/diagrams/score_state_flow_diagram.md`
- Mathsquiz Graphify-style architecture graph: `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md`
- Reverse-engineering report: `reports/reverse_engineering_report.md`
- Phase 2 architecture review: `reports/phase2_architecture_review.md`
- Phase 1 review gate: `reports/phase1_review.md`

## Phase 3 Agent Workflow

Phase 3 is complete. The workflow is designed to read Obsidian and graph artifacts before raw source code, select graph-supported suspects, produce a proposed modular fix, and write a graph-guided investigation log.

The project now includes both:

- A deterministic fallback workflow for local verification.
- A real LangGraph wrapper in `src/agent/langgraph_workflow.py` that uses the same state contract and graph-first stages when LangGraph is installed.

Run command:

```bash
python -m src.agent.run_agent
```

Run with JSON state output:

```bash
python -m src.agent.run_agent --json
```

Run with LangGraph explicitly:

```bash
python -m src.agent.run_agent --engine langgraph --json
```

Phase 3 artifacts:

- Agent workflow diagram: `artifacts/diagrams/agent_workflow_diagram.md`
- Agent workflow report: `reports/agent_workflow_report.md`
- Graph-guided agent log: `artifacts/logs/graph_guided_agent_log.md`
- Phase 3 verification log: `artifacts/logs/phase3_verification.md`
- Agent implementation: `src/agent/`
- LangGraph wrapper: `src/agent/langgraph_workflow.py`

## Phase 4 Root Cause and Fix

Phase 4 is complete for the selected `print_final_scores` bug.

Root cause:

`print_final_scores(...)` accepted score values through parameters but read global `score` internally. This made the output depend on hidden module state instead of the explicit function interface.

Fixed files:

- `src/target_project/mathsquiz/mathsquiz_step2.py`
- `src/target_project/mathsquiz/mathsquiz_step3.py`

Verification command:

```bash
python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow
```

Result: 6 tests passed.

Phase 4 artifacts:

- Bug analysis: `reports/bug_analysis_report.md`
- Fix verification: `reports/fix_verification_report.md`
- Phase 4 review: `reports/phase4_review.md`
- Before evidence: `artifacts/before_after/before.md`
- After evidence: `artifacts/before_after/after.md`
- Fix diff summary: `artifacts/before_after/fix.diff`

## Phase 5 Token Efficiency

Phase 5 is complete. The project compares a naive raw-code reading workflow with graph-guided workflows for the official `print_final_scores` bug.

Best operational comparison:

- Naive raw-code baseline: 4 text units, 8303 characters, 2074 estimated input tokens, 4 investigation iterations, quality 3/5.
- Graph-guided hot-context workflow: 2 text units, 6855 characters, 1713 estimated input tokens, 2 investigation iterations, quality 5/5.
- Reduction from the best operational workflow: 17.4% fewer estimated input tokens, 50% fewer text units, and 50% fewer investigation iterations.

Important limitation:

- The full graph-guided audit workflow uses 15775 estimated input tokens because it includes the complete `graph.json`.
- This full audit mode is useful for traceability, but it is not token-cheaper for the tiny instructor-approved `broken-python` exception repository.
- The token-efficient pattern is to distill Graphify output into `obsidian/hot.md` plus focused source evidence before sending context to an LLM.

Phase 5 artifacts:

- Token efficiency report: `reports/token_efficiency_report.md`
- Token comparison CSV: `artifacts/token_measurements/token_comparison.csv`
- Naive baseline log: `artifacts/logs/naive_baseline_log.md`
- Graph-guided agent log: `artifacts/logs/graph_guided_agent_log.md`
- Phase 5 verification log: `artifacts/logs/phase5_verification.md`
- Phase 5 review: `reports/phase5_review.md`

## Phase 6 Original Extension

Phase 6 is complete. The project adds an executable original extension that ranks suspicious graph nodes and generates a fresh Obsidian hot-context note from the ranking.

Purpose:

- Convert `artifacts/graphify/graph.json` into a small ordered suspect list.
- Prioritize bug-specific risk nodes over noisy high-degree utility calls.
- Generate `obsidian/hot.generated.md` so an agent can start from focused context instead of loading the whole graph.
- Connect the Phase 6 extension back to Phase 5 token efficiency.

Run commands:

```bash
python -m src.analysis.suspicious_nodes --graph artifacts/graphify/graph.json --output reports/suspicious_nodes.md
python -m src.analysis.hot_md_generator --graph artifacts/graphify/graph.json --output obsidian/hot.generated.md
```

Main result:

- The ranking correctly prioritizes `print_final_scores` risk nodes.
- The highest-ranked risks are `unused_arg:final_score` and `global_score_instead_of_param`.
- The top implementation files are `mathsquiz-step2.py` and `mathsquiz-step3.py`.

Phase 6 artifacts:

- Extension report: `reports/original_extension_report.md`
- Suspicious-node report: `reports/suspicious_nodes.md`
- Generated hot context: `obsidian/hot.generated.md`
- Phase 6 review: `reports/phase6_review.md`
- Extension code: `src/analysis/`
- Extension tests: `tests/unit/test_phase6_analysis.py`

## Completed Workflow

1. Select repository and bug.
2. Generate Graphify artifacts.
3. Build Obsidian vault with `index.md` and `hot.md`.
4. Reverse-engineer the architecture.
5. Define detailed agent instructions for modular architecture and code generation.
6. Build a graph-guided LangGraph agent workflow.
7. Reproduce and fix the bug.
8. Compare naive vs graph-guided token efficiency.
9. Add an original extension.
10. Package the final submission.

## Phase 7 Final Packaging

Phase 7 is complete. Final packaging added a grader-oriented README flow, final checklist updates, final submission report, and verification logs.

Phase 7 artifacts:

- Final submission report: `reports/final_submission_report.md`
- Final submission checklist: `reports/final_submission_checklist.md`
- Final verification log: `artifacts/logs/phase7_verification.md`

## Setup

```bash
uv sync
```

If `uv` is not installed:

```bash
python -m pip install uv
uv sync --group dev
```

## Test

```bash
uv run pytest
```

Current local fallback verification:

```bash
python -m unittest tests.unit.test_print_final_scores_fix tests.unit.test_agent_workflow tests.unit.test_phase6_analysis
python -m compileall src tests
```

Note: `uv.lock` is not present in this submitted workspace. The reproducible fallback verification path uses the Python standard library `unittest` and `compileall` commands above.

## Lint

```bash
uv run ruff check .
```

Local note: Ruff is configured in `pyproject.toml`, but `python -m ruff check .` was not available in the final local environment because Ruff was not installed there. This limitation is recorded in `artifacts/logs/phase7_verification.md`.

## Final Limitations

- The selected source repository is much smaller than the general 10,000+ LOC / 70+ file guideline, but it is documented as a lecturer-approved exception.
- Graphify itself was not available locally, so the project generated Graphify-style artifacts with Python AST/static analysis and documented that method.
- Token counts are estimates based on `characters / 4`; no API billing logs were available.
- `uv.lock` is absent in this workspace, so the final verification path uses standard-library commands that do not require dependency installation.
- The project has no UI, so screenshots are not required; visual evidence is represented through Mermaid diagrams and `artifacts/graphify/graph.html`.

## Credits

- Assignment context: EX04 gaphify-obcidian reverse-engineering task and Lecture 07 concepts.
- Selected source repository: `martinpeck/broken-python`.
- Investigation path: `mathsquiz` `print_final_scores` global-state bug.

## Artifact Index

- Planning docs: `docs/`
- Agent instruction architecture: `docs/PRD_agent_instruction_architecture.md`
- Obsidian vault: `obsidian/`
- Reports: `reports/`
- Repository size report: `reports/repository_size_report.md`
- Final submission report: `reports/final_submission_report.md`
- Final submission checklist: `reports/final_submission_checklist.md`
- Final Phase 7 review: `reports/phase7_review.md`
- Phase 4 review: `reports/phase4_review.md`
- Phase 5 token efficiency report: `reports/token_efficiency_report.md`
- Phase 5 review: `reports/phase5_review.md`
- Phase 6 original extension report: `reports/original_extension_report.md`
- Phase 6 suspicious-node report: `reports/suspicious_nodes.md`
- Phase 6 review: `reports/phase6_review.md`
- Phase 7 verification: `artifacts/logs/phase7_verification.md`
- Graphify outputs: `artifacts/graphify/`
- Graphify local run report: `reports/graphify_local_run_report.md`
- Diagrams: `artifacts/diagrams/`
- Architecture block diagram: `artifacts/diagrams/architecture_block_diagram.md`
- OOP/module interaction diagram: `artifacts/diagrams/oop_diagram.md`
- Score-state flow diagram: `artifacts/diagrams/score_state_flow_diagram.md`
- Agent workflow diagram: `artifacts/diagrams/agent_workflow_diagram.md`
- Logs: `artifacts/logs/`
- Phase 1 bug probe: `artifacts/logs/phase1_print_final_scores_probe.md`
- Phase 3 agent log: `artifacts/logs/graph_guided_agent_log.md`
- Phase 3 verification: `artifacts/logs/phase3_verification.md`
- Phase 4 after-fix test log: `artifacts/logs/test_after_fix.md`
- Phase 4 before-fix reproduction: `artifacts/logs/bug_reproduction_before.md`
- Phase 5 naive baseline log: `artifacts/logs/naive_baseline_log.md`
- Phase 5 verification: `artifacts/logs/phase5_verification.md`
- Phase 6 verification: `artifacts/logs/phase6_verification.md`
- Before/after evidence: `artifacts/before_after/`
- Token measurements: `artifacts/token_measurements/`
- Token comparison CSV: `artifacts/token_measurements/token_comparison.csv`
- Analysis extension code: `src/analysis/`
- Generated hot context: `obsidian/hot.generated.md`
