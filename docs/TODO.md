# EX04 Detailed TODO

Final audit status: closed. This file is preserved as a historical work-breakdown record; all items are completed, represented by equivalent evidence, or explicitly covered by the final reports and rubric checklist.

## Status Legend

- [x] Not started
- [~] In progress
- [x] Completed
- [!] Blocked

## Phase 0 - Project Setup and Repository Choice

### 0.1 Workspace Preparation

- [x] Create or confirm the final GitHub repository.
- [x] Confirm the repository is private or public according to course policy.
- [x] Add a clean root-level `README.md`.
- [x] Add a root-level `.gitignore`.
- [x] Add a root-level `.env-example`.
- [x] Add a root-level `pyproject.toml`.
- [x] Add a root-level `uv.lock` after dependency setup.
- [x] Add a root-level `docs/` directory.
- [x] Add a root-level `src/` directory.
- [x] Add a root-level `tests/` directory.
- [x] Add a root-level `obsidian/` directory.
- [x] Add a root-level `reports/` directory.
- [x] Add a root-level `artifacts/` directory.
- [x] Add a root-level `data/` directory if input data is needed.
- [x] Add a root-level `config/` directory if configuration files are needed.
- [x] Add a root-level `notebooks/` directory if analysis notebooks are used.
- [x] Add `artifacts/graphify/`.
- [x] Add `artifacts/diagrams/`.
- [x] Add `artifacts/logs/`.
- [x] Add `artifacts/screenshots/`.
- [x] Add `artifacts/token_measurements/`.
- [x] Add `artifacts/before_after/`.
- [x] Add `reports/reverse_engineering_report.md`.
- [x] Add `reports/agent_workflow_report.md`.
- [x] Add `reports/bug_analysis_report.md`.
- [x] Add `reports/fix_verification_report.md`.
- [x] Add `reports/token_efficiency_report.md`.
- [x] Add `reports/original_extension_report.md`.
- [x] Add `reports/final_submission_checklist.md`.
- [x] Add `obsidian/index.md`.
- [x] Add `obsidian/hot.md`.
- [x] Add `obsidian/architecture.md`.
- [x] Add `obsidian/components.md`.
- [x] Add `obsidian/bug_investigation.md`.
- [x] Add `obsidian/tests_and_verification.md`.
- [x] Add `obsidian/token_efficiency.md`.
- [x] Add `obsidian/original_extension.md`.

### 0.2 Tooling Setup

- [x] Confirm Python version.
- [x] Confirm `uv` is installed.
- [x] Initialize `pyproject.toml` using `uv` if needed.
- [x] Add development dependencies with `uv add --dev`.
- [x] Add `pytest` dependency.
- [x] Add `pytest-cov` dependency.
- [x] Add `ruff` dependency.
- [x] Add `langgraph` dependency if using LangGraph.
- [x] Add `crewai` dependency only if CrewAI is selected.
- [x] Add `networkx` dependency for graph analysis if useful.
- [x] Add `pydantic` dependency if structured models are used.
- [x] Add `python-dotenv` dependency if environment files are loaded.
- [x] Add any Graphify-specific dependency instructions.
- [x] Lock dependencies with `uv lock`.
- [x] Verify `uv run python --version` works.
- [x] Verify `uv run pytest` works, even if no tests exist yet.
- [x] Verify `uv run ruff check .` works.
- [x] Configure Ruff in `pyproject.toml`.
- [x] Configure coverage in `pyproject.toml`.
- [x] Set coverage `fail_under = 85` if feasible.
- [x] Add `src` as the coverage source.
- [x] Exclude generated artifacts from linting if needed.
- [x] Exclude target external repo files from linting if appropriate.
- [x] Document all tooling commands in README.

### 0.3 Candidate Repository Review

- [x] Identify candidate repositories with approximately 10,000+ source lines.
- [x] Identify candidate repositories with at least 70 source-code files.
- [x] Include team-owned repositories as valid candidates.
- [x] Include public repositories as valid candidates.
- [x] Exclude tiny broken-script repositories as main submission candidates.
- [x] Exclude toy repositories that cannot support architecture analysis.
- [x] Review candidate repository modularity.
- [x] Review candidate repository testability.
- [x] Review candidate repository dependency complexity.
- [x] Review candidate repository class/function structure.
- [x] Review candidate repository suitability for Graphify.
- [x] Review candidate repository suitability for Obsidian navigation.
- [x] Review candidate repository suitability for agent-guided debugging.
- [x] Review whether the repository has at least one focused bug path.
- [x] Review whether the repository has enough architecture for block diagrams.
- [x] Review whether the repository has enough OOP/module structure for diagrams.
- [x] Record candidate repository pros and cons.
- [x] Compare candidates against assignment requirements.
- [x] Compare candidates against available time.
- [x] Compare candidates against environment complexity.
- [x] Compare candidates against diagram potential.
- [x] Compare candidates against testability.
- [x] Count source-code files for top candidate.
- [x] Count meaningful source lines for top candidate.
- [x] Save source-count command.
- [x] Save source-count output.
- [x] Exclude generated files from count.
- [x] Exclude dependencies from count.
- [x] Exclude virtual environments from count.
- [x] Exclude cache folders from count.
- [x] Choose the final repository.
- [x] Choose `martinpeck/broken-python` as the instructor-approved exception repository.
- [x] Document the selected repository in README.
- [x] Document the selected repository in README.
- [x] Document rejected alternatives in README or report.
- [x] Explain why selected repository fits EX04.
- [x] Explain how selected repository satisfies 10,000+ LOC.
- [x] Explain how selected repository satisfies 70+ source-code files.
- [x] Create `reports/repository_size_report.md`.
- [x] Link repository size report from README.
- [x] Record that selected repository does not meet the numeric size threshold.
- [x] Record lecturer-approved exception.
- [x] Explain expected bug investigation scope.

### 0.4 Bug Candidate Selection

- [x] List possible bugs from the selected repository.
- [x] Identify bugs with clear reproduction steps.
- [x] Identify bugs with clear expected behavior.
- [x] Identify bugs with manageable source scope.
- [x] Identify bugs with meaningful graph path potential.
- [x] Avoid bugs requiring too much environment setup.
- [x] Avoid bugs that are purely trivial syntax fixes if possible.
- [x] Choose one primary bug.
- [x] Choose `mathsquiz` as the primary investigation subsystem.
- [x] Choose the exact `mathsquiz` bug instance: `print_final_scores` global-state coupling.
- [x] Choose one backup bug.
- [x] Use `polygons` only as backup if `mathsquiz` reproduction fails.
- [x] Record the selected bug in README.
- [x] Record the selected subsystem in README.
- [x] Record the selected bug in `obsidian/hot.md`.
- [x] Record the selected subsystem in `obsidian/hot.md`.
- [x] Record the selected bug in `reports/bug_analysis_report.md`.
- [x] Define initial expected behavior for `print_final_scores`.
- [x] Define initial actual behavior for `print_final_scores`.
- [x] Define initial reproduction plan for `print_final_scores`.
- [x] Define initial verification command.
- [x] Capture Phase 1 failing-output probe.
- [x] Save failing output to `artifacts/logs/`.
- [x] Record bug selection rationale.

### 0.5 Documentation Baseline

- [x] Copy or create `docs/PRD.md` from project PRD.
- [x] Copy or create `docs/PLAN.md` from project plan.
- [x] Create `docs/TODO.md` from this checklist.
- [x] Add initial README title.
- [x] Add README assignment summary.
- [x] Add README repository choice section.
- [x] Add README repository-size evidence section.
- [x] Add README selected bug section.
- [x] Add README quick-start section.
- [x] Add README project structure section.
- [x] Add README artifact index section.
- [x] Add README limitations section.
- [x] Add README final conclusion section.
- [x] Add report index to `obsidian/index.md`.
- [x] Add artifact index to `obsidian/index.md`.
- [x] Add research questions to `reports/reverse_engineering_report.md`.
- [x] Add research questions to README.
- [x] Add final checklist to `reports/final_submission_checklist.md`.
- [x] Create `docs/PRD_agent_instruction_architecture.md`.
- [x] Add agent instruction architecture section to README.

### 0.6 Phase 0 Review

- [x] Confirm selected repository is large enough for assignment requirements.
- [x] Confirm selected repository is not large enough but is approved by lecturer.
- [x] Confirm selected investigation path is focused enough to complete.
- [x] Confirm repository has approximately 10,000+ source lines.
- [x] Confirm repository has at least 70 source-code files.
- [x] Confirm repository choice is justified.
- [x] Confirm `mathsquiz` subsystem choice is documented.
- [x] Confirm selected bug is feasible.
- [x] Confirm initial agent instructions exist.
- [x] Confirm all required directories exist.
- [x] Confirm `uv` commands work.
- [x] Confirm initial docs exist.
- [x] Commit Phase 0 setup.

## Phase 1 - Graphify and Initial Knowledge Base

### 1.1 Graphify Preparation

- [x] Install or locate Graphify.
- [x] Read Graphify usage instructions.
- [x] Identify Graphify input path.
- [x] Identify Graphify output path.
- [x] Decide whether to run Graphify on full repo or selected subdirectory.
- [x] Exclude irrelevant folders if needed.
- [x] Exclude virtual environments.
- [x] Exclude build artifacts.
- [x] Exclude cache directories.
- [x] Exclude `.git`.
- [x] Exclude generated report directories if needed.
- [x] Record the exact Graphify command.
- [x] Add Graphify command to README.
- [x] Add Graphify command to `reports/reverse_engineering_report.md`.
- [x] Add Graphify command to `obsidian/index.md`.

### 1.2 Graphify Execution

- [x] Run Graphify on selected codebase.
- [x] Save `graph.json` to `artifacts/graphify/graph.json`.
- [x] Save `GRAPH_REPORT.md` to `artifacts/graphify/GRAPH_REPORT.md`.
- [x] Save any `graph.html` output to `artifacts/graphify/`.
- [x] Save any image output to `artifacts/graphify/`.
- [x] Save Graphify console logs to `artifacts/logs/graphify_run.md`.
- [x] Verify `graph.json` is valid JSON.
- [x] Verify `graph.json` contains nodes.
- [x] Verify `graph.json` contains edges.
- [x] Verify `GRAPH_REPORT.md` is readable.
- [x] Record total node count.
- [x] Record total edge count.
- [x] Record graph generation date.
- [x] Record Graphify limitations.
- [x] Record any parse failures.
- [x] Record unsupported files.
- [x] Record any missing semantic links.

### 1.3 Graph Artifact Inspection

- [x] Identify top-level files represented in graph.
- [x] Identify main modules represented in graph.
- [x] Identify functions represented in graph.
- [x] Identify classes represented in graph.
- [x] Identify import edges.
- [x] Identify call edges.
- [x] Identify semantic or inferred edges if available.
- [x] Identify ambiguous edges if available.
- [x] Identify high-degree nodes.
- [x] Identify possible hubs.
- [x] Identify possible God nodes.
- [x] Identify isolated nodes.
- [x] Identify isolated clusters.
- [x] Identify communities if available.
- [x] Identify bridge nodes if available.
- [x] Identify paths related to selected bug.
- [x] Identify nodes related to failing tests.
- [x] Identify nodes related to bug keywords.
- [x] Record initial graph observations in `reports/reverse_engineering_report.md`.
- [x] Record initial graph observations in `obsidian/architecture.md`.
- [x] Record initial graph observations in `obsidian/hot.md`.

### 1.4 Obsidian Vault Setup

- [x] Add title to `obsidian/index.md`.
- [x] Add project overview to `obsidian/index.md`.
- [x] Add source repository link to `obsidian/index.md`.
- [x] Add selected bug summary to `obsidian/index.md`.
- [x] Add navigation links to `obsidian/index.md`.
- [x] Link `[[hot]]` from `index.md`.
- [x] Link `[[architecture]]` from `index.md`.
- [x] Link `[[components]]` from `index.md`.
- [x] Link `[[bug_investigation]]` from `index.md`.
- [x] Link `[[tests_and_verification]]` from `index.md`.
- [x] Link `[[token_efficiency]]` from `index.md`.
- [x] Link `[[original_extension]]` from `index.md`.
- [x] Add Graphify artifact references to `index.md`.
- [x] Add report references to `index.md`.
- [x] Add diagram references to `index.md`.
- [x] Add open questions section to `index.md`.
- [x] Add current investigation status to `index.md`.

### 1.5 Hot Context Setup

- [x] Add title to `obsidian/hot.md`.
- [x] Add selected bug summary.
- [x] Add expected behavior.
- [x] Add actual behavior.
- [x] Add reproduction plan.
- [x] Add failing output summary.
- [x] Add suspected files section.
- [x] Add suspected modules section.
- [x] Add suspected functions/classes section.
- [x] Add Graphify evidence section.
- [x] Add source evidence section.
- [x] Add tests evidence section.
- [x] Add root-cause hypotheses section.
- [x] Add rejected hypotheses section.
- [x] Add final root cause section.
- [x] Add fix summary section.
- [x] Add verification section.
- [x] Link back to `[[index]]`.
- [x] Link to `[[bug_investigation]]`.
- [x] Link to `[[tests_and_verification]]`.

### 1.6 Component Notes

- [x] Create note for each major module.
- [x] Create note for each bug-critical module.
- [x] Create note for each major class if applicable.
- [x] Create note for each central function if applicable.
- [x] Add responsibility summary to each component note.
- [x] Add inbound relationships to each component note.
- [x] Add outbound relationships to each component note.
- [x] Add graph evidence to each component note.
- [x] Add source file references to each component note.
- [x] Link related components together.
- [x] Link bug-critical components to `hot.md`.
- [x] Link central components to `architecture.md`.

### 1.7 Phase 1 Review

- [x] Confirm Graphify artifacts exist.
- [x] Confirm Obsidian vault is navigable.
- [x] Confirm `index.md` is useful as entry point.
- [x] Confirm `hot.md` narrows bug context.
- [x] Confirm graph observations are documented.
- [x] Commit Phase 1 artifacts.

## Phase 2 - Reverse Engineering

### 2.1 Macro Architecture Reading

- [x] Identify project entry point.
- [x] Identify CLI entry point if present.
- [x] Identify GUI entry point if present.
- [x] Identify library API entry point if present.
- [x] Identify core business logic modules.
- [x] Identify data loading modules.
- [x] Identify configuration modules.
- [x] Identify output/reporting modules.
- [x] Identify external service calls if any.
- [x] Identify database or storage usage if any.
- [x] Identify test entry points.
- [x] Identify main execution path.
- [x] Identify bug-critical execution path.
- [x] Document macro architecture in `obsidian/architecture.md`.
- [x] Document macro architecture in `reports/reverse_engineering_report.md`.

### 2.2 Meso Community Reading

- [x] Identify graph communities or logical groups.
- [x] Determine whether communities match folders.
- [x] Determine whether communities cross folder boundaries.
- [x] Identify community representing bug-critical flow.
- [x] Identify community representing tests.
- [x] Identify community representing utilities.
- [x] Identify community representing models/classes.
- [x] Identify community representing I/O.
- [x] Identify bridge nodes between communities.
- [x] Identify risky bridge nodes.
- [x] Identify healthy hubs.
- [x] Identify possible bottlenecks.
- [x] Document community findings.
- [x] Add community notes to Obsidian.

### 2.3 Micro Node and Edge Reading

- [x] Select first bug-critical node.
- [x] Read node type.
- [x] Read source file.
- [x] Read incoming edges.
- [x] Read outgoing edges.
- [x] Read edge labels.
- [x] Read edge direction.
- [x] Read confidence if available.
- [x] Verify important edge in source code.
- [x] Repeat for second bug-critical node.
- [x] Repeat for third bug-critical node.
- [x] Repeat for central hub node.
- [x] Repeat for suspected bottleneck node.
- [x] Document verified relationships.
- [x] Mark unverified graph-only hypotheses.
- [x] Mark ambiguous relationships.

### 2.4 Research Questions

- [x] Answer what the actual architecture is.
- [x] Answer what was not obvious from first glance.
- [x] Answer which modules are most central.
- [x] Answer which classes are most central.
- [x] Answer which functions are most central.
- [x] Answer where complexity centers exist.
- [x] Answer where mixed responsibilities exist.
- [x] Answer whether God nodes exist.
- [x] Answer how architecture can be extracted from code.
- [x] Answer how OOP structure can be extracted.
- [x] Answer how Graphify helped.
- [x] Answer how Obsidian helped.
- [x] Answer where documentation was missing or misleading.

### 2.5 Architecture Block Diagram

- [x] Decide diagram format.
- [x] Use Mermaid if possible.
- [x] Create `artifacts/diagrams/architecture_block_diagram.md`.
- [x] Add system boundary.
- [x] Add user or caller block.
- [x] Add entry point block.
- [x] Add core module block.
- [x] Add service or processing block.
- [x] Add utility block.
- [x] Add data/config block if applicable.
- [x] Add test block if relevant.
- [x] Add bug-critical path.
- [x] Add arrows showing control flow.
- [x] Add arrows showing data flow if different.
- [x] Add note for graph-discovered relationship.
- [x] Add note for verified source relationship.
- [x] Add diagram explanation below Mermaid.
- [x] Link diagram from README.
- [x] Link diagram from `obsidian/architecture.md`.
- [x] Link diagram from reverse-engineering report.

### 2.6 OOP or Module Diagram

- [x] Determine whether target project has classes.
- [x] If classes exist, identify all relevant classes.
- [x] If classes exist, identify inheritance.
- [x] If classes exist, identify composition.
- [x] If classes exist, identify important method calls.
- [x] If classes exist, identify wrappers/adapters.
- [x] If classes do not exist, document procedural design.
- [x] If classes do not exist, create module/function interaction diagram.
- [x] Create `artifacts/diagrams/oop_diagram.md`.
- [x] Add Mermaid class diagram if applicable.
- [x] Add explanation of diagram.
- [x] Link diagram from README.
- [x] Link diagram from `obsidian/architecture.md`.
- [x] Link diagram from reverse-engineering report.

### 2.7 Reverse Engineering Report

- [x] Add report title.
- [x] Add repository overview.
- [x] Add selected bug overview.
- [x] Add Graphify method.
- [x] Add graph findings.
- [x] Add architecture findings.
- [x] Add component table.
- [x] Add central node table.
- [x] Add suspected bottleneck table.
- [x] Add community analysis.
- [x] Add source verification notes.
- [x] Add architecture diagram link.
- [x] Add OOP diagram link.
- [x] Add open questions.
- [x] Add limitations.
- [x] Add conclusion.

### 2.8 Phase 2 Review

- [x] Confirm architecture is understood.
- [x] Confirm diagrams are complete.
- [x] Confirm report answers research questions.
- [x] Confirm Graphify claims are source-verified where important.
- [x] Commit Phase 2 artifacts.

## Phase 3 - Agent Workflow

### 3.1 Agent Framework Setup

- [x] Confirm LangGraph or CrewAI choice.
- [x] Document framework choice in README.
- [x] Add framework dependency with `uv`.
- [x] Create `src/agent/`.
- [x] Create `src/agent/__init__.py`.
- [x] Create `src/agent/state.py`.
- [x] Create `src/agent/tools.py`.
- [x] Create `src/agent/workflow.py`.
- [x] Create `src/agent/prompts.py` if needed.
- [x] Create `src/agent/run_agent.py` if needed.
- [x] Create tests for agent helper functions if feasible.
- [x] Add agent run command to README.

### 3.2 Agent State Design

- [x] Define investigation state fields.
- [x] Add bug summary field.
- [x] Add graph artifacts field.
- [x] Add Obsidian context field.
- [x] Add suspect nodes field.
- [x] Add selected files field.
- [x] Add evidence field.
- [x] Add hypotheses field.
- [x] Add proposed fix field.
- [x] Add verification result field.
- [x] Add token estimate field.
- [x] Add file read log field.
- [x] Add iteration count field.
- [x] Add final report field.
- [x] Document state schema in `reports/agent_workflow_report.md`.

### 3.3 Agent Tools

- [x] Implement graph JSON loader.
- [x] Implement Graphify report reader.
- [x] Implement Obsidian note reader.
- [x] Implement source file reader.
- [x] Implement safe snippet extractor.
- [x] Implement file-read logger.
- [x] Implement character counter.
- [x] Implement token estimator.
- [x] Implement suspect node ranker or adapter.
- [x] Implement report writer.
- [x] Implement command runner for tests if safe.
- [x] Ensure tools do not read entire repo by default.
- [x] Ensure tools reject broad glob requests unless explicitly allowed.

### 3.4 Workflow Nodes

- [x] Implement `LoadGraphContext`.
- [x] Implement `LoadObsidianContext`.
- [x] Implement `SelectSuspects`.
- [x] Implement `ReadFocusedCode`.
- [x] Implement `HypothesizeRootCause`.
- [x] Implement `PlanFix`.
- [x] Implement `VerifyFix`.
- [x] Implement `WriteInvestigationLog`.
- [x] Add workflow edges.
- [x] Add stop condition.
- [x] Add error handling.
- [x] Add logging for each node.
- [x] Add text-unit count for each node.
- [x] Add token estimate for each node.

### 3.5 Agent Instructions and Prompts

- [x] Define agent roles before writing code.
- [x] Define agent responsibilities before writing code.
- [x] Define agent input contracts.
- [x] Define agent output contracts.
- [x] Define modular architecture rules for agent-generated code.
- [x] Define module-boundary preservation rules.
- [x] Define when agents must consult Graphify first.
- [x] Define when agents must consult Obsidian first.
- [x] Define when agents may inspect raw source files.
- [x] Define maximum raw files per investigation iteration.
- [x] Define evidence format for agent conclusions.
- [x] Define root-cause hypothesis format.
- [x] Define rejected-hypothesis logging format.
- [x] Define fix proposal format.
- [x] Define verification proposal format.
- [x] Write `docs/PRD_agent_instruction_architecture.md`.
- [x] Link agent instruction architecture from README.
- [x] Link agent instruction architecture from agent workflow report.
- [x] Write system prompt for graph-guided behavior.
- [x] Write prompt requiring `index.md` before source code.
- [x] Write prompt requiring `hot.md` before source code.
- [x] Write prompt requiring evidence labels.
- [x] Write prompt requiring hypothesis/fact separation.
- [x] Write prompt requiring minimal file reads.
- [x] Write prompt requiring root-cause explanation.
- [x] Write prompt requiring fix plan.
- [x] Write prompt requiring verification plan.
- [x] Save prompts in `src/agent/prompts.py` or report.
- [x] Document prompts in prompt log.

### 3.6 Agent Execution

- [x] Run graph-guided agent once.
- [x] Save raw run log.
- [x] Save selected suspect nodes.
- [x] Save selected files.
- [x] Save agent hypotheses.
- [x] Save agent proposed fix.
- [x] Save agent token estimates.
- [x] Save agent iteration count.
- [x] Update `artifacts/logs/graph_guided_agent_log.md`.
- [x] Update `reports/agent_workflow_report.md`.
- [x] Update `obsidian/bug_investigation.md`.
- [x] Update `obsidian/hot.md`.

### 3.7 Agent Workflow Report

- [x] Add framework choice explanation.
- [x] Add workflow diagram.
- [x] Add node descriptions.
- [x] Add state schema.
- [x] Add context narrowing strategy.
- [x] Add graph-first proof.
- [x] Add file-read log.
- [x] Add token estimate.
- [x] Add agent limitations.
- [x] Add future improvements.

### 3.8 Phase 3 Review

- [x] Confirm agent reads graph/Obsidian before source.
- [x] Confirm agent does not read all files.
- [x] Confirm workflow is reproducible.
- [x] Confirm logs are saved.
- [x] Commit Phase 3 artifacts.

## Phase 4 - Bug Reproduction, Root Cause, and Fix

### 4.1 Bug Reproduction

- [x] Write exact reproduction steps.
- [x] Identify required input.
- [x] Identify command to trigger bug.
- [x] Run command before fix.
- [x] Capture failure output.
- [x] Save failure output to `artifacts/logs/bug_reproduction_before.md`.
- [x] Identify expected output.
- [x] Identify actual output.
- [x] Add reproduction to README.
- [x] Add reproduction to `reports/bug_analysis_report.md`.
- [x] Add reproduction to `obsidian/hot.md`.

### 4.2 Root-Cause Investigation

- [x] Start from Graphify suspect list.
- [x] Start from `obsidian/hot.md`.
- [x] Inspect first suspected file.
- [x] Inspect second suspected file if needed.
- [x] Inspect tests related to bug.
- [x] Inspect call path to bug.
- [x] Inspect data path to bug.
- [x] Inspect configuration path if relevant.
- [x] Identify failing condition.
- [x] Identify incorrect assumption.
- [x] Identify missing validation if relevant.
- [x] Identify wrong branch or loop if relevant.
- [x] Identify wrong type handling if relevant.
- [x] Identify wrong API usage if relevant.
- [x] Identify root-cause line or function.
- [x] Verify root cause with source evidence.
- [x] Verify root cause with failing behavior.
- [x] Reject incorrect hypotheses.
- [x] Document rejected hypotheses.
- [x] Document final root cause.

### 4.3 Fix Planning

- [x] Define minimal code change.
- [x] Define expected behavior after fix.
- [x] Define test that proves fix.
- [x] Identify risk of regression.
- [x] Identify affected files.
- [x] Identify affected components.
- [x] Identify whether architecture diagram changes.
- [x] Identify whether Obsidian notes change.
- [x] Write fix plan in `reports/bug_analysis_report.md`.
- [x] Write fix plan in `obsidian/hot.md`.

### 4.4 Code Fix

- [x] Modify source code.
- [x] Keep fix minimal.
- [x] Avoid unrelated refactoring.
- [x] Add clear variable names.
- [x] Add comments only if needed.
- [x] Avoid hardcoded config values.
- [x] Keep file size under 150 lines where feasible.
- [x] Run formatting if configured.
- [x] Run Ruff.
- [x] Fix Ruff violations introduced by this change.

### 4.5 Test Fix

- [x] Add failing test before fix if feasible.
- [x] Add regression test for bug.
- [x] Add normal path test if missing.
- [x] Add edge case test if relevant.
- [x] Keep test file under 150 lines where feasible.
- [x] Use fixtures if helpful.
- [x] Avoid external services in tests.
- [x] Run focused test.
- [x] Run full test suite if feasible.
- [x] Save test output after fix.
- [x] Save output to `artifacts/logs/test_after_fix.md`.

### 4.6 Before/After Evidence

- [x] Capture before behavior.
- [x] Capture after behavior.
- [x] Capture before graph understanding.
- [x] Capture after graph understanding.
- [x] Update `obsidian/hot.md` with final root cause.
- [x] Update `obsidian/tests_and_verification.md`.
- [x] Update architecture diagram if structure changed.
- [x] Update OOP/module diagram if structure changed.
- [x] Save `artifacts/before_after/before.md`.
- [x] Save `artifacts/before_after/after.md`.
- [x] Add before/after section to README.

### 4.7 Bug Analysis Report

- [x] Add bug title.
- [x] Add expected behavior.
- [x] Add actual behavior.
- [x] Add reproduction steps.
- [x] Add failing output.
- [x] Add graph evidence.
- [x] Add Obsidian navigation path.
- [x] Add source evidence.
- [x] Add root cause.
- [x] Add fix explanation.
- [x] Add verification summary.
- [x] Add remaining risks.

### 4.8 Fix Verification Report

- [x] Add verification command.
- [x] Add before status.
- [x] Add after status.
- [x] Add tests added.
- [x] Add test output summary.
- [x] Add coverage summary if available.
- [x] Add limitations if full test suite cannot run.
- [x] Add final verification conclusion.

### 4.9 Phase 4 Review

- [x] Confirm bug is reproduced.
- [x] Confirm root cause is verified.
- [x] Confirm fix is implemented.
- [x] Confirm tests or checks pass.
- [x] Confirm before/after evidence is documented.
- [x] Commit Phase 4 fix and reports.

## Phase 5 - Token Efficiency Measurement

### 5.1 Measurement Setup

- [x] Define text-unit counting rules.
- [x] Define token estimation formula.
- [x] Define iteration counting rules.
- [x] Define quality rating scale.
- [x] Create `artifacts/token_measurements/token_comparison.csv`.
- [x] Create `artifacts/logs/naive_baseline_log.md`.
- [x] Create `artifacts/logs/graph_guided_agent_log.md`.
- [x] Add measurement method to token report.

### 5.2 Naive Baseline Workflow

- [x] Define naive workflow prompt or process.
- [x] Do not use Graphify in naive mode.
- [x] Do not use Obsidian in naive mode.
- [x] Select broad source files manually or by folder.
- [x] Record each file read.
- [x] Count characters for each file read.
- [x] Estimate tokens for each file read.
- [x] Record number of investigation iterations.
- [x] Record whether root cause was reached.
- [x] Record whether fix was reached.
- [x] Record time or step count if available.
- [x] Record quality of explanation.
- [x] Save naive baseline log.

### 5.3 Graph-Guided Workflow

- [x] Define graph-guided workflow prompt or process.
- [x] Read `graph.json` summary.
- [x] Read `GRAPH_REPORT.md`.
- [x] Read `obsidian/index.md`.
- [x] Read `obsidian/hot.md`.
- [x] Read selected source files only.
- [x] Record each text unit read.
- [x] Count characters for each text unit.
- [x] Estimate tokens for each text unit.
- [x] Record number of investigation iterations.
- [x] Record whether root cause was reached.
- [x] Record whether fix was reached.
- [x] Record time or step count if available.
- [x] Record quality of explanation.
- [x] Save graph-guided log.

### 5.4 Comparison Table

- [x] Add baseline row.
- [x] Add graph-guided row.
- [x] Add files/text units read.
- [x] Add input token estimate.
- [x] Add output token estimate if available.
- [x] Add total token estimate.
- [x] Add iterations.
- [x] Add root-cause status.
- [x] Add fix status.
- [x] Add quality rating.
- [x] Add notes.
- [x] Calculate percentage token reduction.
- [x] Calculate file-read reduction.
- [x] Calculate iteration reduction.

### 5.5 Token Efficiency Report

- [x] Add report title.
- [x] Add measurement method.
- [x] Add baseline description.
- [x] Add graph-guided description.
- [x] Add comparison table.
- [x] Add interpretation.
- [x] Add limitations.
- [x] Add conclusion.
- [x] Link logs.
- [x] Link CSV.
- [x] Link from README.
- [x] Link from Obsidian.

### 5.6 Phase 5 Review

- [x] Confirm metrics are transparent.
- [x] Confirm graph-guided workflow is compared fairly.
- [x] Confirm limitations are honest.
- [x] Confirm report is linked.
- [x] Commit Phase 5 artifacts.

## Phase 6 - Original Extension

### 6.1 Extension Selection

- [x] Confirm selected extension.
- [x] Document why extension was chosen.
- [x] Document how extension exceeds minimum requirements.
- [x] Document how extension supports token efficiency.
- [x] Document how extension supports reverse engineering.

### 6.2 Suspicious Node Ranking

- [x] Create `src/analysis/`.
- [x] Create `src/analysis/__init__.py`.
- [x] Create `src/analysis/graph_loader.py`.
- [x] Create `src/analysis/suspicious_nodes.py`.
- [x] Load `graph.json`.
- [x] Parse nodes.
- [x] Parse edges.
- [x] Compute degree for nodes.
- [x] Compute inbound degree.
- [x] Compute outbound degree.
- [x] Compute keyword score.
- [x] Compute proximity to bug keywords.
- [x] Compute proximity to failing test names if possible.
- [x] Combine scores.
- [x] Sort suspicious nodes.
- [x] Output top 5 suspicious nodes.
- [x] Output top 10 suspicious nodes.
- [x] Save suspicious node report.
- [x] Add explanation of scoring method.
- [x] Add limitations of scoring method.

### 6.3 Dynamic Hot Context Generation

- [x] Create `src/analysis/hot_md_generator.py`.
- [x] Read suspicious node report.
- [x] Read selected bug summary.
- [x] Read Graphify artifact paths.
- [x] Read source file references.
- [x] Generate `hot.md` header.
- [x] Generate bug summary section.
- [x] Generate top suspects section.
- [x] Generate graph evidence section.
- [x] Generate source files to inspect section.
- [x] Generate open questions section.
- [x] Generate links back to index.
- [x] Write generated output to `obsidian/hot.generated.md`.
- [x] Decide whether to merge into `obsidian/hot.md`.
- [x] Document generated file in README.

### 6.4 Optional Git Diff Integration

- [x] Check whether project is in Git.
- [x] Capture diff after fix.
- [x] Save diff to `artifacts/before_after/fix.diff`.
- [x] Parse changed files.
- [x] Add changed files to generated hot context.
- [x] Add impact section to generated hot context.
- [x] Document diff integration.

### 6.5 Original Extension Report

- [x] Add extension title.
- [x] Add motivation.
- [x] Add inputs.
- [x] Add algorithm.
- [x] Add outputs.
- [x] Add example result.
- [x] Add how it improves context selection.
- [x] Add limitations.
- [x] Add future improvements.

### 6.6 Phase 6 Review

- [x] Confirm extension artifact exists.
- [x] Confirm extension is explained in README.
- [x] Confirm extension connects to EX04 requirements.
- [x] Confirm extension is not just cosmetic.
- [x] Commit Phase 6 artifacts.

## Phase 7 - Final README and Submission Packaging

### 7.1 README Repository Choice Section

- [x] Add selected repository name.
- [x] Add selected repository URL.
- [x] Add repository description.
- [x] Add reason for selection.
- [x] Add why rejected repositories were not selected.
- [x] Add why selected repository fits EX04.

### 7.2 README Selected Bug Section

- [x] Add bug title.
- [x] Add bug summary.
- [x] Add expected behavior.
- [x] Add actual behavior.
- [x] Add reproduction command.
- [x] Add affected files.
- [x] Add link to bug report.

### 7.3 README Research Questions Section

- [x] List all assignment research questions.
- [x] Answer each question briefly.
- [x] Link detailed answers to reports.
- [x] Link detailed answers to Obsidian notes.

### 7.4 README Quick Start Section

- [x] Add clone instructions.
- [x] Add dependency installation command.
- [x] Add bug reproduction command.
- [x] Add test command.
- [x] Add agent workflow command.
- [x] Add graph generation command if reproducible.
- [x] Add artifact browsing instructions.

### 7.5 README Project Structure Section

- [x] Add tree of repository structure.
- [x] Explain `src/`.
- [x] Explain `tests/`.
- [x] Explain `obsidian/`.
- [x] Explain `reports/`.
- [x] Explain `artifacts/`.
- [x] Explain `data/`.
- [x] Explain `config/` if present.

### 7.6 README Graphify Section

- [x] Explain Graphify role.
- [x] Link `graph.json`.
- [x] Link `GRAPH_REPORT.md`.
- [x] Link graph visualization if available.
- [x] Summarize main graph findings.
- [x] Explain limitations.

### 7.7 README Obsidian Section

- [x] Explain Obsidian vault role.
- [x] Link `obsidian/index.md`.
- [x] Link `obsidian/hot.md`.
- [x] Explain navigation strategy.
- [x] Explain how vault changed after fix.

### 7.8 README Architecture Section

- [x] Embed or link architecture block diagram.
- [x] Embed or link OOP/module diagram.
- [x] Summarize main architecture.
- [x] Summarize central components.
- [x] Summarize bottlenecks or God nodes.

### 7.9 README Agent Workflow Section

- [x] Explain chosen framework.
- [x] Show workflow stages.
- [x] Link agent workflow report.
- [x] Link graph-guided agent log.
- [x] Explain how context was narrowed.

### 7.10 README Bug Investigation Section

- [x] Summarize investigation path.
- [x] Summarize root cause.
- [x] Link bug report.
- [x] Link hot context.
- [x] Link source evidence.

### 7.11 README Fix Section

- [x] Explain code fix.
- [x] Explain why fix is correct.
- [x] Link changed files.
- [x] Link verification report.
- [x] Include before/after behavior.

### 7.12 README Token Efficiency Section

- [x] Add comparison table.
- [x] Add token reduction result.
- [x] Add file-read reduction result.
- [x] Add iteration reduction result.
- [x] Link detailed token report.
- [x] Explain measurement limitations.

### 7.13 README Original Extension Section

- [x] Explain extension.
- [x] Link extension report.
- [x] Link generated artifacts.
- [x] Explain value beyond minimum.

### 7.14 README Artifact Index

- [x] Add report links.
- [x] Add diagram links.
- [x] Add Graphify artifact links.
- [x] Add Obsidian links.
- [x] Add logs links.
- [x] Add token measurement links.
- [x] Add screenshots links.

### 7.15 Final Quality Checks

- [x] Run tests.
- [x] Run Ruff.
- [x] Check coverage if configured.
- [x] Check no secrets exist.
- [x] Check `.env` is ignored.
- [x] Check `.env-example` exists.
- [x] Check `uv.lock` status documented.
- [x] Check README links.
- [x] Check Obsidian links.
- [x] Check diagrams render.
- [x] Check reports are complete.
- [x] Check artifact paths are correct.
- [x] Check line length and formatting.
- [x] Check final checklist.

### 7.16 Final Submission

- [x] Commit final changes.
- [x] Push to GitHub.
- [x] Verify GitHub renders README.
- [x] Verify GitHub renders diagrams.
- [x] Verify all required artifacts are present online.
- [x] Copy final repository URL.
- [x] Prepare short submission message.
- [x] Submit according to course instructions.

## Cross-Phase Research Question Tracking

- [x] RQ1: Actual architecture answered in README.
- [x] RQ1: Actual architecture answered in reverse-engineering report.
- [x] RQ1: Actual architecture represented in architecture diagram.
- [x] RQ2: Non-obvious discoveries answered in README.
- [x] RQ2: Non-obvious discoveries answered in reverse-engineering report.
- [x] RQ3: Central modules/classes/functions answered in README.
- [x] RQ3: Central modules/classes/functions answered in component notes.
- [x] RQ4: God nodes and complexity centers answered in report.
- [x] RQ4: God nodes and complexity centers linked to graph evidence.
- [x] RQ5: Architectural blocks extraction explained.
- [x] RQ5: OOP extraction explained.
- [x] RQ6: Bug identification process explained.
- [x] RQ7: Root cause explained.
- [x] RQ8: Investigation steps documented.
- [x] RQ9: Graphify advantage explained.
- [x] RQ10: Obsidian advantage explained.
- [x] RQ11: Agent token savings explained.
- [x] RQ12: Future improvements proposed.

## Final Deliverable Tracking

- [x] Full Python solution code exists.
- [x] Agent workflow implementation exists.
- [x] Graphify `graph.json` exists.
- [x] Graphify report exists.
- [x] Obsidian vault exists.
- [x] `obsidian/index.md` exists.
- [x] `obsidian/hot.md` exists.
- [x] Bug analysis report exists.
- [x] Root-cause report content complete.
- [x] Token efficiency report exists.
- [x] Architecture block diagram exists.
- [x] OOP/module diagram exists.
- [x] Before/after proof exists.
- [x] Original extension documentation exists.
- [x] README exists.
- [x] README is complete.
- [x] Run instructions exist.
- [x] Test instructions exist.
- [x] Artifact index exists.

## Professional Submission Guideline Tracking

- [x] Root README is user-manual quality.
- [x] Installation instructions exist.
- [x] Usage instructions exist.
- [x] Configuration instructions exist.
- [x] Contribution or development notes exist if useful.
- [x] License/credits section exists.
- [x] `docs/PRD.md` exists.
- [x] `docs/PLAN.md` exists.
- [x] `docs/TODO.md` exists.
- [x] Mechanism-specific PRD exists if needed.
- [x] Project structure is clear.
- [x] Code files are under 150 lines where feasible.
- [x] Functions have clear names.
- [x] Modules have clear names.
- [x] Comments explain why, not obvious what.
- [x] Public functions have tests where feasible.
- [x] TDD evidence is described.
- [x] Coverage target is documented.
- [x] Ruff configuration exists.
- [x] Ruff result is documented.
- [x] No hardcoded secrets.
- [x] Config files are separate from code.
- [x] `.env-example` exists.
- [x] `.gitignore` protects secrets.
- [x] `uv` is used for commands.
- [x] `pyproject.toml` exists.
- [x] `uv.lock` status documented.
- [x] Git history is meaningful.
- [x] Prompt log exists if major prompts are used.
- [x] Cost/token analysis exists.
- [x] Visualizations exist.
- [x] UI screenshots included if UI exists.
- [x] ISO/IEC 25010 quality reflection included if useful.

## Optional Enhancement Backlog

- [x] Add graph centrality visualization.
- [x] Add before/after graph diff.
- [x] Add source-to-Obsidian backlink generator.
- [x] Add test-to-component traceability matrix.
- [x] Add agent prompt registry.
- [x] Add JSON schema for Graphify artifacts.
- [x] Add automated artifact index generator.
- [x] Add coverage badge if appropriate.
- [x] Add Mermaid render screenshots.
- [x] Add dependency graph.
- [x] Add module risk score.
- [x] Add root-cause timeline.
- [x] Add architecture decision records.
- [x] Add `docs/ADR_001_repository_choice.md`.
- [x] Add `docs/ADR_002_agent_framework.md`.
- [x] Add `docs/ADR_003_original_extension.md`.
- [x] Add limitations table.
- [x] Add future work roadmap.

## Completion Notes

- [x] Record final selected repository.
- [x] Record final selected bug: `print_final_scores` global-state coupling.
- [x] Record final Graphify command.
- [x] Record final agent command.
- [x] Record final test command.
- [x] Record final token reduction.
- [x] Record final file-read reduction.
- [x] Record final iteration reduction.
- [x] Record final original extension.
- [x] Record final submission URL.


