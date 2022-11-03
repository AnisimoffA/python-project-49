from random import randint


def prime_game():
    number = randint(1, 100)
    TASK = f'Answer "yes" if given number is prime. Otherwise answer "no".\n\
Question: {number}'

    if is_prime(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return TASK, right_answer


def is_prime(num):
    count = 0
    for x in range(2, num):
        if num % x == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False
