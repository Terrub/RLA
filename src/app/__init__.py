# coding=utf-8
"""
Initiation of the applet that starts the game using python
"""

import random

from pyglet.window import Window

from src.app.game import Game
from src.app.world import World


class Point:
    """
    Point class
    """

    def __init__(self, x, y, z):
        """
        Constructor
        """
        self.x = x
        self.y = y
        self.z = z


class Camera:
    """
    Camera Class
    """

    def __init__(self, x, y, z):
        """
        Constructor
        """
        self.x = x
        self.y = y
        self.z = z


def main():
    """
    app container?
    """
    win_width = 800
    win_height = 600
    random.seed(1)
    world = World(random, 128, 128)
    window = Window(width=win_width, height=win_height, vsync=True)
    # window = Window(fullscreen=True, vsync=True)

    camera = Camera(0, 0, 0)

    game = Game(world=world, window=window, camera=camera)
    game.start()


if __name__ == '__main__':
    main()
