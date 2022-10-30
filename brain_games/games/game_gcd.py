from random import randint
import prompt


def gcd_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    print("Find the greatest common divisor of given numbers.")
    print(f"Question: {number1} {number2}")
    answer = prompt.string("Your answer: ")
    answer_list = []

    for x in max_divider(number1):
        for y in max_divider(number2):
            if x == y:
                answer_list.append(x)
                break

    right_answer = max(answer_list)

    return str(answer), str(right_answer)


def max_divider(n):
    all_dividers = []

    for x in range(1, n + 1):
        if n % x == 0:
            all_dividers.append(x)
    return all_dividers
