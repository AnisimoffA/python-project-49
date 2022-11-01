from random import randint
import prompt


def prime_game():
    number = randint(1, 100)
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    print(f"Question: {number}")

    if is_prime(number) == 0:
        right_answer = "yes"
    else:
        right_answer = "no"

    return right_answer


def is_prime(num):
    count = 0
    for x in range(2, num):
        if num % x == 0:
            count += 1
    return count
