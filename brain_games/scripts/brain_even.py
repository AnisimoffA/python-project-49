import brain_games.scripts.brain_games as brain_games
from random import randint
import prompt

def main():
    name = brain_games.main() #это и есть наше имя
    n = 0
    while n <= 2:
        number = randint(1,6)
        answer = prompt.string(f"Answer \"yes\" if the number is even, otherwise answer \"no\"\nQuestion: {number}\n")
        print("Your answer: ", answer)
        if answer == "yes" and number % 2 == 0 or answer == "no" and number % 2 != 0:
            print("correct!")
            n += 1
        else:
            print(f"Let's try again, {name}!")
            break
        if n == 3:
            print(f"Congratulations, {name}")

if __name__ == "__main__":
    main()
