from random import randint, choice
import brain_games.scripts.brain_games as brain_games
import brain_games.game_logic as game_logic
import prompt


def calc_game():
    name = game_logic.name
    number1 = randint(1,30)
    number2 = randint(1,30)
    action = choice(["+","-","*"])
    print(f"What the result of the expression?\nQuestion: {number1} {action} {number2}")
    answer = prompt.string("Your answer: ")

    if action == "+":
        right_answer = number1 + number2
    elif action == "-":
        right_answer = number1 - number2
    elif action == "*":
        right_answer = number1 * number2

    if answer == str(right_answer):
        print("Correct!")
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}.\nLet's try again, {name}")
        return False
    
