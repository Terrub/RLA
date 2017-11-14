# coding=utf-8
"""
The actual game module.

This should contain values or references to all the game related states and
info that it needs to make the game work and playable.
"""
from pyglet.gl import (
    GL_COLOR_BUFFER_BIT, GL_MODELVIEW, GL_PROJECTION, glClear,
    glLoadIdentity, glMatrixMode, gluOrtho2D
)
from pyglet.graphics import Batch, OrderedGroup
from pyglet.resource import image
from pyglet.sprite import Sprite
from pyglet.window import key


class Game:
    """
    The game class
    """

    def __init__(self, world, window, camera) -> None:
        """
        Constructor
        """
        self.world = world
        self.window = window
        self.camera = camera
        self.sprite_batch = None
        self.sprites = {}
        self.unit = 16

    @staticmethod
    def _move_camera_down(camera, unit):
        new_y = max(camera.y - 4, 0)
        camera.y = new_y

    @staticmethod
    def _move_camera_up(calculated_height, camera, unit):
        new_y = min(camera.y + 4, calculated_height)
        camera.y = new_y

    @staticmethod
    def _move_camera_right(calculated_width, camera, unit):
        new_x = camera.x + 4
        if new_x >= calculated_width:
            new_x = 0
        camera.x = new_x

    @staticmethod
    def _move_camera_left(calculated_width, camera, unit):
        new_x = camera.x - 4
        if new_x <= 0:
            new_x = calculated_width
        camera.x = new_x

    def start(self):
        """
        Starts the current game object and main loop
        """
        window = self.window
        self.pressed_keys = key.KeyStateHandler()
        window.push_handlers(self.pressed_keys)
        while not window.has_exit:
            window.dispatch_events()
            self.validate_camera()
            self.render_to_window()

    def validate_camera(self):
        pressed = self.pressed_keys
        unit = self.unit
        camera = self.camera
        world = self.world
        window = self.window

        calculated_width = world.width * unit
        calculated_height = world.height * unit - window.height

        if pressed[key.LEFT] and not pressed[key.RIGHT]:
            self._move_camera_left(calculated_width, camera, unit)
        elif pressed[key.RIGHT] and not pressed[key.LEFT]:
            self._move_camera_right(calculated_width, camera, unit)

        if pressed[key.UP] and not pressed[key.DOWN]:
            self._move_camera_up(calculated_height, camera, unit)
        elif pressed[key.DOWN] and not pressed[key.UP]:
            self._move_camera_down(camera, unit)

    def render_to_window(self):
        """
        Renders the game to the current window
        """
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
        """
        Draws the world
        """
        sprite_batch = self.get_sprite_batch()
        sprite_batch.draw()

    def draw_hud(self):
        """
        Draws the hud
        """
        pass

    def get_sprite_batch(self):
        """
        Getter for a new sprite batch
        """
        if self.sprite_batch is None:
            world = self.world
            unit = self.unit
            window = self.window
            sprites = self.sprites

            sprite_batch = Batch()
            floor_group = OrderedGroup(0)

            width = world.width
            height = world.height
            z = 0

            for y in range(height):
                for x in range(width + (window.width // unit)):
                    offset_x = x % width
                    key = world.get_tile_key_from(offset_x, y, z)
                    floor = world.get_tile_at(key, y)
                    path = '{}.png'.format(floor.type)
                    img_floor = image(path)
                    calculated_x = x * unit
                    calculated_y = y * unit
                    sprite = Sprite(
                        img_floor,
                        x=calculated_x,
                        y=calculated_y,
                        batch=sprite_batch,
                        group=floor_group)
                    sprites[(x, y)] = sprite

            self.sprite_batch = sprite_batch

        return self.sprite_batch
