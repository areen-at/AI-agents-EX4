# EX04 - Graph-Guided Reverse Engineering

## Status

Phase 0 scaffold is complete. Repository selection and bug selection are prepared but still need final confirmation before Phase 1.

## Assignment Goal

This project will demonstrate reverse engineering, debugging, and token-efficient agentic AI using Graphify, Obsidian, and a graph-guided AI workflow.

The final submission must prove that graph-guided investigation is more focused than naive raw-code reading.

## Repository Choice

Selected repository: TBD

Recommended first candidate: `martinpeck/broken-python`

Reason for recommendation:

- Small enough for a complete, polished investigation.
- Suitable for a clear bug reproduction and fix.
- Lower setup risk than large real-world bug corpora.

Backup candidates:

- `andela/buggy-python`
- `soarsmu/BugsInPy`

## Selected Bug

Selected bug: TBD

The chosen bug must support:

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

## Planned Workflow

1. Select repository and bug.
2. Generate Graphify artifacts.
3. Build Obsidian vault with `index.md` and `hot.md`.
4. Reverse-engineer the architecture.
5. Build a graph-guided LangGraph agent workflow.
6. Reproduce and fix the bug.
7. Compare naive vs graph-guided token efficiency.
8. Add an original extension.
9. Package the final submission.

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
- Obsidian vault: `obsidian/`
- Reports: `reports/`
- Graphify outputs: `artifacts/graphify/`
- Diagrams: `artifacts/diagrams/`
- Logs: `artifacts/logs/`
- Token measurements: `artifacts/token_measurements/`

