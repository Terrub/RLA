# coding=utf-8
"""
Display module.

Contains all the shit we need to display whatever we throw at it.
"""
import pyglet
from pyglet.sprite import Sprite


class Display:
    """
    Display class
    """
    def __init__(self, game):
        """
        Constructor

        :param game: The game that should be displayed
        :type game: src.app.game.Game
        """
        self.game = game

    def display_player(self):
        game = self.game
        pos = game.get_player_position()

        self.draw_player_at(pos)

    def draw_player_at(self, pos):
        image = pyglet.resource.image('sprites\entities.png')
        player_sprite = Sprite(image)
        player_sprite.draw()

