"""Fixed importable version of broken-python mathsquiz-step3.py."""

import random

score = 0
number_of_questions = 10


def welcome_message() -> None:
    print("Hello! I'm going to ask you 10 maths questions.")
    print("Let's see how many you can get right!")


def ask_question(first_number: int, second_number: int) -> int:
    print("What is", first_number, "x", second_number)
    answer = input("Answer: ")

    correct_answer = first_number * second_number

    if int(answer) == correct_answer:
        print("Correct!")
        points_awarded = 1
    else:
        print("Wrong! The correct answer was", correct_answer)
        points_awarded = 0

    print("")
    return points_awarded


def random_question_score() -> int:
    first_number = random.randint(2, 12)
    second_number = random.randint(2, 12)
    return ask_question(first_number, second_number)


def print_final_scores(final_score: int, max_possible_score: int) -> None:
    print("That's all the questions done. So...what was your score...?")
    print("You scored", final_score, "points out of a possible", max_possible_score)

    percentage = (final_score / max_possible_score) * 100

    if percentage < 50:
        print("You need to practice your maths!")
    elif percentage < 80:
        print("That's pretty good!")
    elif percentage < 100:
        print("You did really well! Try and get 10 out of 10 next time!")
    elif percentage == 100:
        print("Wow! What a maths star you are!! I'm impressed!")
