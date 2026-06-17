# Component Notes

## Main Components

- `welcome_message`: displays introduction text.
- `ask_question`: asks one multiplication question, parses answer, returns 1 or 0.
- `print_final_scores`: displays score and feedback; official bug target because it reads global `score` instead of using its explicit parameter.
- Module-level quiz flow: initializes score, asks questions, accumulates score, prints final result.

## Central Nodes

From Phase 1 graph metrics:

- `call:print` - highest degree callable-reference node.
- `mathsquiz-step1.py` - high-degree file due to repeated linear question blocks.
- `mathsquiz-step2.py` and `mathsquiz-step3.py` - functional versions with central `print_final_scores`.
- `call:input` and `call:int` - important user-input path.
- `call:ask_question` - repeated quiz question execution.

## Possible Bottlenecks

- `print_final_scores`: final feedback incorrectly depends on hidden global score state.
- `ask_question`: central point for input parsing and answer correctness.
- Global `score`: hidden dependency risk in step2/step3.
