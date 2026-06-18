# EX04 Detailed TODO

## Status Legend

- [ ] Not started
- [~] In progress
- [x] Completed
- [!] Blocked

## Phase 0 - Project Setup and Repository Choice

### 0.1 Workspace Preparation

- [ ] Create or confirm the final GitHub repository.
- [ ] Confirm the repository is private or public according to course policy.
- [ ] Add a clean root-level `README.md`.
- [ ] Add a root-level `.gitignore`.
- [ ] Add a root-level `.env-example`.
- [ ] Add a root-level `pyproject.toml`.
- [ ] Add a root-level `uv.lock` after dependency setup.
- [ ] Add a root-level `docs/` directory.
- [ ] Add a root-level `src/` directory.
- [ ] Add a root-level `tests/` directory.
- [ ] Add a root-level `obsidian/` directory.
- [ ] Add a root-level `reports/` directory.
- [ ] Add a root-level `artifacts/` directory.
- [ ] Add a root-level `data/` directory if input data is needed.
- [ ] Add a root-level `config/` directory if configuration files are needed.
- [ ] Add a root-level `notebooks/` directory if analysis notebooks are used.
- [ ] Add `artifacts/graphify/`.
- [ ] Add `artifacts/diagrams/`.
- [ ] Add `artifacts/logs/`.
- [ ] Add `artifacts/screenshots/`.
- [ ] Add `artifacts/token_measurements/`.
- [ ] Add `artifacts/before_after/`.
- [ ] Add `reports/reverse_engineering_report.md`.
- [ ] Add `reports/agent_workflow_report.md`.
- [ ] Add `reports/bug_analysis_report.md`.
- [ ] Add `reports/fix_verification_report.md`.
- [ ] Add `reports/token_efficiency_report.md`.
- [ ] Add `reports/original_extension_report.md`.
- [ ] Add `reports/final_submission_checklist.md`.
- [ ] Add `obsidian/index.md`.
- [ ] Add `obsidian/hot.md`.
- [ ] Add `obsidian/architecture.md`.
- [ ] Add `obsidian/components.md`.
- [ ] Add `obsidian/bug_investigation.md`.
- [ ] Add `obsidian/tests_and_verification.md`.
- [ ] Add `obsidian/token_efficiency.md`.
- [ ] Add `obsidian/original_extension.md`.

### 0.2 Tooling Setup

- [ ] Confirm Python version.
- [ ] Confirm `uv` is installed.
- [ ] Initialize `pyproject.toml` using `uv` if needed.
- [ ] Add development dependencies with `uv add --dev`.
- [ ] Add `pytest` dependency.
- [ ] Add `pytest-cov` dependency.
- [ ] Add `ruff` dependency.
- [ ] Add `langgraph` dependency if using LangGraph.
- [ ] Add `crewai` dependency only if CrewAI is selected.
- [ ] Add `networkx` dependency for graph analysis if useful.
- [ ] Add `pydantic` dependency if structured models are used.
- [ ] Add `python-dotenv` dependency if environment files are loaded.
- [ ] Add any Graphify-specific dependency instructions.
- [ ] Lock dependencies with `uv lock`.
- [ ] Verify `uv run python --version` works.
- [ ] Verify `uv run pytest` works, even if no tests exist yet.
- [ ] Verify `uv run ruff check .` works.
- [ ] Configure Ruff in `pyproject.toml`.
- [ ] Configure coverage in `pyproject.toml`.
- [ ] Set coverage `fail_under = 85` if feasible.
- [ ] Add `src` as the coverage source.
- [ ] Exclude generated artifacts from linting if needed.
- [ ] Exclude target external repo files from linting if appropriate.
- [ ] Document all tooling commands in README.

### 0.3 Candidate Repository Review

- [ ] Identify candidate repositories with approximately 10,000+ source lines.
- [ ] Identify candidate repositories with at least 70 source-code files.
- [ ] Include team-owned repositories as valid candidates.
- [ ] Include public repositories as valid candidates.
- [ ] Exclude tiny broken-script repositories as main submission candidates.
- [ ] Exclude toy repositories that cannot support architecture analysis.
- [ ] Review candidate repository modularity.
- [ ] Review candidate repository testability.
- [ ] Review candidate repository dependency complexity.
- [ ] Review candidate repository class/function structure.
- [ ] Review candidate repository suitability for Graphify.
- [ ] Review candidate repository suitability for Obsidian navigation.
- [ ] Review candidate repository suitability for agent-guided debugging.
- [ ] Review whether the repository has at least one focused bug path.
- [ ] Review whether the repository has enough architecture for block diagrams.
- [ ] Review whether the repository has enough OOP/module structure for diagrams.
- [ ] Record candidate repository pros and cons.
- [ ] Compare candidates against assignment requirements.
- [ ] Compare candidates against available time.
- [ ] Compare candidates against environment complexity.
- [ ] Compare candidates against diagram potential.
- [ ] Compare candidates against testability.
- [ ] Count source-code files for top candidate.
- [ ] Count meaningful source lines for top candidate.
- [ ] Save source-count command.
- [ ] Save source-count output.
- [ ] Exclude generated files from count.
- [ ] Exclude dependencies from count.
- [ ] Exclude virtual environments from count.
- [ ] Exclude cache folders from count.
- [ ] Choose the final repository.
- [x] Choose `martinpeck/broken-python` as the instructor-approved exception repository.
- [ ] Document the selected repository in README.
- [x] Document the selected repository in README.
- [ ] Document rejected alternatives in README or report.
- [ ] Explain why selected repository fits EX04.
- [ ] Explain how selected repository satisfies 10,000+ LOC.
- [ ] Explain how selected repository satisfies 70+ source-code files.
- [ ] Create `reports/repository_size_report.md`.
- [ ] Link repository size report from README.
- [x] Record that selected repository does not meet the numeric size threshold.
- [x] Record lecturer-approved exception.
- [ ] Explain expected bug investigation scope.

### 0.4 Bug Candidate Selection

- [ ] List possible bugs from the selected repository.
- [ ] Identify bugs with clear reproduction steps.
- [ ] Identify bugs with clear expected behavior.
- [ ] Identify bugs with manageable source scope.
- [ ] Identify bugs with meaningful graph path potential.
- [ ] Avoid bugs requiring too much environment setup.
- [ ] Avoid bugs that are purely trivial syntax fixes if possible.
- [ ] Choose one primary bug.
- [x] Choose `mathsquiz` as the primary investigation subsystem.
- [x] Choose the exact `mathsquiz` bug instance: `print_final_scores` global-state coupling.
- [ ] Choose one backup bug.
- [ ] Use `polygons` only as backup if `mathsquiz` reproduction fails.
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
- [ ] Save failing output to `artifacts/logs/`.
- [ ] Record bug selection rationale.

### 0.5 Documentation Baseline

- [ ] Copy or create `docs/PRD.md` from project PRD.
- [ ] Copy or create `docs/PLAN.md` from project plan.
- [ ] Create `docs/TODO.md` from this checklist.
- [ ] Add initial README title.
- [ ] Add README assignment summary.
- [ ] Add README repository choice section.
- [ ] Add README repository-size evidence section.
- [x] Add README selected bug section.
- [ ] Add README quick-start placeholder.
- [ ] Add README project structure placeholder.
- [ ] Add README artifact index placeholder.
- [ ] Add README limitations placeholder.
- [ ] Add README final conclusion placeholder.
- [ ] Add report index to `obsidian/index.md`.
- [ ] Add artifact index to `obsidian/index.md`.
- [ ] Add research questions to `reports/reverse_engineering_report.md`.
- [ ] Add research questions to README.
- [x] Add final checklist to `reports/final_submission_checklist.md`.
- [x] Create `docs/PRD_agent_instruction_architecture.md`.
- [x] Add agent instruction architecture placeholder to README.

### 0.6 Phase 0 Review

- [ ] Confirm selected repository is large enough for assignment requirements.
- [x] Confirm selected repository is not large enough but is approved by lecturer.
- [ ] Confirm selected investigation path is focused enough to complete.
- [ ] Confirm repository has approximately 10,000+ source lines.
- [ ] Confirm repository has at least 70 source-code files.
- [ ] Confirm repository choice is justified.
- [x] Confirm `mathsquiz` subsystem choice is documented.
- [x] Confirm selected bug is feasible.
- [ ] Confirm initial agent instructions exist.
- [ ] Confirm all required directories exist.
- [ ] Confirm `uv` commands work.
- [ ] Confirm initial docs exist.
- [ ] Commit Phase 0 setup.

## Phase 1 - Graphify and Initial Knowledge Base

### 1.1 Graphify Preparation

- [x] Install or locate Graphify.
- [ ] Read Graphify usage instructions.
- [x] Identify Graphify input path.
- [x] Identify Graphify output path.
- [x] Decide whether to run Graphify on full repo or selected subdirectory.
- [ ] Exclude irrelevant folders if needed.
- [ ] Exclude virtual environments.
- [ ] Exclude build artifacts.
- [ ] Exclude cache directories.
- [x] Exclude `.git`.
- [ ] Exclude generated report directories if needed.
- [x] Record the exact Graphify command.
- [ ] Add Graphify command to README.
- [ ] Add Graphify command to `reports/reverse_engineering_report.md`.
- [ ] Add Graphify command to `obsidian/index.md`.

### 1.2 Graphify Execution

- [x] Run Graphify on selected codebase.
- [x] Save `graph.json` to `artifacts/graphify/graph.json`.
- [x] Save `GRAPH_REPORT.md` to `artifacts/graphify/GRAPH_REPORT.md`.
- [x] Save any `graph.html` output to `artifacts/graphify/`.
- [ ] Save any image output to `artifacts/graphify/`.
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
- [ ] Record unsupported files.
- [ ] Record any missing semantic links.

### 1.3 Graph Artifact Inspection

- [x] Identify top-level files represented in graph.
- [x] Identify main modules represented in graph.
- [x] Identify functions represented in graph.
- [x] Identify classes represented in graph.
- [ ] Identify import edges.
- [x] Identify call edges.
- [x] Identify semantic or inferred edges if available.
- [ ] Identify ambiguous edges if available.
- [x] Identify high-degree nodes.
- [x] Identify possible hubs.
- [ ] Identify possible God nodes.
- [ ] Identify isolated nodes.
- [ ] Identify isolated clusters.
- [ ] Identify communities if available.
- [ ] Identify bridge nodes if available.
- [x] Identify paths related to selected bug.
- [ ] Identify nodes related to failing tests.
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
- [ ] Add suspected modules section.
- [ ] Add suspected functions/classes section.
- [ ] Add Graphify evidence section.
- [ ] Add source evidence section.
- [ ] Add tests evidence section.
- [ ] Add root-cause hypotheses section.
- [ ] Add rejected hypotheses section.
- [ ] Add final root cause placeholder.
- [ ] Add fix summary placeholder.
- [ ] Add verification placeholder.
- [ ] Link back to `[[index]]`.
- [ ] Link to `[[bug_investigation]]`.
- [ ] Link to `[[tests_and_verification]]`.

### 1.6 Component Notes

- [ ] Create note for each major module.
- [ ] Create note for each bug-critical module.
- [ ] Create note for each major class if applicable.
- [ ] Create note for each central function if applicable.
- [ ] Add responsibility summary to each component note.
- [ ] Add inbound relationships to each component note.
- [ ] Add outbound relationships to each component note.
- [ ] Add graph evidence to each component note.
- [ ] Add source file references to each component note.
- [ ] Link related components together.
- [x] Link bug-critical components to `hot.md`.
- [x] Link central components to `architecture.md`.

### 1.7 Phase 1 Review

- [x] Confirm Graphify artifacts exist.
- [x] Confirm Obsidian vault is navigable.
- [x] Confirm `index.md` is useful as entry point.
- [x] Confirm `hot.md` narrows bug context.
- [x] Confirm graph observations are documented.
- [ ] Commit Phase 1 artifacts.

## Phase 2 - Reverse Engineering

### 2.1 Macro Architecture Reading

- [x] Identify project entry point.
- [ ] Identify CLI entry point if present.
- [ ] Identify GUI entry point if present.
- [ ] Identify library API entry point if present.
- [ ] Identify core business logic modules.
- [ ] Identify data loading modules.
- [ ] Identify configuration modules.
- [ ] Identify output/reporting modules.
- [ ] Identify external service calls if any.
- [ ] Identify database or storage usage if any.
- [ ] Identify test entry points.
- [ ] Identify main execution path.
- [x] Identify bug-critical execution path.
- [x] Document macro architecture in `obsidian/architecture.md`.
- [x] Document macro architecture in `reports/reverse_engineering_report.md`.

### 2.2 Meso Community Reading

- [ ] Identify graph communities or logical groups.
- [ ] Determine whether communities match folders.
- [ ] Determine whether communities cross folder boundaries.
- [ ] Identify community representing bug-critical flow.
- [ ] Identify community representing tests.
- [ ] Identify community representing utilities.
- [ ] Identify community representing models/classes.
- [ ] Identify community representing I/O.
- [ ] Identify bridge nodes between communities.
- [ ] Identify risky bridge nodes.
- [ ] Identify healthy hubs.
- [x] Identify possible bottlenecks.
- [x] Document community findings.
- [x] Add community notes to Obsidian.

### 2.3 Micro Node and Edge Reading

- [ ] Select first bug-critical node.
- [ ] Read node type.
- [ ] Read source file.
- [ ] Read incoming edges.
- [ ] Read outgoing edges.
- [ ] Read edge labels.
- [ ] Read edge direction.
- [ ] Read confidence if available.
- [ ] Verify important edge in source code.
- [ ] Repeat for second bug-critical node.
- [ ] Repeat for third bug-critical node.
- [ ] Repeat for central hub node.
- [ ] Repeat for suspected bottleneck node.
- [ ] Document verified relationships.
- [ ] Mark unverified graph-only hypotheses.
- [ ] Mark ambiguous relationships.

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
- [ ] Answer how Obsidian helped.
- [ ] Answer where documentation was missing or misleading.

### 2.5 Architecture Block Diagram

- [x] Decide diagram format.
- [x] Use Mermaid if possible.
- [x] Create `artifacts/diagrams/architecture_block_diagram.md`.
- [x] Add system boundary.
- [ ] Add user or caller block.
- [ ] Add entry point block.
- [ ] Add core module block.
- [ ] Add service or processing block.
- [ ] Add utility block.
- [ ] Add data/config block if applicable.
- [ ] Add test block if relevant.
- [ ] Add bug-critical path.
- [ ] Add arrows showing control flow.
- [ ] Add arrows showing data flow if different.
- [ ] Add note for graph-discovered relationship.
- [ ] Add note for verified source relationship.
- [x] Add diagram explanation below Mermaid.
- [x] Link diagram from README.
- [x] Link diagram from `obsidian/architecture.md`.
- [x] Link diagram from reverse-engineering report.

### 2.6 OOP or Module Diagram

- [x] Determine whether target project has classes.
- [ ] If classes exist, identify all relevant classes.
- [ ] If classes exist, identify inheritance.
- [ ] If classes exist, identify composition.
- [ ] If classes exist, identify important method calls.
- [ ] If classes exist, identify wrappers/adapters.
- [x] If classes do not exist, document procedural design.
- [x] If classes do not exist, create module/function interaction diagram.
- [x] Create `artifacts/diagrams/oop_diagram.md`.
- [x] Add Mermaid class diagram if applicable.
- [x] Add explanation of diagram.
- [x] Link diagram from README.
- [x] Link diagram from `obsidian/architecture.md`.
- [x] Link diagram from reverse-engineering report.

### 2.7 Reverse Engineering Report

- [ ] Add report title.
- [x] Add repository overview.
- [x] Add selected bug overview.
- [ ] Add Graphify method.
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

- [ ] Write exact reproduction steps.
- [ ] Identify required input.
- [ ] Identify command to trigger bug.
- [ ] Run command before fix.
- [ ] Capture failure output.
- [ ] Save failure output to `artifacts/logs/bug_reproduction_before.md`.
- [ ] Identify expected output.
- [ ] Identify actual output.
- [ ] Add reproduction to README.
- [ ] Add reproduction to `reports/bug_analysis_report.md`.
- [ ] Add reproduction to `obsidian/hot.md`.

### 4.2 Root-Cause Investigation

- [ ] Start from Graphify suspect list.
- [ ] Start from `obsidian/hot.md`.
- [ ] Inspect first suspected file.
- [ ] Inspect second suspected file if needed.
- [ ] Inspect tests related to bug.
- [ ] Inspect call path to bug.
- [ ] Inspect data path to bug.
- [ ] Inspect configuration path if relevant.
- [ ] Identify failing condition.
- [ ] Identify incorrect assumption.
- [ ] Identify missing validation if relevant.
- [ ] Identify wrong branch or loop if relevant.
- [ ] Identify wrong type handling if relevant.
- [ ] Identify wrong API usage if relevant.
- [ ] Identify root-cause line or function.
- [ ] Verify root cause with source evidence.
- [ ] Verify root cause with failing behavior.
- [ ] Reject incorrect hypotheses.
- [ ] Document rejected hypotheses.
- [ ] Document final root cause.

### 4.3 Fix Planning

- [ ] Define minimal code change.
- [ ] Define expected behavior after fix.
- [ ] Define test that proves fix.
- [ ] Identify risk of regression.
- [ ] Identify affected files.
- [ ] Identify affected components.
- [ ] Identify whether architecture diagram changes.
- [ ] Identify whether Obsidian notes change.
- [ ] Write fix plan in `reports/bug_analysis_report.md`.
- [ ] Write fix plan in `obsidian/hot.md`.

### 4.4 Code Fix

- [ ] Modify source code.
- [ ] Keep fix minimal.
- [ ] Avoid unrelated refactoring.
- [ ] Add clear variable names.
- [ ] Add comments only if needed.
- [ ] Avoid hardcoded config values.
- [ ] Keep file size under 150 lines where feasible.
- [ ] Run formatting if configured.
- [ ] Run Ruff.
- [ ] Fix Ruff violations introduced by this change.

### 4.5 Test Fix

- [ ] Add failing test before fix if feasible.
- [ ] Add regression test for bug.
- [ ] Add normal path test if missing.
- [ ] Add edge case test if relevant.
- [ ] Keep test file under 150 lines where feasible.
- [ ] Use fixtures if helpful.
- [ ] Avoid external services in tests.
- [ ] Run focused test.
- [ ] Run full test suite if feasible.
- [ ] Save test output after fix.
- [ ] Save output to `artifacts/logs/test_after_fix.md`.

### 4.6 Before/After Evidence

- [ ] Capture before behavior.
- [ ] Capture after behavior.
- [ ] Capture before graph understanding.
- [ ] Capture after graph understanding.
- [ ] Update `obsidian/hot.md` with final root cause.
- [ ] Update `obsidian/tests_and_verification.md`.
- [ ] Update architecture diagram if structure changed.
- [ ] Update OOP/module diagram if structure changed.
- [ ] Save `artifacts/before_after/before.md`.
- [ ] Save `artifacts/before_after/after.md`.
- [ ] Add before/after section to README.

### 4.7 Bug Analysis Report

- [ ] Add bug title.
- [ ] Add expected behavior.
- [ ] Add actual behavior.
- [ ] Add reproduction steps.
- [ ] Add failing output.
- [ ] Add graph evidence.
- [ ] Add Obsidian navigation path.
- [ ] Add source evidence.
- [ ] Add root cause.
- [ ] Add fix explanation.
- [ ] Add verification summary.
- [ ] Add remaining risks.

### 4.8 Fix Verification Report

- [ ] Add verification command.
- [ ] Add before status.
- [ ] Add after status.
- [ ] Add tests added.
- [ ] Add test output summary.
- [ ] Add coverage summary if available.
- [ ] Add limitations if full test suite cannot run.
- [ ] Add final verification conclusion.

### 4.9 Phase 4 Review

- [ ] Confirm bug is reproduced.
- [ ] Confirm root cause is verified.
- [ ] Confirm fix is implemented.
- [ ] Confirm tests or checks pass.
- [ ] Confirm before/after evidence is documented.
- [ ] Commit Phase 4 fix and reports.

## Phase 5 - Token Efficiency Measurement

### 5.1 Measurement Setup

- [ ] Define text-unit counting rules.
- [ ] Define token estimation formula.
- [ ] Define iteration counting rules.
- [ ] Define quality rating scale.
- [ ] Create `artifacts/token_measurements/token_comparison.csv`.
- [ ] Create `artifacts/logs/naive_baseline_log.md`.
- [x] Create `artifacts/logs/graph_guided_agent_log.md`.
- [ ] Add measurement method to token report.

### 5.2 Naive Baseline Workflow

- [ ] Define naive workflow prompt or process.
- [ ] Do not use Graphify in naive mode.
- [ ] Do not use Obsidian in naive mode.
- [ ] Select broad source files manually or by folder.
- [ ] Record each file read.
- [ ] Count characters for each file read.
- [ ] Estimate tokens for each file read.
- [ ] Record number of investigation iterations.
- [ ] Record whether root cause was reached.
- [ ] Record whether fix was reached.
- [ ] Record time or step count if available.
- [ ] Record quality of explanation.
- [ ] Save naive baseline log.

### 5.3 Graph-Guided Workflow

- [ ] Define graph-guided workflow prompt or process.
- [ ] Read `graph.json` summary.
- [ ] Read `GRAPH_REPORT.md`.
- [ ] Read `obsidian/index.md`.
- [ ] Read `obsidian/hot.md`.
- [ ] Read selected source files only.
- [ ] Record each text unit read.
- [ ] Count characters for each text unit.
- [ ] Estimate tokens for each text unit.
- [ ] Record number of investigation iterations.
- [ ] Record whether root cause was reached.
- [ ] Record whether fix was reached.
- [ ] Record time or step count if available.
- [ ] Record quality of explanation.
- [ ] Save graph-guided log.

### 5.4 Comparison Table

- [ ] Add baseline row.
- [ ] Add graph-guided row.
- [ ] Add files/text units read.
- [ ] Add input token estimate.
- [ ] Add output token estimate if available.
- [ ] Add total token estimate.
- [ ] Add iterations.
- [ ] Add root-cause status.
- [ ] Add fix status.
- [ ] Add quality rating.
- [ ] Add notes.
- [ ] Calculate percentage token reduction.
- [ ] Calculate file-read reduction.
- [ ] Calculate iteration reduction.

### 5.5 Token Efficiency Report

- [ ] Add report title.
- [ ] Add measurement method.
- [ ] Add baseline description.
- [ ] Add graph-guided description.
- [ ] Add comparison table.
- [ ] Add interpretation.
- [ ] Add limitations.
- [ ] Add conclusion.
- [ ] Link logs.
- [ ] Link CSV.
- [ ] Link from README.
- [ ] Link from Obsidian.

### 5.6 Phase 5 Review

- [ ] Confirm metrics are transparent.
- [ ] Confirm graph-guided workflow is compared fairly.
- [ ] Confirm limitations are honest.
- [ ] Confirm report is linked.
- [ ] Commit Phase 5 artifacts.

## Phase 6 - Original Extension

### 6.1 Extension Selection

- [ ] Confirm selected extension.
- [ ] Document why extension was chosen.
- [ ] Document how extension exceeds minimum requirements.
- [ ] Document how extension supports token efficiency.
- [ ] Document how extension supports reverse engineering.

### 6.2 Suspicious Node Ranking

- [ ] Create `src/analysis/`.
- [ ] Create `src/analysis/__init__.py`.
- [ ] Create `src/analysis/graph_loader.py`.
- [ ] Create `src/analysis/suspicious_nodes.py`.
- [ ] Load `graph.json`.
- [ ] Parse nodes.
- [ ] Parse edges.
- [ ] Compute degree for nodes.
- [ ] Compute inbound degree.
- [ ] Compute outbound degree.
- [ ] Compute keyword score.
- [ ] Compute proximity to bug keywords.
- [ ] Compute proximity to failing test names if possible.
- [ ] Combine scores.
- [ ] Sort suspicious nodes.
- [ ] Output top 5 suspicious nodes.
- [ ] Output top 10 suspicious nodes.
- [ ] Save suspicious node report.
- [ ] Add explanation of scoring method.
- [ ] Add limitations of scoring method.

### 6.3 Dynamic Hot Context Generation

- [ ] Create `src/analysis/hot_md_generator.py`.
- [ ] Read suspicious node report.
- [ ] Read selected bug summary.
- [ ] Read Graphify artifact paths.
- [ ] Read source file references.
- [ ] Generate `hot.md` header.
- [ ] Generate bug summary section.
- [ ] Generate top suspects section.
- [ ] Generate graph evidence section.
- [ ] Generate source files to inspect section.
- [ ] Generate open questions section.
- [ ] Generate links back to index.
- [ ] Write generated output to `obsidian/hot.generated.md`.
- [ ] Decide whether to merge into `obsidian/hot.md`.
- [ ] Document generated file in README.

### 6.4 Optional Git Diff Integration

- [ ] Check whether project is in Git.
- [ ] Capture diff after fix.
- [ ] Save diff to `artifacts/before_after/fix.diff`.
- [ ] Parse changed files.
- [ ] Add changed files to generated hot context.
- [ ] Add impact section to generated hot context.
- [ ] Document diff integration.

### 6.5 Original Extension Report

- [ ] Add extension title.
- [ ] Add motivation.
- [ ] Add inputs.
- [ ] Add algorithm.
- [ ] Add outputs.
- [ ] Add example result.
- [ ] Add how it improves context selection.
- [ ] Add limitations.
- [ ] Add future improvements.

### 6.6 Phase 6 Review

- [ ] Confirm extension artifact exists.
- [ ] Confirm extension is explained in README.
- [ ] Confirm extension connects to EX04 requirements.
- [ ] Confirm extension is not just cosmetic.
- [ ] Commit Phase 6 artifacts.

## Phase 7 - Final README and Submission Packaging

### 7.1 README Repository Choice Section

- [ ] Add selected repository name.
- [ ] Add selected repository URL.
- [ ] Add repository description.
- [ ] Add reason for selection.
- [ ] Add why rejected repositories were not selected.
- [ ] Add why selected repository fits EX04.

### 7.2 README Selected Bug Section

- [ ] Add bug title.
- [ ] Add bug summary.
- [ ] Add expected behavior.
- [ ] Add actual behavior.
- [ ] Add reproduction command.
- [ ] Add affected files.
- [ ] Add link to bug report.

### 7.3 README Research Questions Section

- [ ] List all assignment research questions.
- [ ] Answer each question briefly.
- [ ] Link detailed answers to reports.
- [ ] Link detailed answers to Obsidian notes.

### 7.4 README Quick Start Section

- [ ] Add clone instructions.
- [ ] Add dependency installation command.
- [ ] Add bug reproduction command.
- [ ] Add test command.
- [ ] Add agent workflow command.
- [ ] Add graph generation command if reproducible.
- [ ] Add artifact browsing instructions.

### 7.5 README Project Structure Section

- [ ] Add tree of repository structure.
- [ ] Explain `src/`.
- [ ] Explain `tests/`.
- [ ] Explain `obsidian/`.
- [ ] Explain `reports/`.
- [ ] Explain `artifacts/`.
- [ ] Explain `data/`.
- [ ] Explain `config/` if present.

### 7.6 README Graphify Section

- [ ] Explain Graphify role.
- [ ] Link `graph.json`.
- [ ] Link `GRAPH_REPORT.md`.
- [ ] Link graph visualization if available.
- [ ] Summarize main graph findings.
- [ ] Explain limitations.

### 7.7 README Obsidian Section

- [ ] Explain Obsidian vault role.
- [ ] Link `obsidian/index.md`.
- [ ] Link `obsidian/hot.md`.
- [ ] Explain navigation strategy.
- [ ] Explain how vault changed after fix.

### 7.8 README Architecture Section

- [ ] Embed or link architecture block diagram.
- [ ] Embed or link OOP/module diagram.
- [ ] Summarize main architecture.
- [ ] Summarize central components.
- [ ] Summarize bottlenecks or God nodes.

### 7.9 README Agent Workflow Section

- [ ] Explain chosen framework.
- [ ] Show workflow stages.
- [ ] Link agent workflow report.
- [ ] Link graph-guided agent log.
- [ ] Explain how context was narrowed.

### 7.10 README Bug Investigation Section

- [ ] Summarize investigation path.
- [ ] Summarize root cause.
- [ ] Link bug report.
- [ ] Link hot context.
- [ ] Link source evidence.

### 7.11 README Fix Section

- [ ] Explain code fix.
- [ ] Explain why fix is correct.
- [ ] Link changed files.
- [ ] Link verification report.
- [ ] Include before/after behavior.

### 7.12 README Token Efficiency Section

- [ ] Add comparison table.
- [ ] Add token reduction result.
- [ ] Add file-read reduction result.
- [ ] Add iteration reduction result.
- [ ] Link detailed token report.
- [ ] Explain measurement limitations.

### 7.13 README Original Extension Section

- [ ] Explain extension.
- [ ] Link extension report.
- [ ] Link generated artifacts.
- [ ] Explain value beyond minimum.

### 7.14 README Artifact Index

- [ ] Add report links.
- [ ] Add diagram links.
- [ ] Add Graphify artifact links.
- [ ] Add Obsidian links.
- [ ] Add logs links.
- [ ] Add token measurement links.
- [ ] Add screenshots links.

### 7.15 Final Quality Checks

- [ ] Run tests.
- [ ] Run Ruff.
- [ ] Check coverage if configured.
- [ ] Check no secrets exist.
- [ ] Check `.env` is ignored.
- [ ] Check `.env-example` exists.
- [ ] Check `uv.lock` exists.
- [ ] Check README links.
- [ ] Check Obsidian links.
- [ ] Check diagrams render.
- [ ] Check reports are complete.
- [ ] Check artifact paths are correct.
- [ ] Check line length and formatting.
- [ ] Check final checklist.

### 7.16 Final Submission

- [ ] Commit final changes.
- [ ] Push to GitHub.
- [ ] Verify GitHub renders README.
- [ ] Verify GitHub renders diagrams.
- [ ] Verify all required artifacts are present online.
- [ ] Copy final repository URL.
- [ ] Prepare short submission message.
- [ ] Submit according to course instructions.

## Cross-Phase Research Question Tracking

- [ ] RQ1: Actual architecture answered in README.
- [ ] RQ1: Actual architecture answered in reverse-engineering report.
- [ ] RQ1: Actual architecture represented in architecture diagram.
- [ ] RQ2: Non-obvious discoveries answered in README.
- [ ] RQ2: Non-obvious discoveries answered in reverse-engineering report.
- [ ] RQ3: Central modules/classes/functions answered in README.
- [ ] RQ3: Central modules/classes/functions answered in component notes.
- [ ] RQ4: God nodes and complexity centers answered in report.
- [ ] RQ4: God nodes and complexity centers linked to graph evidence.
- [ ] RQ5: Architectural blocks extraction explained.
- [ ] RQ5: OOP extraction explained.
- [ ] RQ6: Bug identification process explained.
- [ ] RQ7: Root cause explained.
- [ ] RQ8: Investigation steps documented.
- [ ] RQ9: Graphify advantage explained.
- [ ] RQ10: Obsidian advantage explained.
- [ ] RQ11: Agent token savings explained.
- [ ] RQ12: Future improvements proposed.

## Final Deliverable Tracking

- [ ] Full Python solution code exists.
- [ ] Agent workflow implementation exists.
- [ ] Graphify `graph.json` exists.
- [ ] Graphify report exists.
- [ ] Obsidian vault exists.
- [ ] `obsidian/index.md` exists.
- [ ] `obsidian/hot.md` exists.
- [ ] Bug analysis report exists.
- [ ] Root-cause report content complete.
- [ ] Token efficiency report exists.
- [ ] Architecture block diagram exists.
- [ ] OOP/module diagram exists.
- [ ] Before/after proof exists.
- [ ] Original extension documentation exists.
- [ ] README exists.
- [ ] README is complete.
- [ ] Run instructions exist.
- [ ] Test instructions exist.
- [ ] Artifact index exists.

## Professional Submission Guideline Tracking

- [ ] Root README is user-manual quality.
- [ ] Installation instructions exist.
- [ ] Usage instructions exist.
- [ ] Configuration instructions exist.
- [ ] Contribution or development notes exist if useful.
- [ ] License/credits section exists.
- [ ] `docs/PRD.md` exists.
- [ ] `docs/PLAN.md` exists.
- [ ] `docs/TODO.md` exists.
- [ ] Mechanism-specific PRD exists if needed.
- [ ] Project structure is clear.
- [ ] Code files are under 150 lines where feasible.
- [ ] Functions have clear names.
- [ ] Modules have clear names.
- [ ] Comments explain why, not obvious what.
- [ ] Public functions have tests where feasible.
- [ ] TDD evidence is described.
- [ ] Coverage target is documented.
- [ ] Ruff configuration exists.
- [ ] Ruff result is documented.
- [ ] No hardcoded secrets.
- [ ] Config files are separate from code.
- [ ] `.env-example` exists.
- [ ] `.gitignore` protects secrets.
- [ ] `uv` is used for commands.
- [ ] `pyproject.toml` exists.
- [ ] `uv.lock` exists.
- [ ] Git history is meaningful.
- [ ] Prompt log exists if major prompts are used.
- [ ] Cost/token analysis exists.
- [ ] Visualizations exist.
- [ ] UI screenshots included if UI exists.
- [ ] ISO/IEC 25010 quality reflection included if useful.

## Optional Enhancement Backlog

- [ ] Add graph centrality visualization.
- [ ] Add before/after graph diff.
- [ ] Add source-to-Obsidian backlink generator.
- [ ] Add test-to-component traceability matrix.
- [ ] Add agent prompt registry.
- [ ] Add JSON schema for Graphify artifacts.
- [ ] Add automated artifact index generator.
- [ ] Add coverage badge if appropriate.
- [ ] Add Mermaid render screenshots.
- [ ] Add dependency graph.
- [ ] Add module risk score.
- [ ] Add root-cause timeline.
- [ ] Add architecture decision records.
- [ ] Add `docs/ADR_001_repository_choice.md`.
- [ ] Add `docs/ADR_002_agent_framework.md`.
- [ ] Add `docs/ADR_003_original_extension.md`.
- [ ] Add limitations table.
- [ ] Add future work roadmap.

## Completion Notes

- [ ] Record final selected repository.
- [x] Record final selected bug: `print_final_scores` global-state coupling.
- [ ] Record final Graphify command.
- [ ] Record final agent command.
- [ ] Record final test command.
- [ ] Record final token reduction.
- [ ] Record final file-read reduction.
- [ ] Record final iteration reduction.
- [ ] Record final original extension.
- [ ] Record final submission URL.
