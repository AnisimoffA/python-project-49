from random import randint


def gcd_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    CONDITION = f"""Find the greatest common divisor of given numbers.\nQuestion: {number1} {number2}"""
    answer_list = []

    number1_all_divisors = get_all_divisors(number1)
    number2_all_divisors = get_all_divisors(number2)

    for x in number1_all_divisors:
        if x in number2_all_divisors:
            answer_list.append(x)

    right_answer = max(answer_list)
    return CONDITION, str(right_answer)


def get_all_divisors(n):
    all_dividers = []

    for x in range(1, int(n / 2 + 1) + 1):
        if n % x == 0:
            all_dividers.append(x)
    return all_dividers
