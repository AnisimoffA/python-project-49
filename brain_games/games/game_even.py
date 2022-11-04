from random import randint


def even_game():
    number = randint(1, 6)

    TASK = f"Answer \"yes\" if the number is even, otherwise answer \"no\"."
    input_line = f"Question: {number}"

    if is_even(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return TASK, input_line, right_answer


def is_even(num):
    return num % 2 == 0
