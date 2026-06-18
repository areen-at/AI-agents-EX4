# Phase 3 Verification

Status: complete.

## Commands Run

```powershell
python -m src.agent.run_agent --json
python -m src.agent.run_agent
python -m unittest tests.unit.test_agent_workflow
python -m compileall src tests
python -m pytest --version
uv --version
```

## Results

| Command | Result |
|---|---|
| `python -m src.agent.run_agent --json` | Passed; workflow reached `phase3_executed`. |
| `python -m src.agent.run_agent` | Passed; wrote `artifacts/logs/graph_guided_agent_log.md`. |
| `python -m unittest tests.unit.test_agent_workflow` | Passed; 3 tests OK. |
| `python -m compileall src tests` | Passed. |
| `python -m pytest --version` | Failed locally because `pytest` is not installed. |
| `uv --version` | Failed locally because `uv` is not installed. |

## Pytest Installation

`pytest` should be installed for the final submission workflow because it is declared in `pyproject.toml`.

Recommended project-standard commands:

```powershell
python -m pip install uv
uv sync --group dev
uv run pytest
```

Fallback commands:

```powershell
python -m pip install pytest pytest-cov
python -m pytest
```

## Phase 3 Completion Criteria

- Agent workflow has a command-line runner.
- Workflow reads Obsidian and graph artifacts before selecting suspects.
- Workflow avoids broad raw-code reading.
- Workflow logs selected suspects, token estimates, proposed fix, and verification plan.
- Unit tests pass using the standard library test runner.
- Focused source evidence is read after Obsidian and graph artifacts.
