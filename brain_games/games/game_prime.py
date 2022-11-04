from random import randint


def prime_game():
    number = randint(1, 100)
    TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    input_line = f"Question: {number}"

    if is_prime(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return TASK, input_line, right_answer


def is_prime(num):
    count = 0

    if num == 1:
        return False

    for x in range(2, int(num / 2) + 1):
        if num % x == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
