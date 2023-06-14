import arcade
import arcade.gui
from World import World


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title,resizable=True)
        self.game_width = 20
        self.game_height = 20
        self.world = None

    def start(self):
        self.world = World(self.width, self.height)
        pass

    def on_draw(self):
        self.clear()
        self.manager.draw()
