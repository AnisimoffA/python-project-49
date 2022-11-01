from brain_games.scripts.brain_games import name
import prompt


player_name = name

def lets_play(func):
    step = 0
    while step <= 2:
        right_answer = func()
        answer = prompt.string("Your answer: ")

        if right_answer == answer:
            print("correct!")
            step += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if step == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    logic()
