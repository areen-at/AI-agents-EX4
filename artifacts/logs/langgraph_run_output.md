# LangGraph Run Output

Status: passed.

## Install Command

```bash
python -m pip install langgraph networkx pydantic python-dotenv
```

Result: dependencies installed successfully in the user Python environment.

## Run Command

```bash
python -m src.agent.run_agent --engine langgraph --json
```

## Key Output

```json
{
  "status": "langgraph_executed",
  "engine_used": "langgraph",
  "selected_files": [
    "mathsquiz/mathsquiz-step2.py",
    "mathsquiz/mathsquiz-step3.py"
  ],
  "suspect_nodes_count": 7,
  "evidence_count": 2,
  "total_estimated_input_tokens": 15775,
  "proposed_fix": "Replace reads of global score inside print_final_scores with final_score; in step3 compute percentage from final_score / max_possible_score."
}
```

## Observed Behavior

- The workflow executed through the LangGraph engine.
- The state ended with `status: langgraph_executed`.
- The CLI output included `engine_used: langgraph`.
- The workflow selected the same seven graph-supported `print_final_scores` suspect nodes.
- The workflow wrote `artifacts/logs/graph_guided_agent_log.md`.

## Full Output Summary

The full JSON output included:

- Bug summary: `print_final_scores accepts final_score but reads global score.`
- Graph artifacts:
  - `artifacts/graphify/GRAPH_REPORT.md`
  - `artifacts/graphify/graph.json`
  - `artifacts/source_evidence/print_final_scores_source.md`
- Obsidian context:
  - `obsidian/index.md`
  - `obsidian/hot.md`
- Top suspect nodes:
  - `call:print_final_scores`
  - `function:mathsquiz/mathsquiz-step2.py:print_final_scores`
  - `function:mathsquiz/mathsquiz-step3.py:print_final_scores`
  - `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:global_score_instead_of_param`
  - `risk:mathsquiz/mathsquiz-step2.py:print_final_scores:unused_arg:final_score`
  - `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:global_score_instead_of_param`
  - `risk:mathsquiz/mathsquiz-step3.py:print_final_scores:unused_arg:final_score`
