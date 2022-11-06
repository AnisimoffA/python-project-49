from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    number = randint(1, 100)
    input_line = f"Question: {number}"

    if is_prime(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return input_line, right_answer


def is_prime(num):
    if num == 1:
        return False

    for x in range(2, int(num / 2) + 1):
        if num % x == 0:
            return False
    return True
