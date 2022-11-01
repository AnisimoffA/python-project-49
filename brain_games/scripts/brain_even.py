#!/usr/bin/env python3
from brain_games import game_logic
from brain_games.games import game_even


def main():
    game_logic.lets_play(game_even.even_game)


if __name__ == "__main__":
    main()
