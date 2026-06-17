# OOP / Module Interaction Diagram

Status: Phase 2 draft.

## OOP Applicability

The selected `mathsquiz` subsystem does not define classes. A traditional OOP diagram is therefore not applicable. The appropriate substitute is a functional/module interaction diagram that shows the procedural blocks, functions, state variables, and call relationships.

```mermaid
classDiagram
    class "mathsquiz-step2.py" {
        module global score
        welcome_message()
        ask_question(first_number, second_number)
        print_final_scores(final_score)
    }

    class "mathsquiz-step3.py" {
        import random
        module global score
        module global number_of_questions
        welcome_message()
        ask_question(first_number, second_number)
        print_final_scores(final_score, max_possible_score)
    }

    class "ask_question()" {
        input answer
        compute correct answer
        return points_awarded
    }

    class "print_final_scores()" {
        accept final_score
        print score summary
        print feedback
        BUG reads global score
    }

    "mathsquiz-step2.py" --> "ask_question()" : calls 10 fixed times
    "mathsquiz-step2.py" --> "print_final_scores()" : passes score
    "mathsquiz-step3.py" --> "ask_question()" : calls in loop
    "mathsquiz-step3.py" --> "print_final_scores()" : passes score and max
    "print_final_scores()" ..> "mathsquiz-step2.py" : hidden global score dependency
    "print_final_scores()" ..> "mathsquiz-step3.py" : hidden global score dependency
```

## Important Difference Between Step2 and Step3

| Version | Question Selection | Score Reporting | Bug Shape |
|---|---|---|---|
| `mathsquiz-step2.py` | Ten fixed multiplication questions | Prints out of 10 | `final_score` ignored; global `score` printed and used for thresholds |
| `mathsquiz-step3.py` | Random questions in a loop | Prints out of `max_possible_score` and calculates percentage | `final_score` ignored; global `score` printed and used for percentage |

## Design Insight

The subsystem looks modular because behavior is split into functions. The graph and source evidence show that the modular boundary is incomplete: `print_final_scores(...)` still depends on ambient module state.
