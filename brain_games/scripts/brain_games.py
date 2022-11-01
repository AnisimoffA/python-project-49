#!/usr/bin/env python3
import brain_games.cli as cli


def main():
    print("Welcome to the Brain Games!")
    cli.welcome_user()


def main2():
    print("Welcome to the Brain Games!")
    x = cli.welcome_user()
    return x

name = main2()


if __name__ == "__main__":
    main()
