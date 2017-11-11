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

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """
        Key press handler for pyglet window
        """
        unit = self.unit
        if symbol == key.LEFT:
            self.camera.x += -unit
        elif symbol == key.RIGHT:
            self.camera.x += unit
        elif symbol == key.UP:
            self.camera.y += unit
        elif symbol == key.DOWN:
            self.camera.y += -unit

    def start(self) -> None:
        """
        Starts the current game object and main loop
        """
        window = self.window
        window.push_handlers(self.on_key_press)
        while not window.has_exit:
            window.dispatch_events()
            self.render_to_window()

    def render_to_window(self) -> None:
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

    def draw_world(self) -> None:
        """
        Draws the world
        """
        sprite_batch = self.get_sprite_batch()
        sprite_batch.draw()

    def draw_hud(self) -> None:
        """
        Draws the hud
        """
        pass

    def get_sprite_batch(self) -> Batch:
        """
        Getter for a new sprite batch
        """
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
                    img_floor = image(path)
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
