from brain_games.cli import welcome_user
import prompt


def run_game(game):
    game_task = game.TASK
    number_of_rounds = 3
    print("Welcome to the Brain Games!")
    player_name = welcome_user()

    step = 0

    print(game_task)

    while step < number_of_rounds:
        input_line, right_answer = game.game()
        print(input_line)
        answer = prompt.string("Your answer: ")

        if right_answer == answer:
            print("correct!")
            step += 1
        else:
            print(f"Let's try again, {player_name}!")
            break

    if step == 3:
        print(f"Congratulations, {player_name}!")
