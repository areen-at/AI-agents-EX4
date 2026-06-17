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

- [ ] Open `soarsmu/BugsInPy`.
- [ ] Review BugsInPy setup difficulty.
- [ ] Review BugsInPy available bugs.
- [ ] Estimate BugsInPy environment cost.
- [ ] Open `martinpeck/broken-python`.
- [ ] Review broken-python repository size.
- [ ] Review broken-python bug examples.
- [ ] Estimate whether broken-python has enough structure for diagrams.
- [ ] Open `andela/buggy-python`.
- [ ] Review buggy-python repository size.
- [ ] Review buggy-python bug examples.
- [ ] Estimate whether buggy-python has enough structure for diagrams.
- [ ] Record candidate repository pros and cons.
- [ ] Compare candidates against assignment requirements.
- [ ] Compare candidates against available time.
- [ ] Compare candidates against environment complexity.
- [ ] Compare candidates against diagram potential.
- [ ] Compare candidates against testability.
- [ ] Choose the final repository.
- [ ] Document the selected repository in README.
- [ ] Document rejected alternatives in README or report.
- [ ] Explain why selected repository fits EX04.
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
- [ ] Choose one backup bug.
- [ ] Record the selected bug in README.
- [ ] Record the selected bug in `obsidian/hot.md`.
- [ ] Record the selected bug in `reports/bug_analysis_report.md`.
- [ ] Define initial expected behavior.
- [ ] Define initial actual behavior.
- [ ] Define initial reproduction command.
- [ ] Define initial verification command.
- [ ] Capture any failing output.
- [ ] Save failing output to `artifacts/logs/`.
- [ ] Record bug selection rationale.

### 0.5 Documentation Baseline

- [ ] Copy or create `docs/PRD.md` from project PRD.
- [ ] Copy or create `docs/PLAN.md` from project plan.
- [ ] Create `docs/TODO.md` from this checklist.
- [ ] Add initial README title.
- [ ] Add README assignment summary.
- [ ] Add README repository choice section.
- [ ] Add README selected bug section.
- [ ] Add README quick-start placeholder.
- [ ] Add README project structure placeholder.
- [ ] Add README artifact index placeholder.
- [ ] Add README limitations placeholder.
- [ ] Add README final conclusion placeholder.
- [ ] Add report index to `obsidian/index.md`.
- [ ] Add artifact index to `obsidian/index.md`.
- [ ] Add research questions to `reports/reverse_engineering_report.md`.
- [ ] Add research questions to README.
- [ ] Add final checklist to `reports/final_submission_checklist.md`.

### 0.6 Phase 0 Review

- [ ] Confirm project scope is small enough.
- [ ] Confirm repository choice is justified.
- [ ] Confirm selected bug is feasible.
- [ ] Confirm all required directories exist.
- [ ] Confirm `uv` commands work.
- [ ] Confirm initial docs exist.
- [ ] Commit Phase 0 setup.

## Phase 1 - Graphify and Initial Knowledge Base

### 1.1 Graphify Preparation

- [ ] Install or locate Graphify.
- [ ] Read Graphify usage instructions.
- [ ] Identify Graphify input path.
- [ ] Identify Graphify output path.
- [ ] Decide whether to run Graphify on full repo or selected subdirectory.
- [ ] Exclude irrelevant folders if needed.
- [ ] Exclude virtual environments.
- [ ] Exclude build artifacts.
- [ ] Exclude cache directories.
- [ ] Exclude `.git`.
- [ ] Exclude generated report directories if needed.
- [ ] Record the exact Graphify command.
- [ ] Add Graphify command to README.
- [ ] Add Graphify command to `reports/reverse_engineering_report.md`.
- [ ] Add Graphify command to `obsidian/index.md`.

### 1.2 Graphify Execution

- [ ] Run Graphify on selected codebase.
- [ ] Save `graph.json` to `artifacts/graphify/graph.json`.
- [ ] Save `GRAPH_REPORT.md` to `artifacts/graphify/GRAPH_REPORT.md`.
- [ ] Save any `graph.html` output to `artifacts/graphify/`.
- [ ] Save any image output to `artifacts/graphify/`.
- [ ] Save Graphify console logs to `artifacts/logs/graphify_run.md`.
- [ ] Verify `graph.json` is valid JSON.
- [ ] Verify `graph.json` contains nodes.
- [ ] Verify `graph.json` contains edges.
- [ ] Verify `GRAPH_REPORT.md` is readable.
- [ ] Record total node count.
- [ ] Record total edge count.
- [ ] Record graph generation date.
- [ ] Record Graphify limitations.
- [ ] Record any parse failures.
- [ ] Record unsupported files.
- [ ] Record any missing semantic links.

### 1.3 Graph Artifact Inspection

- [ ] Identify top-level files represented in graph.
- [ ] Identify main modules represented in graph.
- [ ] Identify functions represented in graph.
- [ ] Identify classes represented in graph.
- [ ] Identify import edges.
- [ ] Identify call edges.
- [ ] Identify semantic or inferred edges if available.
- [ ] Identify ambiguous edges if available.
- [ ] Identify high-degree nodes.
- [ ] Identify possible hubs.
- [ ] Identify possible God nodes.
- [ ] Identify isolated nodes.
- [ ] Identify isolated clusters.
- [ ] Identify communities if available.
- [ ] Identify bridge nodes if available.
- [ ] Identify paths related to selected bug.
- [ ] Identify nodes related to failing tests.
- [ ] Identify nodes related to bug keywords.
- [ ] Record initial graph observations in `reports/reverse_engineering_report.md`.
- [ ] Record initial graph observations in `obsidian/architecture.md`.
- [ ] Record initial graph observations in `obsidian/hot.md`.

### 1.4 Obsidian Vault Setup

- [ ] Add title to `obsidian/index.md`.
- [ ] Add project overview to `obsidian/index.md`.
- [ ] Add source repository link to `obsidian/index.md`.
- [ ] Add selected bug summary to `obsidian/index.md`.
- [ ] Add navigation links to `obsidian/index.md`.
- [ ] Link `[[hot]]` from `index.md`.
- [ ] Link `[[architecture]]` from `index.md`.
- [ ] Link `[[components]]` from `index.md`.
- [ ] Link `[[bug_investigation]]` from `index.md`.
- [ ] Link `[[tests_and_verification]]` from `index.md`.
- [ ] Link `[[token_efficiency]]` from `index.md`.
- [ ] Link `[[original_extension]]` from `index.md`.
- [ ] Add Graphify artifact references to `index.md`.
- [ ] Add report references to `index.md`.
- [ ] Add diagram references to `index.md`.
- [ ] Add open questions section to `index.md`.
- [ ] Add current investigation status to `index.md`.

### 1.5 Hot Context Setup

- [ ] Add title to `obsidian/hot.md`.
- [ ] Add selected bug summary.
- [ ] Add expected behavior.
- [ ] Add actual behavior.
- [ ] Add reproduction command.
- [ ] Add failing output summary.
- [ ] Add suspected files section.
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
- [ ] Link bug-critical components to `hot.md`.
- [ ] Link central components to `architecture.md`.

### 1.7 Phase 1 Review

- [ ] Confirm Graphify artifacts exist.
- [ ] Confirm Obsidian vault is navigable.
- [ ] Confirm `index.md` is useful as entry point.
- [ ] Confirm `hot.md` narrows bug context.
- [ ] Confirm graph observations are documented.
- [ ] Commit Phase 1 artifacts.

## Phase 2 - Reverse Engineering

### 2.1 Macro Architecture Reading

- [ ] Identify project entry point.
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
- [ ] Identify bug-critical execution path.
- [ ] Document macro architecture in `obsidian/architecture.md`.
- [ ] Document macro architecture in `reports/reverse_engineering_report.md`.

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
- [ ] Identify possible bottlenecks.
- [ ] Document community findings.
- [ ] Add community notes to Obsidian.

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

- [ ] Answer what the actual architecture is.
- [ ] Answer what was not obvious from first glance.
- [ ] Answer which modules are most central.
- [ ] Answer which classes are most central.
- [ ] Answer which functions are most central.
- [ ] Answer where complexity centers exist.
- [ ] Answer where mixed responsibilities exist.
- [ ] Answer whether God nodes exist.
- [ ] Answer how architecture can be extracted from code.
- [ ] Answer how OOP structure can be extracted.
- [ ] Answer how Graphify helped.
- [ ] Answer how Obsidian helped.
- [ ] Answer where documentation was missing or misleading.

### 2.5 Architecture Block Diagram

- [ ] Decide diagram format.
- [ ] Use Mermaid if possible.
- [ ] Create `artifacts/diagrams/architecture_block_diagram.md`.
- [ ] Add system boundary.
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
- [ ] Add diagram explanation below Mermaid.
- [ ] Link diagram from README.
- [ ] Link diagram from `obsidian/architecture.md`.
- [ ] Link diagram from reverse-engineering report.

### 2.6 OOP or Module Diagram

- [ ] Determine whether target project has classes.
- [ ] If classes exist, identify all relevant classes.
- [ ] If classes exist, identify inheritance.
- [ ] If classes exist, identify composition.
- [ ] If classes exist, identify important method calls.
- [ ] If classes exist, identify wrappers/adapters.
- [ ] If classes do not exist, document procedural design.
- [ ] If classes do not exist, create module/function interaction diagram.
- [ ] Create `artifacts/diagrams/oop_diagram.md`.
- [ ] Add Mermaid class diagram if applicable.
- [ ] Add explanation of diagram.
- [ ] Link diagram from README.
- [ ] Link diagram from `obsidian/architecture.md`.
- [ ] Link diagram from reverse-engineering report.

### 2.7 Reverse Engineering Report

- [ ] Add report title.
- [ ] Add repository overview.
- [ ] Add selected bug overview.
- [ ] Add Graphify method.
- [ ] Add graph findings.
- [ ] Add architecture findings.
- [ ] Add component table.
- [ ] Add central node table.
- [ ] Add suspected bottleneck table.
- [ ] Add community analysis.
- [ ] Add source verification notes.
- [ ] Add architecture diagram link.
- [ ] Add OOP diagram link.
- [ ] Add open questions.
- [ ] Add limitations.
- [ ] Add conclusion.

### 2.8 Phase 2 Review

- [ ] Confirm architecture is understood.
- [ ] Confirm diagrams are complete.
- [ ] Confirm report answers research questions.
- [ ] Confirm Graphify claims are source-verified where important.
- [ ] Commit Phase 2 artifacts.

## Phase 3 - Agent Workflow

### 3.1 Agent Framework Setup

- [ ] Confirm LangGraph or CrewAI choice.
- [ ] Document framework choice in README.
- [ ] Add framework dependency with `uv`.
- [ ] Create `src/agent/`.
- [ ] Create `src/agent/__init__.py`.
- [ ] Create `src/agent/state.py`.
- [ ] Create `src/agent/tools.py`.
- [ ] Create `src/agent/workflow.py`.
- [ ] Create `src/agent/prompts.py` if needed.
- [ ] Create `src/agent/run_agent.py` if needed.
- [ ] Create tests for agent helper functions if feasible.
- [ ] Add agent run command to README.

### 3.2 Agent State Design

- [ ] Define investigation state fields.
- [ ] Add bug summary field.
- [ ] Add graph artifacts field.
- [ ] Add Obsidian context field.
- [ ] Add suspect nodes field.
- [ ] Add selected files field.
- [ ] Add evidence field.
- [ ] Add hypotheses field.
- [ ] Add proposed fix field.
- [ ] Add verification result field.
- [ ] Add token estimate field.
- [ ] Add file read log field.
- [ ] Add iteration count field.
- [ ] Add final report field.
- [ ] Document state schema in `reports/agent_workflow_report.md`.

### 3.3 Agent Tools

- [ ] Implement graph JSON loader.
- [ ] Implement Graphify report reader.
- [ ] Implement Obsidian note reader.
- [ ] Implement source file reader.
- [ ] Implement safe snippet extractor.
- [ ] Implement file-read logger.
- [ ] Implement character counter.
- [ ] Implement token estimator.
- [ ] Implement suspect node ranker or adapter.
- [ ] Implement report writer.
- [ ] Implement command runner for tests if safe.
- [ ] Ensure tools do not read entire repo by default.
- [ ] Ensure tools reject broad glob requests unless explicitly allowed.

### 3.4 Workflow Nodes

- [ ] Implement `LoadGraphContext`.
- [ ] Implement `LoadObsidianContext`.
- [ ] Implement `SelectSuspects`.
- [ ] Implement `ReadFocusedCode`.
- [ ] Implement `HypothesizeRootCause`.
- [ ] Implement `PlanFix`.
- [ ] Implement `VerifyFix`.
- [ ] Implement `WriteInvestigationLog`.
- [ ] Add workflow edges.
- [ ] Add stop condition.
- [ ] Add error handling.
- [ ] Add logging for each node.
- [ ] Add text-unit count for each node.
- [ ] Add token estimate for each node.

### 3.5 Agent Prompts

- [ ] Write system prompt for graph-guided behavior.
- [ ] Write prompt requiring `index.md` before source code.
- [ ] Write prompt requiring `hot.md` before source code.
- [ ] Write prompt requiring evidence labels.
- [ ] Write prompt requiring hypothesis/fact separation.
- [ ] Write prompt requiring minimal file reads.
- [ ] Write prompt requiring root-cause explanation.
- [ ] Write prompt requiring fix plan.
- [ ] Write prompt requiring verification plan.
- [ ] Save prompts in `src/agent/prompts.py` or report.
- [ ] Document prompts in prompt log.

### 3.6 Agent Execution

- [ ] Run graph-guided agent once.
- [ ] Save raw run log.
- [ ] Save selected suspect nodes.
- [ ] Save selected files.
- [ ] Save agent hypotheses.
- [ ] Save agent proposed fix.
- [ ] Save agent token estimates.
- [ ] Save agent iteration count.
- [ ] Update `artifacts/logs/graph_guided_agent_log.md`.
- [ ] Update `reports/agent_workflow_report.md`.
- [ ] Update `obsidian/bug_investigation.md`.
- [ ] Update `obsidian/hot.md`.

### 3.7 Agent Workflow Report

- [ ] Add framework choice explanation.
- [ ] Add workflow diagram.
- [ ] Add node descriptions.
- [ ] Add state schema.
- [ ] Add context narrowing strategy.
- [ ] Add graph-first proof.
- [ ] Add file-read log.
- [ ] Add token estimate.
- [ ] Add agent limitations.
- [ ] Add future improvements.

### 3.8 Phase 3 Review

- [ ] Confirm agent reads graph/Obsidian before source.
- [ ] Confirm agent does not read all files.
- [ ] Confirm workflow is reproducible.
- [ ] Confirm logs are saved.
- [ ] Commit Phase 3 artifacts.

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
- [ ] Create `artifacts/logs/graph_guided_agent_log.md`.
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
- [ ] Record final selected bug.
- [ ] Record final Graphify command.
- [ ] Record final agent command.
- [ ] Record final test command.
- [ ] Record final token reduction.
- [ ] Record final file-read reduction.
- [ ] Record final iteration reduction.
- [ ] Record final original extension.
- [ ] Record final submission URL.

