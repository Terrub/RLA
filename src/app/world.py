# coding=utf-8
"""
The world object
"""
from math import pi, sin


class Tile:
    """
    The World tile class
    """

    def __init__(self, p_type, p_id):
        """
        Constructor
        """
        self.type = p_type
        self.id = p_id


class World:
    """
    The world class
    """

    def __init__(self, randomiser, width, height):
        """
        Constructor
        """
        self.height = width
        self.width = height
        self.randomiser = randomiser

        self.tiles = {}

    @staticmethod
    def _create_tile(randomiser, key, h, y):
        """
        Creates a tile for given key, height and y position.
        """
        tile_type = World._calculate_tile_type(randomiser, h, y)
        tile = Tile(p_type=tile_type, p_id=key)

        return tile

    @staticmethod
    def _calculate_tile_type(randomiser, h, y):
        """
        Returns the tile type based on local algorithm and given params.
        """
        p = randomiser.random()
        tile_type = 'grass' if p < sin(y / h * pi) else 'stone'

        return tile_type

    def get_tile_key_from(self, x, y, z):
        """
        Returns the tile key for given coordinates.
        """
        h = self.height
        w = self.width
        return (z * h * w) + (y * w) + x

    def get_tile_at(self, key, y):
        """
        Returns tile info for given coordinates.
        """
        tiles = self.tiles
        if key not in tiles:
            height = self.height
            randomiser = self.randomiser
            tiles[key] = World._create_tile(randomiser, key, height, y)

        tile = tiles[key]

        return tile
