# Agent Instruction Architecture PRD

## 1. Purpose

This document defines how AI agents must be instructed before they generate, analyze, or modify code for EX04.

The assignment emphasizes that a major part of the work is knowing how to define precise instructions for agents, especially instructions that preserve modular architecture while creating or modifying code.

## 2. Core Principle

Agents must not behave like free-form chatbots reading the entire repository.

Agents must behave like constrained engineering workers:

- They receive a clear role.
- They receive bounded inputs.
- They produce bounded outputs.
- They use Graphify and Obsidian before raw source reading.
- They preserve module boundaries.
- They justify conclusions with evidence.
- They document rejected hypotheses.
- They verify fixes before accepting them.

## 2.1 Active Investigation Target

Official bug path: `print_final_scores` global-state coupling in the `mathsquiz` subsystem.

Primary source files:

- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

The agent workflow must treat this as the locked bug target unless a human explicitly changes the target. Agents should use `mathsquiz.py` baseline syntax/logic issues and `ask_question(...)` input-conversion risks only as background or rejected hypotheses.

The modularity rule for the fix is explicit: `print_final_scores(...)` must use its function parameters, not hidden global `score` state.

## 3. Required Agent Roles

### 3.1 Graph Navigator Agent

Responsibilities:

- Read `graph.json`.
- Read `GRAPH_REPORT.md`.
- Identify central nodes.
- Identify bug-proximal nodes.
- Identify possible bottlenecks or God nodes.
- Recommend a small set of source files for inspection.

Must not:

- Read the entire repository.
- Propose code changes.
- Treat graph layout position as evidence.

### 3.2 Obsidian Context Agent

Responsibilities:

- Read `obsidian/index.md`.
- Read `obsidian/hot.md`.
- Extract the current investigation state.
- Maintain links between notes.
- Update bug-focused context after new evidence.

Must not:

- Replace source-code verification.
- Add unsupported conclusions.

### 3.3 Source Evidence Agent

Responsibilities:

- Inspect only graph-selected source files.
- Verify important graph edges against source.
- Extract relevant snippets.
- Distinguish facts from hypotheses.

Must not:

- Read broad folders without justification.
- Refactor code while investigating.

### 3.4 Root Cause Agent

Responsibilities:

- Combine graph evidence, Obsidian context, source evidence, and test output.
- Produce root-cause hypotheses.
- Rank hypotheses by evidence strength.
- Record rejected hypotheses.

Must not:

- Claim root cause before source/test verification.
- Ignore contradictory evidence.

### 3.5 Fix Planner Agent

Responsibilities:

- Propose a minimal fix.
- Identify affected modules.
- Preserve modular architecture.
- Propose tests.
- Identify risks.

Must not:

- Introduce broad unrelated refactoring.
- Move logic across module boundaries without justification.

### 3.6 Verification Agent

Responsibilities:

- Run or define reproduction checks.
- Run or define regression tests.
- Compare before/after behavior.
- Record verification evidence.

Must not:

- Accept a fix without evidence.

## 4. Modular Architecture Rules

All agents must follow these rules:

- Keep responsibilities separated.
- Prefer small modules with clear interfaces.
- Avoid duplicating logic.
- Avoid placing business logic in CLI, UI, or orchestration layers.
- Preserve existing architectural style unless there is evidence it causes the bug.
- If a refactor is proposed, explain why it is necessary.
- Keep fixes minimal unless the assignment extension explicitly analyzes refactoring.

## 5. Context Rules

Agents must read context in this order:

1. `obsidian/index.md`
2. `obsidian/hot.md`
3. `artifacts/graphify/GRAPH_REPORT.md`
4. `artifacts/graphify/graph.json` or summarized graph output
5. Focused source files selected from graph evidence
6. Tests or reproduction files

Agents may not start by loading the entire codebase into the prompt.

## 6. Evidence Format

Every important conclusion must include:

- Claim
- Evidence source
- Evidence type: graph, Obsidian, source, test, or agent inference
- Confidence level
- Required verification step if not fully verified

## 7. Output Requirements

Agent outputs must be saved or summarized in:

- `reports/agent_workflow_report.md`
- `artifacts/logs/graph_guided_agent_log.md`
- `obsidian/bug_investigation.md`
- `obsidian/hot.md`

## 8. Acceptance Criteria

- The final agent workflow uses these role boundaries.
- Prompts or role definitions reflect this document.
- The bug fix follows modular architecture constraints.
- Agent logs show graph-first and Obsidian-first behavior.
- The final README links this document.
