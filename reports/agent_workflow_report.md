# Agent Workflow Report

Status: Phase 3 complete.

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
- `src/agent/langgraph_workflow.py`
- `src/agent/prompts.py`
- `src/agent/run_agent.py`

## Framework Choice

Recommended framework: LangGraph.

Implementation status:

- The core workflow is deterministic and fully testable with standard Python.
- `src/agent/langgraph_workflow.py` wraps the same state contract as a real LangGraph `StateGraph`.
- `python -m src.agent.run_agent --engine auto` uses LangGraph when installed and falls back to the deterministic engine otherwise.
- The final local verification installed LangGraph and successfully ran `python -m src.agent.run_agent --engine langgraph --json`.

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

## Run Command

```bash
python -m src.agent.run_agent
```

For JSON output:

```bash
python -m src.agent.run_agent --json
```

Force LangGraph when dependencies are installed:

```bash
python -m src.agent.run_agent --engine langgraph --json
```

## Execution Result

The graph-guided workflow executed successfully with LangGraph and wrote:

- `artifacts/logs/graph_guided_agent_log.md`
- `artifacts/logs/phase3_verification.md`
- `artifacts/logs/langgraph_run_output.md`

Selected suspects: 7.

Status: `langgraph_executed`.

Engine: `langgraph`.

## Token Estimate

The workflow records character counts and estimated input tokens for each text unit it reads.

Current run:

- `obsidian/index.md`: 1009 estimated tokens.
- `obsidian/hot.md`: 1204 estimated tokens.
- `artifacts/graphify/GRAPH_REPORT.md`: 1157 estimated tokens.
- `artifacts/graphify/graph.json`: 11896 estimated tokens.
- `artifacts/source_evidence/print_final_scores_source.md`: 509 estimated tokens.
- Total estimated input tokens: 15775.

## Limitations

- LangGraph now runs locally after installing dependencies with `python -m pip install langgraph networkx pydantic python-dotenv`.
- This workflow does not call a live LLM; the assignment focus is graph-guided context selection, investigation, and fix evidence.
- `pytest` is declared in the dev dependency group, but was not available in the current local Python environment during verification.

## Future Improvements

- Add a source-snippet reader that records exact source-line evidence during Phase 4.
- Connect Phase 5 token-efficiency comparison directly to `text_units_read`.
