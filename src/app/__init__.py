# coding=utf-8
from random import choice

from pyglet.gl import *
from pyglet.graphics import Batch, OrderedGroup
from pyglet.sprite import Sprite
from pyglet.window import Window, key


class Game:
    def __init__(self, world, window, camera):
        self.world = world
        self.window = window
        self.camera = camera
        self.sprite_batch = None
        self.sprites = {}
        self.unit = 16

    def on_key_press(self, symbol, modifiers):
        unit = self.unit
        if symbol == key.LEFT:
            self.camera.x += -unit
        elif symbol == key.RIGHT:
            self.camera.x += unit
        elif symbol == key.UP:
            self.camera.y += unit
        elif symbol == key.DOWN:
            self.camera.y += -unit

    def start(self):
        window = self.window
        window.push_handlers(self.on_key_press)
        while not window.has_exit:
            window.dispatch_events()
            self.render_to_window()

    def render_to_window(self):
        window = self.window
        camera = self.camera

        y = camera.y
        x = camera.x

        x1 = x
        x2 = window.width + x
        y1 = y
        y2 = window.height + y

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(x1, x2, y1, y2)

        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.draw_world()
        self.draw_hud()

        window.flip()

    def draw_world(self):
        sprite_batch = self.get_sprite_batch()
        sprite_batch.draw()

    def draw_hud(self):
        pass

    def get_sprite_batch(self):
        world = self.world
        unit = self.unit

        if self.sprite_batch is None:
            sprite_batch = Batch()
            floor_group = OrderedGroup(0)
            sprites = self.sprites
            z = 0

            for y in range(world.height):
                for x in range(world.width):
                    floor = world.get_tile_at(x, y, z)
                    path = '{}.png'.format(floor.type)
                    img_floor = pyglet.resource.image(path)
                    calculated_x = x * unit
                    calculated_y = y * unit
                    sprite = Sprite(
                        img_floor,
                        x=calculated_x,
                        y=calculated_y,
                        batch=sprite_batch,
                        group=floor_group)
                    sprites[floor.id] = sprite

            self.sprite_batch = sprite_batch

        return self.sprite_batch


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
        if not key in tiles:
            type = choice(['grass', 'stone'])
            tiles[key] = Tile(type=type, id=key)

        tile = tiles[key]

        return tile

    def get_tile_key_from(self, x, y, z):
        return (z * self.height) + (y * self.width) + x


win_width = 800
win_height = 600
win_unit = 16
world = World()
window = Window(width=win_width, height=win_height, vsync=True)

camera_point = Point(0, 0, 0)
camera = Camera(camera_point)

game = Game(world=world, window=window, camera=camera)
game.start()
