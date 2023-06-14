import arcade
import arcade.gui

BUTTON_WIDTH = 250
BUTTON_HEIGHT = 40
BUTTON_SPACING = 60
BUTTON_OFFSET = 20


class NewGame(arcade.gui.UIFlatButton):
    def on_click(self, event: UIOnClickEvent):
        game = Game()
        game.start()

class ExitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.width = width
        self.height = height
        self.title = title
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))
        arcade.set_background_color(arcade.color.WINE)
        self.draw_menu()

    def draw_menu(self):
        center_x = self.width // 2
        center_y = self.height // 2
        new_game_button = arcade.gui.UIFlatButton(
            text="New Game",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y + BUTTON_SPACING
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
        exit_button = ExitButton(
            text="Exit",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            center_x=center_x,
            center_y=center_y - 2 * BUTTON_SPACING
        )
        self.v_box.add(new_game_button, center_x=center_x, center_y=center_y + BUTTON_SPACING)
        self.v_box.add(load_game_button, center_x=center_x, center_y=center_y + BUTTON_OFFSET)
        self.v_box.add(settings_button, center_x=center_x, center_y=center_y - BUTTON_SPACING + BUTTON_OFFSET)
        self.v_box.add(exit_button, center_x=center_x, center_y=center_y - 2 * BUTTON_SPACING + BUTTON_OFFSET)


    def on_draw(self):
        self.clear()
        self.manager.draw()

    def exit_game(self,event):
        arcade.exit()
