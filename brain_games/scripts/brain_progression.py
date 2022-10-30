#!/usr/bin/env python3
from brain_games import game_logic
from brain_games.games import game_progression


def main():
    game_logic.logic(game_progression.progression_game)


if __name__ == "__main__":
    main()
