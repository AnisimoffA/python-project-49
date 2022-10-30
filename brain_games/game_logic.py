from brain_games.scripts.brain_games import main2


name = main2()


def logic(func):
    n = 0
    while n <= 2:
        a = func()
        if a[0] == a[1]:
            print("correct!")
            n += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if n == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    logic()
