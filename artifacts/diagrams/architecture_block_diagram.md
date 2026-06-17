# Architecture Block Diagram

Status: Phase 2 draft.

```mermaid
flowchart TD
    Repo["martinpeck/broken-python"]
    Subsystem["mathsquiz subsystem"]
    Baseline["mathsquiz.py<br/>broken baseline"]
    Step1["mathsquiz-step1.py<br/>linear repaired script"]
    Step2["mathsquiz-step2.py<br/>functional refactor"]
    Step3["mathsquiz-step3.py<br/>randomized functional quiz"]

    Repo --> Subsystem
    Subsystem --> Baseline
    Subsystem --> Step1
    Subsystem --> Step2
    Subsystem --> Step3

    Step2 --> Step2Welcome["welcome_message()"]
    Step2 --> Step2Ask["ask_question(first_number, second_number)"]
    Step2 --> Step2Score["module global score"]
    Step2 --> Step2Final["print_final_scores(final_score)"]

    Step3 --> Random["random.randint"]
    Step3 --> Loop["for question loop"]
    Loop --> Step3Ask["ask_question(first_number, second_number)"]
    Step3Ask --> Step3Score["module global score"]
    Step3Score --> Step3Final["print_final_scores(final_score, max_possible_score)"]

    Step2Ask --> Input["input() and int()"]
    Step3Ask --> Input
    Step2Ask --> Points["points_awarded"]
    Step3Ask --> Points
    Points --> Step2Score
    Points --> Step3Score

    Step2Score --> Step2Final
    Step3Score --> Step3Final

    Step2Final -. "bug: reads global score" .-> Step2Score
    Step3Final -. "bug: reads global score" .-> Step3Score

    Step2Final --> Output["score output and feedback"]
    Step3Final --> Output
```

## Interpretation

The architecture is procedural. `mathsquiz-step2.py` and `mathsquiz-step3.py` introduce functions, but the module-level script flow still owns execution order and score state.

The selected bug sits at the boundary between score accumulation and final reporting. `print_final_scores(...)` appears to receive the final score as an explicit argument, but internally it reaches back to the module-level `score` variable.

## Bug-Critical Path

```text
module-level quiz flow
-> ask_question(...)
-> points_awarded
-> global score accumulation
-> print_final_scores(final_score, ...)
-> hidden read of global score
```
