from random import randint
import brain_games.game_logic as game_logic
import prompt

    
def prime_game():
    name = game_logic.name
    number = randint(1,100)
    print(f"Answer \"yes\" if given number is prime. Otherwise answer \"no\".\nQuestion: {number}")
    answer = prompt.string("Your answer: ")

    if is_prime(number) == 0:
        right_answer = "yes"
    else:
        right_answer = "no"

    return str(answer), str(right_answer)

def is_prime(num):
    count = 0
    for x in range(2,num):
        if num % x == 0:
            count += 1
    return count
    