# coding=utf-8
"""
The actual game module.

This should contain values or references to all the game related states and
info that it needs to make the game work and playable.
"""

class Game:
    """
    Game class
    """

    STATUS_RUNNING = 1

    def get_player_position(self):
        return WorldPosition()

    def start(self):
        self.status = self.STATUS_RUNNING

class WorldPosition:
    pass
