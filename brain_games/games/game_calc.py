from random import randint, choice


def calc_game():
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    action = choice(["+", "-", "*"])

    CONDITION = f"""What is the result of the expression?"\nQuestion: {number1} {action} {number2}"""

    right_answer = calculate(number1, number2, action)
    return CONDITION, str(right_answer)


def calculate(num1, num2, action):
    if action == "+":
        right_answer = num1 + num2
    elif action == "-":
        right_answer = num1 - num2
    elif action == "*":
        right_answer = num1 * num2
    return right_answer
