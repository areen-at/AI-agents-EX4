# Rubric-Mapped Final Submission Checklist

Status: ready for submission.

## Purpose

This checklist maps the EX04 assignment rubric to concrete repository evidence. Each row names the requirement, the evidence file or folder, and the current status.

## Rubric Checklist

| # | Requirement | Evidence File | Status |
|---:|---|---|---|
| 1 | Submit a complete GitHub repository | `https://github.com/areen-at/AI-agents-EX4`, `README.md` | Complete |
| 2 | Use a Python codebase as the target | `reports/repository_size_report.md` | Complete |
| 3 | Explain selected repository and why it fits the assignment | `README.md`, `reports/repository_size_report.md` | Complete |
| 4 | Document lecturer-approved exception for small repository size | `README.md`, `reports/repository_size_report.md`, `reports/final_submission_report.md` | Complete, with caveat |
| 5 | Select one focused bug or investigation path | `README.md`, `obsidian/print_final_scores_global_state_bug.md`, `reports/bug_analysis_report.md` | Complete |
| 6 | Build graph representation of the codebase | `artifacts/graphify/graph.json`, `artifacts/graphify/GRAPH_REPORT.md`, `artifacts/graphify/graph_metrics.json` | Complete as Graphify-style output |
| 7 | Attempt/local Graphify run and document output | `reports/graphify_local_run_report.md`, `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md` | Complete, with tool-availability caveat |
| 8 | Provide graph visualization or equivalent graph artifact | `artifacts/graphify/graph.html`, `artifacts/diagrams/mathsquiz_graphify_architecture_graph.md` | Complete |
| 9 | Build Obsidian vault as active knowledge space | `obsidian/index.md`, `obsidian/hot.md`, `obsidian/components.md`, `obsidian/architecture.md` | Complete |
| 10 | Include `index.md` central navigation note | `obsidian/index.md` | Complete |
| 11 | Include `hot.md` focused bug-context note | `obsidian/hot.md`, `obsidian/hot.generated.md` | Complete |
| 12 | Add Markdown notes for components, suspects, findings, tests, and fix | `obsidian/components.md`, `obsidian/bug_investigation.md`, `obsidian/tests_and_verification.md` | Complete |
| 13 | Reverse engineer unfamiliar codebase | `reports/reverse_engineering_report.md`, `obsidian/architecture.md` | Complete |
| 14 | Provide architecture block diagram | `artifacts/diagrams/architecture_block_diagram.md` | Complete |
| 15 | Provide OOP diagram or justified module/function equivalent | `artifacts/diagrams/oop_diagram.md`, `reports/phase2_architecture_review.md` | Complete |
| 16 | Identify central modules/functions/components | `reports/reverse_engineering_report.md`, `obsidian/components.md`, `reports/suspicious_nodes.md` | Complete |
| 17 | Identify complexity centers or God-node-like risks | `reports/reverse_engineering_report.md`, `artifacts/graphify/GRAPH_REPORT.md` | Complete |
| 18 | Build an AI agent workflow with graph-first behavior | `src/agent/`, `reports/agent_workflow_report.md`, `artifacts/diagrams/agent_workflow_diagram.md` | Complete |
| 19 | Include CrewAI or LangGraph implementation path | `src/agent/langgraph_workflow.py`, `src/agent/run_agent.py`, `artifacts/logs/langgraph_run_output.md`, `pyproject.toml` | Complete, LangGraph executed locally |
| 20 | Agent reads Graphify/Obsidian before source code | `src/agent/workflow.py`, `artifacts/logs/graph_guided_agent_log.md`, `tests/unit/test_agent_workflow.py` | Complete |
| 21 | Explain agent workflow stages | `reports/agent_workflow_report.md`, `artifacts/diagrams/agent_workflow_diagram.md`, `README.md` | Complete |
| 22 | Reproduce or demonstrate selected bug | `artifacts/logs/phase1_print_final_scores_probe.md`, `tests/reproduction/print_final_scores_probe.py` | Complete |
| 23 | Explain bug, root cause, and investigation path | `reports/bug_analysis_report.md`, `obsidian/bug_investigation.md`, `README.md` | Complete |
| 24 | Implement real code fix | `src/target_project/mathsquiz/mathsquiz_step2.py`, `src/target_project/mathsquiz/mathsquiz_step3.py` | Complete |
| 25 | Explain why the fix is correct | `reports/fix_verification_report.md`, `artifacts/before_after/fix.diff` | Complete |
| 26 | Provide before/after proof | `artifacts/before_after/before.md`, `artifacts/before_after/after.md`, `artifacts/before_after/fix.diff` | Complete |
| 27 | Verify fix with tests/checks | `tests/unit/test_print_final_scores_fix.py`, `artifacts/logs/test_after_fix.md`, `artifacts/logs/phase7_verification.md` | Complete |
| 28 | Compare naive vs graph-guided workflows | `reports/token_efficiency_report.md`, `artifacts/token_measurements/token_comparison.csv` | Complete |
| 29 | Include token count or estimate | `reports/token_efficiency_report.md`, `artifacts/token_measurements/token_comparison.csv` | Complete |
| 30 | Include file/text-unit read counts | `reports/token_efficiency_report.md`, `artifacts/logs/naive_baseline_log.md`, `artifacts/logs/graph_guided_agent_log.md` | Complete |
| 31 | Include investigation iterations | `reports/token_efficiency_report.md` | Complete |
| 32 | Include quality/speed to root cause and fix | `reports/token_efficiency_report.md`, `reports/phase5_review.md` | Complete |
| 33 | Add at least one original extension beyond minimum | `src/analysis/`, `reports/original_extension_report.md`, `reports/suspicious_nodes.md` | Complete |
| 34 | Extension ranks suspicious nodes or dynamically generates hot context | `src/analysis/suspicious_nodes.py`, `src/analysis/hot_md_generator.py`, `obsidian/hot.generated.md` | Complete |
| 35 | README covers repo, bug, questions, architecture, agent, Graphify, Obsidian, fix, token efficiency, extension, and run commands | `README.md` | Complete |
| 36 | Include visual elements such as diagrams/graphs | `artifacts/diagrams/`, `artifacts/graphify/graph.html` | Complete |
| 37 | Recommended repository structure is clear | `README.md`, root folders `src/`, `tests/`, `obsidian/`, `reports/`, `artifacts/` | Complete |
| 38 | Include tests | `tests/unit/`, `tests/reproduction/` | Complete |
| 39 | Include dependency file | `pyproject.toml`, `.env-example` | Complete |
| 40 | Document tooling limitations honestly | `reports/final_submission_report.md`, `reports/graphify_local_run_report.md`, `artifacts/logs/phase7_verification.md` | Complete |
| 41 | Final packaging and checklist | `reports/final_submission_report.md`, `reports/final_submission_checklist.md`, `reports/phase7_review.md` | Complete |

## Completeness Estimate

Estimated overall completeness: **95%**.

The core investigation, fix, tests, Obsidian vault, diagrams, token comparison, original extension, and LangGraph workflow execution are complete. The remaining gap is mainly external-tool uncertainty around the official Graphify executable.

## Remaining Risks Before Submission

| Risk | Severity | Explanation | Mitigation |
|---|---|---|---|
| Official Graphify executable was not available locally | Medium | The project includes Graphify-style artifacts, but not output from a verified official Graphify binary. | `reports/graphify_local_run_report.md` documents install attempts and generated architecture graph. Ask lecturer for exact Graphify install command if strict official output is required. |
| LangGraph workflow dependency setup | Low | LangGraph now runs locally, but dependency installation is still required on a fresh machine. | README documents the install/run command and `artifacts/logs/langgraph_run_output.md` captures a successful local run. |
| Repository is smaller than the general 10,000 LOC / 70 files guideline | Low to Medium | The selected repo has 5 Python files and 260 meaningful lines. | Lecturer-approved exception is documented in `README.md`, `reports/repository_size_report.md`, and `reports/final_submission_report.md`. |
| Token counts are estimated | Low | Token counts use `characters / 4`, not API logs. | Method and limitations are explicit in `reports/token_efficiency_report.md`. |
| Ruff and `uv.lock` unavailable locally | Low | Ruff was configured but not installed; `uv.lock` is absent. | Standard-library verification commands passed and limitations are documented. |

## Final Recommendation

The project is ready to submit. If there is time for one extra safety step, ask the lecturer or teaching staff for the exact Graphify executable/package URL and run it against `work/target_repos/broken-python/mathsquiz`. Otherwise, submit with the documented Graphify-style artifacts and local-run report.
