from random import randint


def even_game():
    number = randint(1, 6)

    CONDITION = f"""Answer \"yes\" if the number is even, otherwise answer \"no\".\nQuestion: {number}"""

    if is_even(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return CONDITION, right_answer


def is_even(num):
    return num % 2 == 0
