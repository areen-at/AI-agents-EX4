# EX04 Implementation Plan

## 1. Strategy

This plan converts the EX04 requirements into a phased engineering workflow. The project should stay intentionally focused: one unfamiliar Python codebase, one well-explained bug, one graph-guided investigation, one verified fix, and one original extension.

The strongest submission is not the largest one. The strongest submission is the one that proves, with evidence, that graph-guided context selection helped us understand and fix unfamiliar code more efficiently than naive reading.

## 2. Recommended Technical Direction

### 2.1 Repository Choice

Recommended first choice:

`martinpeck/broken-python`

Reason:

- Smaller and easier to control.
- Good for demonstrating debugging without losing time on environment setup.
- Better fit if the goal is a polished, complete EX04 submission.

Recommended second choice:

`andela/buggy-python`

Reason:

- Also simple enough for a focused bug investigation.
- Useful if `broken-python` does not provide enough structure for diagrams.

Use `soarsmu/BugsInPy` only if:

- The team wants a more realistic challenge.
- The environment setup is manageable.
- A single bug can be isolated quickly.

### 2.2 Agent Framework

Recommended:

LangGraph

Reason:

- Easier to control stages.
- Better for limited free accounts.
- Makes the workflow explainable as a graph of steps.
- Fits the assignment theme of graph-guided reasoning.

### 2.3 Original Extension

Recommended extension:

Suspicious-node ranking and dynamic `hot.md` generation.

Inputs:

- `graph.json`
- Failing test name or bug-related keyword
- Optional `git diff`

Outputs:

- `reports/suspicious_nodes.md`
- Updated `obsidian/hot.md`

Why this extension is strong:

- It directly supports token efficiency.
- It shows initiative beyond manual documentation.
- It connects Graphify output to agent context selection.

## 3. Target Repository Structure

```text
README.md
pyproject.toml
uv.lock
.gitignore
.env-example

src/
  agent/
    __init__.py
    workflow.py
    state.py
    tools.py
  analysis/
    __init__.py
    graph_loader.py
    suspicious_nodes.py
    hot_md_generator.py
  target_project/
    ...

tests/
  unit/
  integration/

obsidian/
  index.md
  hot.md
  architecture.md
  bug_investigation.md
  components.md
  tests_and_verification.md
  token_efficiency.md

reports/
  reverse_engineering_report.md
  agent_workflow_report.md
  bug_analysis_report.md
  fix_verification_report.md
  token_efficiency_report.md
  original_extension_report.md

artifacts/
  graphify/
    graph.json
    GRAPH_REPORT.md
  diagrams/
    architecture_block_diagram.md
    oop_diagram.md
  logs/
    naive_baseline_log.md
    graph_guided_agent_log.md
  token_measurements/
    token_comparison.csv
  screenshots/

data/
```

If the target repository already has its own structure, keep its code intact and place EX04 artifacts around it in clearly named folders.

## 4. Phase 0 - Project Setup and Repository Selection

### 4.1 Goals

- Select the base repository.
- Select one bug candidate.
- Create the EX04 submission skeleton.
- Define initial research questions.

### 4.2 Tasks

1. Review candidate repositories.
2. Choose one repository and document the reason.
3. Clone or copy the target project.
4. Identify one candidate bug.
5. Create repository structure.
6. Create initial README skeleton.
7. Create project tracking docs:
   - `docs/PRD.md`
   - `docs/PLAN.md`
   - `docs/TODO.md`

### 4.3 Outputs

- Repository choice section in README.
- Initial TODO list.
- Initial bug candidate note.

### 4.4 Exit Criteria

- Team can explain why the repository was selected.
- Team has a specific bug candidate.
- Project structure exists.

## 5. Phase 1 - Graphify and Initial Knowledge Base

### 5.1 Goals

- Convert codebase into graph artifacts.
- Create the initial Obsidian navigation layer.
- Establish graph-guided reading paths before using the AI agent.

### 5.2 Tasks

1. Run Graphify on the selected codebase.
2. Save Graphify outputs under `artifacts/graphify/`.
3. Inspect:
   - `graph.json`
   - `GRAPH_REPORT.md`
   - visual graph output if available
4. Create `obsidian/index.md`.
5. Create initial `obsidian/hot.md`.
6. Create initial component notes.
7. Link Graphify findings to Obsidian pages.

### 5.3 `index.md` Required Content

- Project name and source repository.
- Short description of system purpose.
- Main components.
- Navigation links:
  - Architecture
  - Bug investigation
  - Hot context
  - Token efficiency
  - Reports
- Initial central nodes from Graphify.

### 5.4 `hot.md` Required Content

- Bug focus.
- Suspected modules/files.
- Graph evidence.
- Relevant relationships.
- Next code files to inspect.
- Open questions.

### 5.5 Outputs

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `obsidian/index.md`
- `obsidian/hot.md`
- Initial Obsidian component notes.

### 5.6 Exit Criteria

- A reader can start at `index.md` and understand where to investigate.
- `hot.md` narrows the bug context to a small set of files/components.

## 6. Phase 2 - Reverse Engineering

### 6.1 Goals

- Understand the actual architecture.
- Extract engineering insights from the graph and source code.
- Produce required diagrams.

### 6.2 Tasks

1. Identify main entry points.
2. Identify major modules and responsibilities.
3. Identify central nodes.
4. Identify possible God nodes or bottlenecks.
5. Identify isolated or suspicious components.
6. Compare graph findings with source files.
7. Build architecture block diagram.
8. Build OOP or module interaction diagram.
9. Write reverse-engineering report.

### 6.3 Architecture Diagram Requirements

Must show:

- Entry point.
- Core modules.
- Data/control flow.
- Bug-critical path.
- External dependencies if any.

Recommended format:

- Mermaid diagram in `artifacts/diagrams/architecture_block_diagram.md`.

### 6.4 OOP Diagram Requirements

If classes exist:

- Show classes.
- Show inheritance/composition.
- Show important method calls.

If no meaningful OOP exists:

- Create a module/function interaction diagram.
- Explain why an OOP diagram is not applicable.

### 6.5 Outputs

- `reports/reverse_engineering_report.md`
- `artifacts/diagrams/architecture_block_diagram.md`
- `artifacts/diagrams/oop_diagram.md`
- Updated Obsidian notes.

### 6.6 Exit Criteria

- The team can answer the assignment research questions about architecture.
- Diagrams reflect code behavior, not just folders.

## 7. Phase 3 - Agent Workflow Design and Implementation

### 7.1 Goals

- Build a graph-guided AI workflow.
- Make the workflow explainable and measurable.
- Prevent the agent from reading the whole codebase naively.

### 7.2 Recommended LangGraph Nodes

1. `LoadGraphContext`
   - Reads `graph.json`, `GRAPH_REPORT.md`, `index.md`, and `hot.md`.

2. `SelectSuspects`
   - Produces a ranked list of likely relevant files/components.

3. `ReadFocusedCode`
   - Reads only selected source files or snippets.

4. `HypothesizeRootCause`
   - Generates root-cause hypotheses with evidence.

5. `PlanFix`
   - Suggests minimal code fix and required tests.

6. `VerifyFix`
   - Runs or records test/reproduction verification.

7. `WriteInvestigationLog`
   - Saves findings to reports and Obsidian.

### 7.3 Agent State

Recommended fields:

```python
class InvestigationState(TypedDict):
    bug_summary: str
    graph_artifacts: dict
    obsidian_context: dict
    suspect_nodes: list[dict]
    selected_files: list[str]
    evidence: list[dict]
    hypotheses: list[dict]
    proposed_fix: str
    verification_result: str
    token_estimate: dict
```

### 7.4 Context Rules

The agent must:

- Read `index.md` before raw source.
- Read `hot.md` before raw source.
- Use graph artifacts to select files.
- Avoid reading all files.
- Log every file/text unit it reads.
- Record token estimate or text length.

### 7.5 Outputs

- `src/agent/workflow.py`
- `src/agent/state.py`
- `src/agent/tools.py`
- `reports/agent_workflow_report.md`
- `artifacts/logs/graph_guided_agent_log.md`

### 7.6 Exit Criteria

- Agent workflow can be explained step by step.
- Logs prove graph-first behavior.
- The workflow narrows context before reading source code.

## 8. Phase 4 - Bug Reproduction, Root Cause, and Fix

### 8.1 Goals

- Reproduce the selected bug.
- Identify root cause.
- Fix the bug.
- Verify the fix.

### 8.2 Tasks

1. Define bug reproduction command or input.
2. Capture failing behavior.
3. Use graph-guided workflow to identify suspect files.
4. Inspect source evidence.
5. Write root-cause explanation.
6. Implement minimal fix.
7. Add or update test.
8. Run verification.
9. Update Obsidian `hot.md`.
10. Write bug analysis and fix verification reports.

### 8.3 Root Cause Report Template

```text
Bug:
Expected behavior:
Actual behavior:
Reproduction steps:
Initial suspects:
Graph evidence:
Source evidence:
Root cause:
Fix:
Verification:
Remaining risks:
```

### 8.4 Outputs

- Code fix.
- Test or reproduction script.
- `reports/bug_analysis_report.md`
- `reports/fix_verification_report.md`
- Updated `obsidian/hot.md`
- Updated README.

### 8.5 Exit Criteria

- Bug is clearly explained.
- Fix is verified.
- Before/after behavior is documented.

## 9. Phase 5 - Token Efficiency Measurement

### 9.1 Goals

- Prove the graph-guided workflow was more focused than naive reading.
- Provide transparent metrics, even if token counts are estimated.

### 9.2 Baseline Mode

Naive baseline:

- Read broad file list.
- No graph guidance.
- No Obsidian navigation.
- Track number of files read.
- Estimate tokens from text length.
- Track number of reasoning iterations.

### 9.3 Graph-Guided Mode

Graph-guided mode:

- Read `index.md`.
- Read `hot.md`.
- Read Graphify report.
- Read only selected code files.
- Track same metrics as baseline.

### 9.4 Metrics Table

Required columns:

```text
Mode
Files/text units read
Approx input tokens
Approx output tokens
Iterations
Root-cause reached?
Fix reached?
Notes
```

### 9.5 Token Estimation Method

Acceptable method:

- Count characters in each text unit.
- Estimate tokens as `characters / 4`.
- State clearly that counts are estimates unless API logs provide exact values.

### 9.6 Outputs

- `reports/token_efficiency_report.md`
- `artifacts/token_measurements/token_comparison.csv`
- `artifacts/logs/naive_baseline_log.md`
- `artifacts/logs/graph_guided_agent_log.md`

### 9.7 Exit Criteria

- Report explains method.
- Comparison table is present.
- Results show concrete benefit or honestly explain limitations.

## 10. Phase 6 - Original Extension

### 10.1 Recommended Extension: Suspicious Node Ranking

Build a script that ranks nodes from `graph.json` using:

- Centrality or degree.
- Proximity to bug keywords.
- Proximity to failing test names.
- Relation labels such as calls/imports/implements if available.

### 10.2 Recommended Extension: Dynamic `hot.md`

Generate or update `hot.md` from:

- Top suspicious nodes.
- Bug keyword.
- Relevant source files.
- Graph links.
- `git diff` after the fix, if available.

### 10.3 Tasks

1. Implement graph parser.
2. Implement ranking logic.
3. Generate `reports/suspicious_nodes.md`.
4. Generate or update `obsidian/hot.md`.
5. Document method and limitations.

### 10.4 Outputs

- `src/analysis/graph_loader.py`
- `src/analysis/suspicious_nodes.py`
- `src/analysis/hot_md_generator.py`
- `reports/original_extension_report.md`
- `reports/suspicious_nodes.md`

### 10.5 Exit Criteria

- Extension produces a useful artifact.
- README explains why it improves the workflow.
- Extension connects directly to token efficiency or graph-guided debugging.

## 11. Phase 7 - Final Packaging and Submission

### 11.1 Goals

- Make the repository easy to grade.
- Ensure every required artifact is linked.
- Verify commands and documentation.

### 11.2 Tasks

1. Finalize README.
2. Add artifact index.
3. Check all links.
4. Run tests.
5. Run lint if configured.
6. Verify no secrets are committed.
7. Verify diagrams render.
8. Verify Obsidian links.
9. Add final limitations section.
10. Add final conclusion.

### 11.3 README Final Structure

```text
# EX04 - Graph-Guided Reverse Engineering

## Repository Choice
## Selected Bug
## Research Questions
## Quick Start
## Project Structure
## Graphify Artifacts
## Obsidian Vault
## Architecture Understanding
## Agent Workflow
## Bug Investigation
## Root Cause and Fix
## Verification
## Token Efficiency Comparison
## Original Extension
## Artifact Index
## Limitations
## Conclusion
```

### 11.4 Final Deliverable Checklist

- [ ] `README.md`
- [ ] `pyproject.toml` or justified dependency file
- [ ] `src/`
- [ ] `tests/`
- [ ] `obsidian/index.md`
- [ ] `obsidian/hot.md`
- [ ] Graphify outputs
- [ ] Architecture block diagram
- [ ] OOP/module diagram
- [ ] Agent workflow code
- [ ] Bug analysis report
- [ ] Fix verification report
- [ ] Token efficiency report
- [ ] Original extension report
- [ ] Before/after evidence
- [ ] Screenshots or visual artifacts where useful

## 12. Work Breakdown by Role

If working in pairs, split responsibilities as follows.

### Partner A - Code and Agent Lead

- Repository setup.
- Bug reproduction.
- Agent workflow implementation.
- Code fix.
- Tests.

### Partner B - Graph and Documentation Lead

- Graphify outputs.
- Obsidian vault.
- Architecture and OOP diagrams.
- Reports.
- Token-efficiency comparison.

Both partners should review:

- Root-cause explanation.
- Final README.
- Final artifact links.

## 13. Suggested Timeline

### Day 1

- Select repository.
- Pick bug.
- Create structure.
- Run Graphify.
- Build initial Obsidian vault.

### Day 2

- Reverse-engineer architecture.
- Create diagrams.
- Build first version of agent workflow.

### Day 3

- Reproduce bug.
- Run graph-guided investigation.
- Identify root cause.
- Implement fix and tests.

### Day 4

- Run token-efficiency comparison.
- Implement original extension.
- Update `hot.md` dynamically or manually with extension output.

### Day 5

- Polish reports.
- Finalize README.
- Verify tests, links, and deliverables.

## 14. Quality Gates

### Gate 1 - Scope Gate

Pass when:

- One bug is selected.
- Repository is not too large.
- Team can reproduce or describe the bug.

### Gate 2 - Graph Gate

Pass when:

- `graph.json` and report exist.
- `index.md` and `hot.md` exist.
- Initial suspects are graph-supported.

### Gate 3 - Investigation Gate

Pass when:

- Architecture is understood.
- Diagrams are drafted.
- Agent workflow reads graph/Obsidian before raw code.

### Gate 4 - Fix Gate

Pass when:

- Root cause is verified.
- Fix is implemented.
- Test or reproduction passes.

### Gate 5 - Submission Gate

Pass when:

- README links every required artifact.
- Reports are complete.
- Token-efficiency comparison is complete.
- Original extension is complete.

## 15. Measurement Plan

### 15.1 File/Text Unit Count

For each workflow mode, record every text unit read:

- Source file.
- Graph report.
- Obsidian note.
- Test file.
- Error trace.

### 15.2 Token Estimate

Use:

```text
estimated_tokens = character_count / 4
```

Record:

- Input token estimate.
- Output token estimate if available.
- Total estimate.

### 15.3 Iteration Count

Count an iteration as one investigation cycle:

1. Read context.
2. Form hypothesis.
3. Inspect evidence.
4. Update hypothesis.

### 15.4 Quality Rating

Rate each mode on:

- Root-cause correctness.
- Evidence quality.
- Fix readiness.
- Explanation clarity.

Use a simple 1-5 scale and explain the rating.

## 16. Risk Management

| Risk | Probability | Impact | Response |
|---|---:|---:|---|
| Graphify cannot parse selected repo | Medium | High | Keep generated artifacts, document limitation, supplement manually |
| Bug cannot be reproduced | Medium | High | Switch to smaller known buggy repo early |
| Agent workflow is too complex | Medium | Medium | Use fixed LangGraph stages and simple tools |
| Token comparison is imprecise | High | Medium | Use transparent estimates plus file-count metrics |
| Diagrams take too long | Medium | Medium | Use Mermaid diagrams first, polish later |
| Environment setup consumes time | Medium | High | Avoid large repos unless setup works quickly |

## 17. Definition of Done

The project is complete when:

- A grader can clone/open the repository and understand the chosen bug.
- Graphify artifacts and Obsidian vault guide the investigation.
- The agent workflow is implemented and documented.
- The bug is fixed and verified.
- Token efficiency is measured.
- At least one original extension is included.
- README provides a complete guided tour through all artifacts.

