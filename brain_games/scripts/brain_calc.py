#!/usr/bin/env python3
from brain_games import game_logic
from brain_games.games import game_calc


def main():
    game_logic.run_game(game_calc.calc_game)


if __name__ == "__main__":
    main()
