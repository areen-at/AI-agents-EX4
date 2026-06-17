# Agent Workflow Report

Status: Phase 3 prepared.

## Purpose

The agent workflow must investigate the selected `print_final_scores` global-state bug without reading the whole repository naively.

It must start from:

1. Obsidian navigation context.
2. Graphify-style graph artifacts.
3. Focused source files selected from graph evidence.

## Workflow Diagram

- `artifacts/diagrams/agent_workflow_diagram.md`

## Prepared Code Scaffold

- `src/agent/state.py`
- `src/agent/tools.py`
- `src/agent/workflow.py`

## Framework Choice

Recommended framework: LangGraph.

Current status:

- Phase 3 preparation uses deterministic Python functions first.
- These functions can be wrapped as LangGraph nodes after the graph-first logic is verified.
- This avoids mixing environment setup problems with the architecture investigation.

## Workflow Stages

| Stage | Input | Output |
|---|---|---|
| Load Obsidian context | `obsidian/index.md`, `obsidian/hot.md` | Current bug target and focused context |
| Load graph context | `GRAPH_REPORT.md`, `graph.json` | Graph-supported suspect list |
| Select suspects | Graph nodes and bug keyword | Ranked `print_final_scores` nodes |
| Read focused source | Step2/step3 source files | Source evidence |
| Hypothesize root cause | Graph + Obsidian + source + probe | Root-cause claim |
| Plan fix | Root-cause claim | Minimal modular fix |
| Plan verification | Phase 1 probe | Regression test plan |
| Write log | Full state | `artifacts/logs/graph_guided_agent_log.md` |

## State Schema

The prepared state schema is implemented in `src/agent/state.py`.

Important fields:

- `bug_summary`: selected bug in one sentence.
- `selected_files`: focused source files allowed for raw-code inspection.
- `graph_artifacts`: graph files to read before source.
- `obsidian_context`: vault notes to read before source.
- `suspect_nodes`: graph-selected suspect nodes.
- `evidence`: claims with evidence type, source, confidence, and verification step.
- `text_units_read`: character and token estimates for context tracking.
- `proposed_fix`: minimal modular fix plan.
- `verification_plan`: planned regression check.
- `status`: workflow stage marker.

## Context Discipline

The agent may not begin by reading all source files.

Required order:

1. `obsidian/index.md`
2. `obsidian/hot.md`
3. `artifacts/graphify/GRAPH_REPORT.md`
4. `artifacts/graphify/graph.json`
5. `mathsquiz-step2.py` and `mathsquiz-step3.py`
6. Phase 1 probe output

## Selected Bug Contract

The workflow is locked to:

```text
print_final_scores accepts final_score but reads global score
```

The expected fix contract is:

```text
print_final_scores must use final_score instead of global score
```

## Evidence Format

Every claim must include:

- Claim
- Evidence source
- Evidence type
- Confidence
- Verification step

This matches `docs/PRD_agent_instruction_architecture.md`.

## Graph-Guided System Prompt Draft

```text
You are the EX04 graph-guided debugging agent.
You must investigate only the selected print_final_scores global-state bug.
Read Obsidian index.md and hot.md before source code.
Read GRAPH_REPORT.md and graph.json before source code.
Select only the source files supported by graph evidence.
Every conclusion must include claim, evidence source, evidence type, confidence, and verification step.
Do not fix baseline mathsquiz.py or ask_question input validation unless the human changes the target.
Preserve modular boundaries: print_final_scores must use explicit parameters rather than hidden global score.
```

## Phase 3 Next Implementation Step

Run the scaffold, save its state summary, then wrap the deterministic steps as LangGraph nodes if environment setup allows.

## Preparation Run

The deterministic scaffold was executed successfully and saved in:

- `artifacts/logs/phase3_preparation_run.md`
