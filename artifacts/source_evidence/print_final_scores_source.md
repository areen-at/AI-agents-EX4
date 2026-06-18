# print_final_scores Source Evidence

Status: focused source evidence for Phase 3.

## Scope

This file captures only the source snippets needed for the selected `print_final_scores` global-state bug.

## `mathsquiz-step2.py`

Function:

```python
def print_final_scores(final_score):
    print("That's all the questions done. So...what was your score...?")
    print("You scored", score, "points out of a possible 10.")
    if score < 5:
        print("You need to practice your maths!")
    elif score < 8:
        print("That's pretty good!")
    elif score < 10:
        print("You did really well! Try and get 10 out of 10 next time!")
    elif score == 10:
        print("Wow! What a maths star you are!! I'm impressed!")
```

Call site:

```python
print_final_scores(score)
```

Evidence:

- The caller passes `score` as `final_score`.
- The function body ignores `final_score`.
- The function body prints and branches on global `score`.

## `mathsquiz-step3.py`

Function:

```python
def print_final_scores(final_score, max_possible_score):

    print("That's all the questions done. So...what was your score...?")
    print("You scored", score, "points out of a possible", max_possible_score)

    percentage = (score/max_possible_score)*100

    if percentage < 50:
        print("You need to practice your maths!")
    elif percentage < 80:
        print("That's pretty good!")
    elif percentage < 100:
        print("You did really well! Try and get 10 out of 10 next time!")
    elif percentage == 100:
        print("Wow! What a maths star you are!! I'm impressed!")
```

Call site:

```python
print_final_scores(score, number_of_questions)
```

Evidence:

- The caller passes `score` as `final_score`.
- The function body ignores `final_score`.
- The function body prints global `score`.
- The function body calculates `percentage` from global `score`.

## Expected Fix Direction

- Step2: use `final_score` for printed score and threshold checks.
- Step3: use `final_score` for printed score and percentage calculation.
