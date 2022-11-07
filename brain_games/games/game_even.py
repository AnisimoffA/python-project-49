from random import randint


TASK = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def start_game():
    number = randint(1, 6)
    input_line = f"Question: {number}"

    if is_even(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return input_line, right_answer


def is_even(num):
    return num % 2 == 0
