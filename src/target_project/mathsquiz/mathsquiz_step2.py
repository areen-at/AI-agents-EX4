"""Fixed importable version of broken-python mathsquiz-step2.py."""

score = 0


def welcome_message() -> None:
    print("Hello! I'm going to ask you 10 maths questions.")
    print("Let's see how many you can get right!")


def ask_question(first_number: int, second_number: int) -> int:
    print("What is", first_number, "x", second_number)
    answer = input("Answer: ")
    if int(answer) == first_number * second_number:
        print("Correct!")
        points_awarded = 1
    else:
        print("Wrong!")
        points_awarded = 0

    print("")
    return points_awarded


def print_final_scores(final_score: int) -> None:
    print("That's all the questions done. So...what was your score...?")
    print("You scored", final_score, "points out of a possible 10.")
    if final_score < 5:
        print("You need to practice your maths!")
    elif final_score < 8:
        print("That's pretty good!")
    elif final_score < 10:
        print("You did really well! Try and get 10 out of 10 next time!")
    elif final_score == 10:
        print("Wow! What a maths star you are!! I'm impressed!")
