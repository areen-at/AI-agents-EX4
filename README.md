# AI-agents-EX4

Reverse Engineering, Debugging, and Token-Efficient Agentic AI with Graphify and Obsidian.

## Status

Phase 0 scaffold is mostly complete. The repository and investigation subsystem are selected; the remaining Phase 0 work is to choose the exact `mathsquiz` bug instance and prepare the first reproduction note before Phase 1.

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

Selected subsystem / bug path: `mathsquiz`

Primary investigation scope:

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`
- `mathsquiz/mathsquiz.py`

The exact bug instance will be selected during the final Phase 0 reproduction pass. The graph-guided investigation will focus on how the quiz flow handles question generation, user input, answer checking, score tracking, and termination behavior.

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

## Agent Instruction Architecture

Before implementing the agent workflow, the project defines explicit agent instructions in:

- `docs/PRD_agent_instruction_architecture.md`

This document specifies agent roles, allowed inputs/outputs, graph-first context rules, evidence format, and modular architecture constraints for agent-generated code.

## Planned Workflow

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

## Setup

```bash
uv sync
```

## Test

```bash
uv run pytest
```

## Lint

```bash
uv run ruff check .
```

## Artifact Index

- Planning docs: `docs/`
- Agent instruction architecture: `docs/PRD_agent_instruction_architecture.md`
- Obsidian vault: `obsidian/`
- Reports: `reports/`
- Repository size report: `reports/repository_size_report.md`
- Graphify outputs: `artifacts/graphify/`
- Diagrams: `artifacts/diagrams/`
- Logs: `artifacts/logs/`
- Token measurements: `artifacts/token_measurements/`
