import arcade
import arcade.gui


BUTTON_WIDTH = 250
BUTTON_HEIGHT = 40
BUTTON_SPACING = 60
BUTTON_OFFSET = 20
GAME_POINT_COLOR = (222, 185, 134)
GAME_POINT_WIDTH = 30
GAME_POINT_HEIGHT = 30

default_game_point_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 15,
            "font_color": (0,0,0),
            "border_color": None,
            "bg_color": GAME_POINT_COLOR,

            # used if button is pressed
            "bg_color_pressed": (139, 97, 38),
            "border_color_pressed": (139, 97, 38),  # also used when hovered
            "font_color_pressed": (139, 97, 38),
            "bg_color_hover": (237, 77, 110)
        }


class GameView(arcade.View):
    def __init__(self, menu_view):
        super().__init__()
        self.menu_view = menu_view
        self.game_width = 20
        self.game_height = 20
        self.game = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color((219, 108, 121))
        self.options_grid = arcade.gui.UIBoxLayout()
        self.game_points = []
        self.game_layout = arcade.gui.UIBoxLayout()
        self.setup_game()
        self.manager.add(self.game_layout)
        self.setup_buttons()

    def setup_buttons(self):
        center_x = self.window.width // 2
        center_y = self.window.height // 2
        for y in range(self.game_height):
            for x in range(self.game_width):
                self.game_points.append(GamePoint(300 + 40 * x, 100 + 40 * y, 'H', GAME_POINT_WIDTH, GAME_POINT_HEIGHT, 0, 0))
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
        for p in self.game_points:
            self.manager.add(p)

    def setup_game(self):
        self.game = Game(self.game_width, self.game_height)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        for p in self.game_points:
            p.draw()
        self.manager.draw()

    def update(self, delta_time):
        for p in self.game_points:
            p.update(delta_time)

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()


class GamePoint(arcade.gui.UIFlatButton):
    def __init__(self, pos_x, pos_y, char, height, width, board_x, board_y):
        super().__init__(pos_x, pos_y, width, height, style=default_game_point_style, text=char)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.char = char
        self.board_x = board_x
        self.board_y = board_y
        self.color = GAME_POINT_COLOR

    def draw(self):
        pass

    def update(self, delta_time):
        pass

    def on_click(self, event):
        pass


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.organisms = []
