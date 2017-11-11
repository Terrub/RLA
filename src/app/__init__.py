# coding=utf-8
from random import random

import math
from pyglet.window import Window

from src.app.game import Game


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Camera:
    def __init__(self, point):
        self.x = point.x
        self.y = point.y
        self.z = point.z


class Tile:
    def __init__(self, type, id):
        self.type = type
        self.id = id


class World:
    def __init__(self):
        self.surface_radius = 1
        self.entities = []
        self.height = 70
        self.width = 70
        self.depth = 10
        self.tiles = {}
        self.changed = True

    def get_tile_at(self, x, y, z):
        tiles = self.tiles
        key = self.get_tile_key_from(x, y, z)
        h = self.height
        p = random()
        if not key in tiles:
            type = 'grass' if p < math.sin(y / h * math.pi) else 'stone'
            tiles[key] = Tile(type=type, id=key)

        tile = tiles[key]

        return tile

    def get_tile_key_from(self, x, y, z):
        return (z * self.height) + (y * self.width) + x


def main():
    """
    app container?
    """
    win_width = 800
    win_height = 600
    world = World()
    window = Window(width=win_width, height=win_height, vsync=True)

    camera_point = Point(0, 0, 0)
    camera = Camera(camera_point)

    game = Game(world=world, window=window, camera=camera)
    game.start()


if __name__ == '__main__':
    main()
