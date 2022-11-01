#!/usr/bin/env python3
from brain_games import game_logic
from brain_games.games import game_gcd


def main():
    game_logic.lets_play(game_gcd.gcd_game)


if __name__ == "__main__":
    main()
