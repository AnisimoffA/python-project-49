from random import randint, choice
import brain_games.scripts.brain_games as brain_games
import brain_games.game_logic as game_logic
import prompt

    
def even_game():
    name = game_logic.name
    number = randint(1,6)
    answer = prompt.string(f"Answer \"yes\" if the number is even, otherwise answer \"no\"\nQuestion: {number}\n")
    print("Your answer: ", answer)

    if answer == "yes" and number % 2 == 0 or answer == "no" and number % 2 != 0:
        print("correct!")
    else:
        print(f"Let's try again, {name}!")
        return False
