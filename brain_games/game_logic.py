from brain_games.scripts.brain_games import main

name = main()

def logic(func):
    n = 0
    while n <= 2:
        if func() == False:
            break
        n += 1
        if n == 3:
            print(f"Congratulations, {name}")

if __name__ == "__main__":
    logic()


