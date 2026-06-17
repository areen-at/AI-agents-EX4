# Reverse Engineering Report

Status: Phase 2 complete enough to enter Phase 3.

## Scope

Selected repository: `martinpeck/broken-python`

Selected subsystem: `mathsquiz`

Analyzed files:

- `mathsquiz/mathsquiz.py`
- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`

## Graph Generation

Graphify executable was not available locally. Phase 1 therefore generated Graphify-style artifacts using a local AST/static-analysis workflow.

Generation log:

- `artifacts/logs/graphify_run.md`

Artifacts:

- `artifacts/graphify/graph.json`
- `artifacts/graphify/GRAPH_REPORT.md`
- `artifacts/graphify/graph_metrics.json`
- `artifacts/graphify/graph.html`

## Graph Totals

- Nodes: 47
- Edges: 153
- Files: 4
- Functions: 6
- Bug risks: 14
- Syntax errors: 1

## Initial Architecture Understanding

`mathsquiz` evolves from a broken linear script into a more modular quiz implementation:

1. `mathsquiz.py`: baseline with syntax and logic defects.
2. `mathsquiz-step1.py`: repaired linear version with repeated question blocks.
3. `mathsquiz-step2.py`: functional refactor with `welcome_message`, `ask_question`, and `print_final_scores`.
4. `mathsquiz-step3.py`: randomized question generation and percentage-based feedback.

## Phase 2 Architecture Findings

### Entry Points

Each `mathsquiz` file is a standalone script. There is no package-level application entry point and no class-based framework.

The most relevant executable flows are:

- `mathsquiz-step2.py`: fixed sequence of ten calls to `ask_question(...)`, followed by `print_final_scores(score)`.
- `mathsquiz-step3.py`: loop over `number_of_questions`, random number generation through `random.randint`, score accumulation, then `print_final_scores(score, number_of_questions)`.

### Main Responsibilities

| Responsibility | Component | Notes |
|---|---|---|
| Greeting/output setup | `welcome_message()` | Presentation-only function |
| Ask one question | `ask_question(...)` | Handles prompt, input parsing, correctness check, and point return |
| Score ownership | module-level `score` | Accumulated in script flow, not encapsulated |
| Final reporting | `print_final_scores(...)` | Should be presentation-only, but reads hidden global state |
| Random question selection | `mathsquiz-step3.py` module flow | Uses `random.randint` before each `ask_question(...)` call |

### Central Nodes

Graph metrics identify these important nodes:

- `call:print`: degree 73, reflecting the output-heavy procedural style.
- `mathsquiz-step1.py`: degree 72, because the linear script repeats question/output logic.
- `mathsquiz-step2.py` and `mathsquiz-step3.py`: degree 20 each, the primary functional versions.
- `call:ask_question`: degree 11, the repeated question-execution path.
- `function:...:print_final_scores`: degree 9 in both step2 and step3, the selected bug-critical function.

### Bottlenecks and Mixed Responsibilities

`ask_question(...)` is a behavioral bottleneck because it combines user prompting, numeric parsing, answer validation, feedback printing, and return-value generation.

`print_final_scores(...)` is the selected architecture bottleneck because it appears to be a pure reporting function but reads module-level `score`. This mixes presentation with external score state and weakens the function boundary.

The module-level script flow is another implicit coordination point: it owns score initialization, score accumulation, call order, and final reporting.

### OOP Assessment

The subsystem has no classes, inheritance, composition, or object lifecycle. A class diagram would be artificial. The project therefore provides a module/function interaction diagram instead of a traditional OOP diagram.

Diagram files:

- `artifacts/diagrams/architecture_block_diagram.md`
- `artifacts/diagrams/oop_diagram.md`
- `artifacts/diagrams/score_state_flow_diagram.md`

### Missing View Found During Review

The first two diagrams covered subsystem structure and module/function relationships, but they did not isolate the state-flow bug tightly enough. Phase 2 therefore adds `score_state_flow_diagram.md`.

That diagram shows:

- Intended path: accumulated `score` is passed into the `final_score` parameter.
- Actual path: `print_final_scores(...)` reads global `score`.
- Fix implication: remove the hidden global-state edge and use the explicit parameter path.

## Source Verification Notes

| Claim | Verification |
|---|---|
| `mathsquiz-step2.py` is functional but still script-driven | Source defines `welcome_message`, `ask_question`, and `print_final_scores`, then executes module-level calls directly. |
| `mathsquiz-step2.py` uses fixed questions | Source has ten explicit `score = score + ask_question(...)` calls. |
| `mathsquiz-step3.py` adds random question generation | Source imports `random`, loops over `number_of_questions`, and calls `random.randint(2,12)`. |
| `print_final_scores` is bug-critical in step2 | Source passes `final_score` but prints and branches using global `score`. |
| `print_final_scores` is bug-critical in step3 | Source passes `final_score` and `max_possible_score` but prints `score` and computes percentage from `score`. |
| No OOP structure exists | No classes are defined in the selected `mathsquiz` files. |

## Phase 2 Research Answers

1. Actual architecture: procedural scripts that evolve toward functions, with module-level orchestration still controlling state and execution.
2. Non-obvious finding: the code looks modular after step2, but `print_final_scores(...)` is still coupled to global state.
3. Central modules/functions: `mathsquiz-step2.py`, `mathsquiz-step3.py`, `ask_question(...)`, and `print_final_scores(...)`.
4. Complexity centers: repeated output/input operations, `ask_question(...)` mixed responsibilities, module-level `score`, and final-score reporting.
5. God nodes: no single class or object is a God object; the closest procedural hub is module-level script flow plus the high-degree `print` callable.
6. Architecture extraction method: combine graph centrality, file/function nodes, state-variable nodes, and source verification.
7. OOP extraction method: check for classes first; because none exist, substitute a module/function interaction diagram.
8. Graphify value: it highlighted `print_final_scores` as a repeated bug-risk pattern across both functional versions and kept attention away from broad baseline noise.

## Limitations

- The graph is Graphify-style static analysis because the official executable was unavailable.
- The codebase is small under the general assignment threshold, but this repository is documented as lecturer-approved.
- Phase 2 diagrams describe current architecture before the Phase 4 fix. If the fix changes structure, diagrams should be updated.

## Open Questions for Later Phases

- Should Phase 4 fix both step2 and step3, or use one as the primary fixed artifact and the other as comparative evidence?
- Should `ask_question(...)` input validation become the original extension or remain a documented secondary risk?
- Should the agent workflow rank `print_final_scores` using graph degree, bug-risk labels, or proximity to score-state nodes?

## Phase 2 Conclusion

The Phase 2 architecture work confirms that the selected bug is not isolated trivia. It is a boundary failure inside the subsystem's main data flow: score is accumulated in module-level orchestration, then passed into a reporting function that secretly ignores the explicit argument. The next phase should build the agent workflow around this narrow, graph-supported path.

See also:

- `reports/phase2_architecture_review.md`
- `artifacts/diagrams/agent_workflow_diagram.md`

## Initial Bug-Risk Findings

- Official target: hidden state coupling in `print_final_scores` in `mathsquiz-step2.py` and `mathsquiz-step3.py`.
- Background candidate: baseline syntax and logic defects in `mathsquiz.py`.
- Background candidate: possible input-conversion crash path through unguarded `int(answer)`.

## Official Bug-Critical Path

```text
module-level quiz flow
-> ask_question(...)
-> score accumulation
-> print_final_scores(final_score, ...)
-> hidden read of global score
-> incorrect or non-isolated final-score output
```

## Next Reverse-Engineering Tasks

- Extend the Phase 2 diagrams if the fix changes structure.
- Prepare Phase 3 agent workflow so it starts from `index.md`, `hot.md`, and the graph report before raw source.
