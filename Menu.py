import arcade
import arcade.gui
from MainGame import GameView

BUTTON_WIDTH = 250
BUTTON_HEIGHT = 40
BUTTON_SPACING = 60
BUTTON_OFFSET = 20


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=BUTTON_OFFSET)
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))
        arcade.set_background_color((219, 108, 121))
        self.draw_menu()

    def draw_menu(self):
        center_x = self.window.width // 2
        center_y = self.window.height // 2
        new_game_button = NewGameButton(
            text="New Game",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y + 100
        )
        load_game_button = arcade.gui.UIFlatButton(
            text="Load Game",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y
        )
        settings_button = arcade.gui.UIFlatButton(
            text="Settings",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y - BUTTON_SPACING
        )
        exit_button = arcade.gui.UIFlatButton(
            text="Exit",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y - 2 * BUTTON_SPACING
        )
        @exit_button.event("on_click")
        def on_click_exit_button(event):
            arcade.exit()
        @new_game_button.event("on_click")
        def on_click_exit_button(event):
            game_view = GameView(self)
            self.window.show_view(game_view)
        self.v_box.add(new_game_button, center_x=center_x, center_y=center_y + BUTTON_SPACING)
        self.v_box.add(load_game_button, center_x=center_x, center_y=center_y)
        self.v_box.add(settings_button, center_x=center_x, center_y=center_y - BUTTON_SPACING)
        self.v_box.add(exit_button, center_x=center_x, center_y=center_y - 2 * BUTTON_SPACING)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()


class NewGameButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        pass


class SettingsView(arcade.View):
    def __init__(self, menu_view):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()
