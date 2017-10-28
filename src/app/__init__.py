# coding=utf-8
"""
Initialisation of the RLA game
"""
from src.app.display import Display
from src.app.game import Game


def initialise():
    """
    Starts the game
    """

    display = Display()
    game = Game()

if __name__ == '__main__':
    initialise()
