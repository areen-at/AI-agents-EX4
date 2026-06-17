# Phase 2 Architecture Review

Status: complete enough to enter Phase 3 after adding the missing score-state flow view.

## Diagram 1: Architecture Block Diagram

File: `artifacts/diagrams/architecture_block_diagram.md`

What it shows:

- The selected repository and `mathsquiz` subsystem boundary.
- The evolution from `mathsquiz.py` baseline to `mathsquiz-step1.py`, `mathsquiz-step2.py`, and `mathsquiz-step3.py`.
- The main execution blocks in step2 and step3: greeting, question asking, score state, final reporting, output, and random number generation in step3.

How it relates to the bug:

- It places `print_final_scores(...)` at the end of the quiz control flow.
- It shows that score is accumulated before final reporting.
- It marks the hidden dependency from `print_final_scores(...)` back to global `score`.

Assessment:

- Complete as the high-level block diagram.
- Good for explaining subsystem boundaries, entry points, and the bug-critical path.

## Diagram 2: OOP / Module Interaction Diagram

File: `artifacts/diagrams/oop_diagram.md`

What it shows:

- Why a traditional OOP diagram is not applicable: the subsystem has no classes.
- The substitute module/function view for `mathsquiz-step2.py` and `mathsquiz-step3.py`.
- The functions, module state, and call relationships that matter to the investigation.

How it relates to the bug:

- It shows that `print_final_scores(...)` is presented as a function interface.
- It shows the mismatch between the interface and the implementation: the function accepts `final_score` but depends on module-level score state.
- It makes clear that the bug exists in both functional versions.

Assessment:

- Complete as the OOP substitute required by the assignment.
- Strong because it explicitly explains why no class diagram is possible.

## Diagram 3: Score State Flow Diagram

File: `artifacts/diagrams/score_state_flow_diagram.md`

What it shows:

- The intended data flow from `score` accumulation to the `final_score` parameter.
- The actual hidden state flow from module-level `score` into `print_final_scores(...)`.
- The exact architectural edge that should be removed in Phase 4.

How it relates to the bug:

- This is the most bug-focused architecture view.
- It shows the parameter contract being bypassed.
- It explains why the Phase 1 probe prints `0` even when non-zero `final_score` values are passed.

Assessment:

- Added because the first two diagrams were structurally complete but did not isolate the state-flow defect enough.
- Completes the architecture view needed before Phase 3.

## Missing Architectural Views

No blocking Phase 2 views remain.

Optional later views:

- Before/after fix diagram after Phase 4.
- Agent workflow diagram in Phase 3.
- Token-efficiency context-selection diagram in Phase 5.

## Phase 2 Verdict

Phase 2 is complete enough to move to Phase 3.

The architecture documentation now includes:

- High-level system/subsystem block view.
- OOP/module interaction substitute.
- Bug-specific score-state data-flow view.
- Reverse-engineering report with central nodes, bottlenecks, source verification, limitations, and research answers.
