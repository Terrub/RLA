# coding=utf-8
"""
The world object
"""
from math import pi, sin


class Tile:
    """
    The World tile class
    """

    def __init__(self, p_type: str, p_id: int) -> None:
        """
        Constructor
        """
        self.type = p_type
        self.id = p_id


class World:
    """
    The world class
    """

    def __init__(self, randomiser) -> None:
        """
        Constructor
        """
        self.surface_radius = 1
        self.entities = []
        self.height = 64
        self.width = 64
        self.depth = 1
        self.tiles = {}
        self.changed = True

        self.randomiser = randomiser

    @staticmethod
    def _create_tile(randomiser, key, h, y) -> Tile:
        """
        Creates a tile for given key, height and y position.
        """
        tile_type = World._calculate_tile_type(randomiser, h, y)
        tile = Tile(p_type=tile_type, p_id=key)

        return tile

    @staticmethod
    def _calculate_tile_type(randomiser, h, y) -> str:
        """
        Returns the tile type based on local algorithm and given params.
        """
        p = randomiser.random()
        tile_type = 'grass' if p < sin(y / h * pi) else 'stone'

        return tile_type

    def get_tile_key_from(self, x, y, z) -> int:
        """
        Returns the tile key for given coordinates.
        """
        h = self.height
        w = self.width
        return (z * h * w) + (y * w) + x

    def get_tile_at(self, key, y) -> Tile:
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
