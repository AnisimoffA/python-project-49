from brain_games.cli import welcome_user
import prompt


def run_game(game):
    number_of_rounds = 3
    print("Welcome to the Brain Games!")
    player_name = welcome_user()
    step = 0

    while step < number_of_rounds:
        game_condition, right_answer = game()
        print(game_condition)

        answer = prompt.string("Your answer: ")

        if right_answer == answer:
            print("correct!")
            step += 1
        else:
            print(f"Let's try again, {player_name}!")
            break

    if step == 3:
        print(f"Congratulations, {player_name}!")
