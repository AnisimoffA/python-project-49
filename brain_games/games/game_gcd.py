from random import randint


def gcd_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    print("Find the greatest common divisor of given numbers.")
    print(f"Question: {number1} {number2}")
    answer_list = []

    for x in getAllDivisors(number1):
        if x in getAllDivisors(number2):
            answer_list.append(x)

    right_answer = max(answer_list)
    return str(right_answer)


def getAllDivisors(n):
    all_dividers = []

    for x in range(1, int(n/2 + 1)):
        if n % x == 0:
            all_dividers.append(x)
    return all_dividers
