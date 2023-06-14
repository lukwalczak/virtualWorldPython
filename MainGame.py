import arcade
import arcade.gui


BUTTON_WIDTH = 250
BUTTON_HEIGHT = 40
BUTTON_SPACING = 60
BUTTON_OFFSET = 20
GAMEBOARD_POINT_DIMENSION = 30

class GameView(arcade.View):
    def __init__(self, menu_view):
        super().__init__()
        self.menu_view = menu_view
        self.game_width = 20
        self.game_height = 20
        self.game = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.WINE)
        self.options_grid = arcade.gui.UIBoxLayout()
        self.game_layout = arcade.gui.UIBoxLayout()
        self.setup_game()
        self.manager.add(self.game_layout)
        self.setup_buttons()

    def setup_buttons(self):
        center_x = self.window.width // 2
        center_y = self.window.height // 2
        exit_to_main_menu_button = arcade.gui.UIFlatButton(
            text="Exit to main menu",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        start_game_button = arcade.gui.UIFlatButton(
            text="Start Game",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        load_game_button = arcade.gui.UIFlatButton(
            text="Load Game",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )

        @exit_to_main_menu_button.event("on_click")
        def on_click_exit_button(event):
            self.window.show_view(self.menu_view)
        @start_game_button.event("on_click")
        def on_click_exit_button(event):
            self.setup_game()
        self.options_grid.add(start_game_button)
        self.options_grid.add(load_game_button)
        self.options_grid.add(exit_to_main_menu_button)
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="left", anchor_y="bottom", child=self.options_grid))

    def setup_game(self):
        self.game = Game(self.game_width, self.game_height)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.organisms = []
        self.organisms.append("S")
        self.organisms.append("C")
