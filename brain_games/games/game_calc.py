from random import randint, choice
import prompt


def calc_game():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    action = choice(["+", "-", "*"])
    print("What is the result of the expression?")
    print(f"Question: {number1} {action} {number2}")
    answer = prompt.string("Your answer: ")

    if action == "+":
        right_answer = number1 + number2
    elif action == "-":
        right_answer = number1 - number2
    elif action == "*":
        right_answer = number1 * number2

    return str(answer), str(right_answer)
