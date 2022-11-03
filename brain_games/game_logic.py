from brain_games.cli import welcome_user
import prompt


NUMBER_OF_ROUNDS = 3


def run_game(func):
    print("Welcome to the Brain Games!")
    player_name = welcome_user()
    step = 0

    while step < NUMBER_OF_ROUNDS:
        right_answer = func()
        answer = prompt.string("Your answer: ")

        if right_answer == answer:
            print("correct!")
            step += 1
        else:
            print(f"Let's try again, {player_name}!")
            break

    if step == 3:
        print(f"Congratulations, {player_name}!")
