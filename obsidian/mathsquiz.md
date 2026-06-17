# Mathsquiz Subsystem

## Status

Selected as the primary EX04 investigation subsystem.

## Source Files

- `mathsquiz/mathsquiz-step1.py`
- `mathsquiz/mathsquiz-step2.py`
- `mathsquiz/mathsquiz-step3.py`
- `mathsquiz/mathsquiz.py`

## Why This Subsystem

- It contains several related scripts that show an evolving quiz program.
- It has enough behavior to support root-cause investigation: random question generation, input parsing, answer validation, score state, and loop control.
- It is compact enough for a complete investigation while still allowing Graphify and Obsidian to demonstrate focused navigation.
- It is more suitable than `polygons` as the primary path because it includes interactive stateful behavior.

## Initial Investigation Questions

- Which script contains the best bug candidate for a reproducible before/after fix?
- How do the step files relate to the final `mathsquiz.py`?
- Which functions or blocks are central to quiz flow?
- Where does user input enter the system?
- Where is the answer checked?
- Where is score state updated?

## Links

- [[index]]
- [[hot]]
- [[bug_investigation]]
- [[tests_and_verification]]

