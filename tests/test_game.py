# coding=utf-8
"""
Tests for the game object
"""
import pytest

from src.app.game import Game, WorldPosition


@pytest.fixture()
def fixt_game():
    """
    Yields an instance of the game class
    :return: Game instance
    :rtype: Game
    """
    game = Game()

    yield game


class TestGameClass:
    """
    Test class for Game class
    """

    def test_game_exposes_method_get_player_position(self, fixt_game):
        """
        Tests whether the game object exposes the get_player_position method.
        """
        assert hasattr(fixt_game, 'get_player_position')

    def test_game_exposes_method_start(self, fixt_game):
        """
        Tests whether the game can be started or not
        """
        assert hasattr(fixt_game, 'start')

    def test_get_player_position_returns_world_position(self, fixt_game):
        """
        Test get player position's x is not none
        """
        position = fixt_game.get_player_position()

        assert isinstance(position, WorldPosition)
