from random import randint
import prompt


def even_game():
    number = randint(1, 6)
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    answer = prompt.string(f"Question: {number}\n")
    print("Your answer: ", answer)

    if is_even(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return str(answer), str(right_answer)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
