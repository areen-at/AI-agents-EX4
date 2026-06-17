# EX04 Product Requirements Document

## 1. Project Overview

### 1.1 Project Name

EX04 - Graph-Guided Reverse Engineering, Debugging, and Token-Efficient Agentic AI

### 1.2 Purpose

This project demonstrates a complete engineering investigation of an unfamiliar Python codebase using Graphify, Obsidian, and an AI agent workflow. The goal is to prove that graph-guided reverse engineering is more focused, more explainable, and more token-efficient than naive raw-code reading.

The project must not be limited to fixing a bug. It must produce a documented investigation process, a knowledge architecture, an agentic workflow, a verified code fix, and measurable before/after evidence.

### 1.3 Assignment Context

The assignment is based on Lecture 07 concepts:

- Reverse engineering unfamiliar code through graph knowledge systems.
- Using Graphify to convert source code and documentation into graph artifacts.
- Using Obsidian as an active human-readable knowledge vault.
- Using `index.md` and `hot.md` to reduce context-window noise.
- Avoiding `Lost in the Middle` by keeping critical context short, structured, and near the active task.
- Measuring token efficiency between naive and graph-guided workflows.
- Using an agent workflow with CrewAI or LangGraph to investigate and explain bugs.

The project must also respect the professional software submission guidelines:

- Clear `README.md`.
- Required planning and documentation.
- Professional repository structure.
- Tests and verification.
- No secrets in code.
- Dependency management through `uv` if possible.
- Meaningful architecture and OOP documentation.

## 2. Target Users

### 2.1 Primary Users

- Course instructor and graders reviewing the final GitHub repository.
- Student team members using the repository to continue development.

### 2.2 Secondary Users

- External engineers who want to understand how Graphify and Obsidian help reverse-engineer a Python project.
- Future students looking for a reproducible example of graph-guided debugging.

## 3. Problem Statement

When developers inspect unfamiliar code naively, they often read many files linearly, overload the LLM context window, waste tokens, and still miss architectural relationships. This assignment requires proving that a graph-guided workflow can identify the important areas of a codebase faster and with fewer irrelevant reads.

The project must answer:

- What is the real architecture of the selected codebase?
- Which components are central, risky, or suspicious?
- Where is the investigated bug located?
- What is the root cause?
- How did Graphify and Obsidian reduce unnecessary context?
- How did the AI agent use graph knowledge before reading raw code?
- What changed after the fix?

## 4. Scope

### 4.1 In Scope

- Selecting one unfamiliar Python repository or a justified combination of repositories.
- Running Graphify or producing equivalent Graphify-style artifacts if the tool requires adaptation.
- Building an Obsidian vault from the graph and investigation.
- Implementing a CrewAI or LangGraph agent workflow.
- Investigating at least one real bug.
- Fixing the bug in code.
- Adding or updating tests that prove the fix.
- Producing architecture and OOP diagrams.
- Producing token-efficiency measurements.
- Creating final reports and README documentation.
- Adding at least one original extension beyond the minimum assignment requirements.

### 4.2 Out of Scope

- Building a large production application unrelated to the assignment.
- Solving many bugs without deep documentation.
- Sending the whole repository blindly to an LLM.
- Creating an overly complex multi-agent system that is hard to explain.
- Spending major effort on environment problems instead of the graph-guided investigation.

## 5. Repository Selection Requirements

### 5.1 Candidate Repositories

The assignment recommends:

- `soarsmu/BugsInPy`: realistic Python bugs, but potentially complex environment setup.
- `martinpeck/broken-python`: smaller Python debugging examples.
- `andela/buggy-python`: buggy Python scripts suitable for simpler investigation.

### 5.2 Selection Criteria

The selected repository must:

- Be unfamiliar to the team.
- Be small or medium enough to complete within assignment time.
- Contain at least one bug that can be investigated, explained, fixed, and tested.
- Have enough structure to support graph analysis.
- Allow meaningful before/after documentation.

### 5.3 Required Documentation

The final `README.md` must explain:

- Which repository was selected.
- Why it was selected.
- Why it fits EX04 goals.
- What bug or defect was chosen for detailed investigation.

## 6. Functional Requirements

### FR-1: Graphify Representation

The system shall generate a graph-based representation of the selected codebase.

Required outputs:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- Any generated HTML, image, or supporting report from Graphify.

The graph representation should identify:

- Files.
- Modules.
- Functions.
- Classes.
- Imports.
- Calls.
- Relevant semantic or documentation links when available.
- Central or suspicious nodes when available.

Acceptance criteria:

- Graph artifacts are committed to the final repository.
- The README explains how the graph was generated.
- Reports are referenced from Obsidian pages and final analysis.

### FR-2: Obsidian Knowledge Vault

The system shall include an Obsidian-compatible Markdown vault that acts as an active knowledge space.

Required files:

- `obsidian/index.md`
- `obsidian/hot.md`
- Additional linked Markdown pages for components, bug investigation, tests, suspects, and fix notes.

`index.md` must include:

- System overview.
- Main navigation paths.
- Links to architecture notes.
- Links to bug investigation notes.
- Links to reports and token-efficiency results.

`hot.md` must include:

- Focused context for the bug-critical area.
- Suspected files/components.
- Key graph evidence.
- Relevant source snippets or source references.
- Root-cause hypothesis.
- Final root-cause conclusion after verification.

Acceptance criteria:

- Vault files use Obsidian-style links where useful.
- Vault is not a dump of raw files.
- The vault supports a reader in navigating from overview to bug evidence.

### FR-3: Reverse Engineering Analysis

The project shall reverse-engineer the selected codebase using graph-guided analysis.

Required analysis:

- High-level architecture.
- Main modules and responsibilities.
- Central components.
- Potential God nodes or bottlenecks.
- Mixed-responsibility or ambiguous areas.
- How documentation differs from implementation if applicable.

Acceptance criteria:

- Findings are documented in `reports/reverse_engineering_report.md`.
- Findings are linked from Obsidian.
- Claims distinguish graph evidence from verified source evidence.

### FR-4: Architecture Block Diagram

The project shall include an architectural block diagram.

The diagram must show:

- Major system blocks.
- Control flow or data flow.
- Entry points.
- Services or core modules.
- External dependencies if present.
- The bug-critical path if possible.

Acceptance criteria:

- Diagram exists in `artifacts/diagrams/architecture_block_diagram.md` or image format.
- The README embeds or links to the diagram.
- The diagram reflects actual code understanding, not only folder structure.

### FR-5: OOP Diagram

The project shall include an OOP diagram when the selected repository has classes or object-style structure.

The diagram should show:

- Classes.
- Inheritance.
- Composition.
- Usage relationships.
- Wrappers or adapters if present.

If the selected project is mostly procedural, the project must explain that and provide a functional/module interaction diagram instead.

Acceptance criteria:

- Diagram exists in `artifacts/diagrams/oop_diagram.md` or image format.
- README explains the diagram and its relevance.

### FR-6: AI Agent Workflow

The project shall implement an AI agent workflow using CrewAI or LangGraph.

The workflow must:

- Start from graph artifacts and Obsidian notes.
- Read `index.md` and `hot.md` before raw code.
- Request only relevant source files or snippets.
- Produce a structured bug investigation trace.
- Explain the root-cause hypothesis.
- Suggest or support a fix.

Acceptance criteria:

- Agent implementation exists under `src/agent/` or equivalent.
- Workflow is documented in README and `reports/agent_workflow_report.md`.
- The workflow shows steps and context-narrowing strategy.
- The agent is not just a single prompt over the whole repository.

### FR-7: Bug Identification and Root Cause

The project shall identify and explain at least one real bug.

Required documentation:

- Bug summary.
- Failing behavior.
- Reproduction steps.
- Suspected components.
- Graph evidence.
- Source-level evidence.
- Root cause.
- Why the bug was not obvious from a first glance.

Acceptance criteria:

- Bug analysis exists in `reports/bug_analysis_report.md`.
- Root cause is tied to source files and tests.
- Report clearly separates hypotheses from verified facts.

### FR-8: Code Fix

The project shall implement a real code fix for the selected bug.

Acceptance criteria:

- Code is changed in the selected project.
- Fix is minimal and justified.
- Tests pass after the fix.
- Before/after behavior is documented.
- README explains how to run the verification.

### FR-9: Verification Tests

The project shall include tests or repeatable checks proving the bug and fix.

Required:

- A failing test or reproduction before the fix where feasible.
- A passing test after the fix.
- Clear command to run tests.

Acceptance criteria:

- Test commands are documented.
- Test results are summarized in `reports/fix_verification_report.md`.
- If full automated tests are impossible, a justified manual reproduction protocol must be documented.

### FR-10: Token Efficiency Comparison

The project shall compare naive and graph-guided workflows.

Required metrics:

- Estimated or measured tokens consumed.
- Number of files or text units read.
- Number of investigation iterations.
- Time or step count to reach root cause.
- Quality of root-cause explanation.

Comparison modes:

- Baseline naive mode: broad raw-file reading.
- Graph-guided mode: Graphify + `index.md` + `hot.md` + focused source reads.

Acceptance criteria:

- Results exist in `reports/token_efficiency_report.md`.
- The report includes a comparison table.
- The report explains measurement method and limitations.

### FR-11: Original Extension

The project shall include at least one original extension beyond the minimum requirements.

Allowed examples:

- Suspicious-node ranking by centrality or proximity to failing tests.
- Dynamic `hot.md` generation from `graph.json` and `git diff`.
- Orphan-component detection.
- Mixed-responsibility detection.
- Before/after graph comparison.
- Impact report for selected class/function changes.

Recommended extension:

Dynamic `hot.md` generator plus suspicious-node ranking.

Acceptance criteria:

- Extension is implemented or documented with a reproducible script/process.
- Extension has its own section in README.
- Extension output is included under `artifacts/` or `reports/`.

### FR-12: README

The final `README.md` shall be a complete external-reader guide.

Required sections:

- Repository choice and justification.
- Bug/problem selected.
- Research questions.
- Architecture overview.
- Agent workflow.
- Graphify and Obsidian usage.
- Reverse-engineering process.
- Bug root cause and fix.
- Before/after comparison.
- Token-efficiency comparison.
- Original extensions.
- Setup and run instructions.
- Test instructions.
- Artifact index.

Acceptance criteria:

- README is clear enough for a grader to navigate without asking the team.
- README links to all major artifacts.
- README includes visual diagrams or links to them.

## 7. Non-Functional Requirements

### NFR-1: Documentation Quality

Documentation must be structured, specific, and evidence-based.

### NFR-2: Traceability

Every major conclusion should trace to at least one of:

- Graph artifact.
- Obsidian note.
- Source file.
- Test result.
- Agent investigation log.

### NFR-3: Token Discipline

The project must avoid large, unfocused LLM calls. It must demonstrate controlled context selection.

### NFR-4: Reproducibility

A grader should be able to reproduce:

- Environment setup.
- Graph generation or inspect generated graph artifacts.
- Agent workflow run or inspect captured logs.
- Bug reproduction.
- Fix verification.

### NFR-5: Maintainability

Project code should follow professional standards:

- Clear module structure.
- Meaningful names.
- Small files where practical.
- Tests for changed behavior.
- No hardcoded secrets.
- Config files where appropriate.

### NFR-6: Tooling

The project should prefer:

- `uv` for package and command management.
- `pyproject.toml` as dependency source.
- `ruff` for linting where feasible.
- `pytest` for tests where feasible.

## 8. Research Questions

The final documentation must explicitly answer:

1. What is the actual architecture of the selected project?
2. What was not obvious from first reading the files?
3. Which modules, classes, or functions are most central?
4. Where are complexity centers, mixed responsibilities, or God nodes?
5. How can architectural blocks and OOP structure be extracted from incomplete documentation?
6. How was the bug identified?
7. What was the root cause?
8. Which investigation steps led to the root cause?
9. What advantage did Graphify provide compared with linear file reading?
10. What advantage did Obsidian provide as a navigation layer?
11. How did the AI agent save tokens or avoid unnecessary code reads?
12. What future improvements or agent mechanisms would be useful?

## 9. Data and Artifact Requirements

### 9.1 Required Directories

```text
README.md
pyproject.toml
src/
tests/
obsidian/
reports/
artifacts/
data/
```

### 9.2 Reports

Required reports:

- `reports/reverse_engineering_report.md`
- `reports/agent_workflow_report.md`
- `reports/bug_analysis_report.md`
- `reports/fix_verification_report.md`
- `reports/token_efficiency_report.md`
- `reports/original_extension_report.md`

### 9.3 Artifacts

Required artifact groups:

- `artifacts/graphify/`
- `artifacts/diagrams/`
- `artifacts/screenshots/`
- `artifacts/logs/`
- `artifacts/token_measurements/`

## 10. Success Metrics

### 10.1 Functional Success

- Bug is reproduced.
- Root cause is documented.
- Fix is implemented.
- Verification passes.
- Graphify and Obsidian artifacts exist and are used.
- Agent workflow exists and is explained.

### 10.2 Efficiency Success

Graph-guided mode should show improvement over naive mode in at least two of:

- Fewer tokens.
- Fewer files read.
- Fewer iterations.
- Faster root-cause localization.
- Cleaner explanation.

### 10.3 Documentation Success

- README can guide a grader through the work.
- Diagrams explain the architecture.
- Reports provide evidence rather than vague claims.
- Obsidian vault is navigable.

## 11. Phased Delivery Plan

### Phase 0: Setup and Repository Choice

Goals:

- Choose repository.
- Define selected bug.
- Create base project structure.
- Confirm tooling.

Exit criteria:

- Repository choice documented.
- Bug candidate selected.
- Initial README skeleton exists.
- `docs/PRD.md`, `docs/PLAN.md`, and `docs/TODO.md` exist.

### Phase 1: Graph and Knowledge Base

Goals:

- Run Graphify.
- Generate graph artifacts.
- Build Obsidian vault.

Exit criteria:

- `graph.json` exists.
- `GRAPH_REPORT.md` exists.
- `obsidian/index.md` and `obsidian/hot.md` exist.
- Initial architecture observations are documented.

### Phase 2: Reverse Engineering

Goals:

- Identify architecture.
- Identify central components.
- Produce block and OOP diagrams.

Exit criteria:

- Architecture diagram complete.
- OOP or module diagram complete.
- Reverse-engineering report complete.

### Phase 3: Agent Workflow

Goals:

- Implement graph-guided agent.
- Log investigation process.
- Ensure agent consults graph/Obsidian first.

Exit criteria:

- Agent code exists.
- Agent workflow report exists.
- Agent logs show graph-guided context narrowing.

### Phase 4: Bug Investigation and Fix

Goals:

- Reproduce bug.
- Identify root cause.
- Implement fix.
- Verify fix.

Exit criteria:

- Bug analysis report complete.
- Code fix complete.
- Test or reproduction passes.
- Before/after evidence documented.

### Phase 5: Token Efficiency Study

Goals:

- Run or simulate naive baseline.
- Run graph-guided workflow.
- Compare metrics.

Exit criteria:

- Token-efficiency report complete.
- Comparison table complete.
- Measurement method explained.

### Phase 6: Original Extension

Goals:

- Implement one extension beyond assignment minimum.

Recommended:

- Suspicious-node ranking plus generated `hot.md`.

Exit criteria:

- Extension output exists.
- Extension report complete.
- README explains extension value.

### Phase 7: Final Packaging

Goals:

- Polish README.
- Verify links and artifacts.
- Run tests/lint where possible.
- Prepare final repository.

Exit criteria:

- README complete.
- Required deliverables present.
- Test commands documented.
- Final checklist complete.

## 12. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---:|---|
| Selected repository too large | High | Choose one small/medium bug and limit scope |
| BugsInPy setup is difficult | High | Use `broken-python` or `buggy-python` if environment blocks progress |
| Graphify output incomplete | Medium | Document limitations and supplement with manual graph notes |
| Agent becomes too complex | Medium | Use a small LangGraph workflow with clear stages |
| Token counts are hard to measure exactly | Medium | Use transparent estimation and count file/text units as secondary metrics |
| OOP diagram not applicable | Low | Provide module/function interaction diagram and explain why |

## 13. Final Acceptance Checklist

- [ ] Repository selected and justified.
- [ ] Bug selected and reproduced.
- [ ] Graphify artifacts generated.
- [ ] Obsidian vault created with `index.md` and `hot.md`.
- [ ] Architecture block diagram created.
- [ ] OOP or module diagram created.
- [ ] Agent workflow implemented.
- [ ] Agent workflow documented.
- [ ] Bug analysis report completed.
- [ ] Root cause verified.
- [ ] Code fix implemented.
- [ ] Tests or reproduction checks pass.
- [ ] Token-efficiency comparison completed.
- [ ] Original extension completed.
- [ ] README completed.
- [ ] Final artifact links verified.

