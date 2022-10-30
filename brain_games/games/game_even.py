from random import randint, choice
import brain_games.scripts.brain_games as brain_games
import brain_games.game_logic as game_logic
import prompt

    
def even_game():
    number = randint(1,6)
    answer = prompt.string(f"Answer \"yes\" if the number is even, otherwise answer \"no\".\nQuestion: {number}\n")
    print("Your answer: ", answer)

    if is_even(number):
        right_answer = "yes"
    else:
        right_answer = "no"

    return str(answer), str(right_answer)

def is_even(num):
    if  num % 2 == 0:
        return True
    else:
        return False