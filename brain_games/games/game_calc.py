from random import randint, choice
import brain_games.game_logic as game_logic
import prompt


def calc_game():
    name = game_logic.name
    number1 = randint(1,30)
    number2 = randint(1,30)
    action = choice(["+","-","*"])
    print(f"What is the result of the expression?\nQuestion: {number1} {action} {number2}")
    answer = prompt.string("Your answer: ")

    if action == "+":
        right_answer = number1 + number2
    elif action == "-":
        right_answer = number1 - number2
    elif action == "*":
        right_answer = number1 * number2

    return str(answer), str(right_answer)
    
