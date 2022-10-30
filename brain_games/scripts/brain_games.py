#!/usr/bin/env python3
import brain_games.cli as cli

print(__name__)
def main():
    print("Welcome to the Brain Games!")
    x = cli.welcome_user()
    return x

if __name__ == "__main__":
    main()
else:
    def main():
        print("Welcome to the Brain Games!")
        x = cli.welcome_user()