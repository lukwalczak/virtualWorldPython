import arcade
import arcade.gui

import conf
from Human import Human
import random
import OrganismFactory
import json
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 40
BUTTON_SPACING = 60
BUTTON_OFFSET = 20
GAME_POINT_COLOR = (222, 185, 134)
GAME_POINT_WIDTH = 35
GAME_POINT_HEIGHT = 35
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

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


class DeathView(arcade.View):
    def __init__(self, menu_view):
        super().__init__()
        self.manager = arcade.gui.UIManager()
        arcade.set_background_color((219, 108, 121))
        self.manager.enable()
        self.menu_view = menu_view
        menu_button = arcade.gui.UIFlatButton(
            text="Exit to main menu",
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
        )
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=menu_button))

        @menu_button.event("on_click")
        def on_click_exit_button(event):
            self.window.show_view(self.menu_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()


class GameView(arcade.View):
    def __init__(self, menu_view):
        super().__init__()
        self.menu_view = menu_view
        self.game_width = 20
        self.game_height = 20
        self.game = Game(self.game_width, self.game_height, self)
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
        for y in range(self.game_height):
            for x in range(self.game_width):
                self.game_points.append(GamePoint(340 + 40 * x, 100 + 40 * y, "", GAME_POINT_WIDTH, GAME_POINT_HEIGHT, 0, 0))
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

        @exit_to_main_menu_button.event("on_click")
        def on_click_exit_button(event):
            self.window.show_view(self.menu_view)

        @load_game_button.event("on_click")
        def on_click_load_game(event):
            self.game.load_game()
        self.options_grid.add(start_game_button)
        self.options_grid.add(load_game_button)
        self.options_grid.add(exit_to_main_menu_button)
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="left", anchor_y="bottom", child=self.options_grid))
        for p in self.game_points:
            self.manager.add(p)

    def setup_game(self):
        self.game = Game(self.game_width, self.game_height, self)

    def clear_organisms(self):
        for gp in self.game_points:
            gp.set_char('')

    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.clear_organisms()
        self.game.draw_organisms()
        self.game.draw_logs()

    def update(self, delta_time):
        for p in self.game_points:
            p.update(delta_time)

    def on_hide_view(self):
        self.manager.disable()

    def on_show_view(self):
        self.manager.enable()

    def get_game_points(self):
        return self.game_points

    def get_game_point_at_xy(self,x,y):
        return self.game_points[self.game_height*y+x]

    def change_char_game_point_at_xy(self, x, y, char):
        self.game_points[self.game_height*y+x].set_char(char)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.game.move_human(-1, 0)
        elif symbol == arcade.key.RIGHT:
            self.game.move_human(1, 0)
        elif symbol == arcade.key.UP:
            self.game.move_human(0, 1)
        elif symbol == arcade.key.DOWN:
            self.game.move_human(0, -1)
        elif symbol == arcade.key.S:
            self.game.save_game()
        elif symbol == arcade.key.L:
            self.game.load_game()
        elif symbol == arcade.key.P:
            self.game.use_ability()


class GamePoint(arcade.gui.UIFlatButton):
    def __init__(self, pos_x, pos_y, char, height, width, board_x, board_y):
        super().__init__(pos_x, pos_y, width, height, style=default_game_point_style, text=char)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.char = char
        self.board_x = board_x
        self.board_y = board_y
        self.color = GAME_POINT_COLOR

    def update(self, delta_time):
        pass

    def on_click(self, event):
        pass

    def set_char(self, char):
        self.char = char
        self.text = char


class Game:
    def __init__(self, width, height, game_view):
        self.width = width
        self.height = height
        self.game_view = game_view
        self.logs = [] * 30
        self.logs.append("test log")
        self.organisms = []
        self.human = Human(self, self.game_view, conf.HUMAN_X, conf.HUMAN_Y)
        self.organisms.append(self.human)
        self.generate_organisms()
        self.do_first_half_turn()

    def generate_organisms(self):
        self.generate_organism("SHEEP")
        self.generate_organism("WOLF")
        self.generate_organism("FOX")
        self.generate_organism("ANTELOPE")
        self.generate_organism("TURTLE")
        self.generate_organism("CYBERSHEEP")
        self.generate_organism("GRASS")
        self.generate_organism("DANDELION")
        self.generate_organism("NIGHTSHADE")
        self.generate_organism("PINEBORSCH")
        self.generate_organism("GUARANA")

    def generate_organism(self, name):
        for i in range(0, 3):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.width - 1)
            while self.get_organism_at_xy(x, y) is not None:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.width - 1)
            OrganismFactory.createOrganism(name, x, y, self, self.game_view)

    def generate_organism_at_xy(self, x, y, name):
        OrganismFactory.createOrganism(name, x, y, self, self.game_view)

    def draw_organisms(self):
        for o in self.organisms:
            o.draw()
        self.human.draw()

    def use_ability(self):
        if self.human.ability_cooldown != 0:
            print("cooldown = " + str(self.human.ability_cooldown))
            return
        print("human used ability")
        self.human.ability_last_time = 5
        self.do_turn()


    def move_human(self, dx, dy):
        self.is_human_alive()
        self.human.action(dx, dy)
        self.do_turn()

    def do_turn(self):
        self.is_human_alive()
        self.do_second_half_turn()
        self.sort_organisms()
        self.do_first_half_turn()
        self.sort_organisms()

    def sort_organisms(self):
        self.organisms.sort(key=lambda x: (x.initiative, -x.age), reverse=True)

    def is_organism_at_xy(self, x, y):
        for o in self.organisms:
            if o is not None and o.pos_x == x and o.pos_y == y:
                return True
        return False

    def get_organism_at_xy(self, x, y):
        for o in self.organisms:
            if o is not None and o.pos_x == x and o.pos_y == y:
                return o
        return None

    def do_first_half_turn(self):
        for o in self.organisms:
            if isinstance(o, Human):
                continue
            if o.initiative > self.human.initiative or (o.initiative == self.human.initiative and o.age >= self.human.age):
                o.action(0, 0)

    def do_second_half_turn(self):
        for o in self.organisms:
            if isinstance(o, Human):
                continue
            if o.initiative <= self.human.initiative:
                o.action(0, 0)

    def remove_organism(self, organism):
        for o in self.organisms:
            if o == organism:
                self.organisms.remove(organism)
                break

    def is_human_alive(self):
        if not self.human.alive:
            death_view = DeathView(self.game_view.menu_view)
            self.game_view.window.show_view(death_view)

    def save_game(self):
        print("saved")
        organisms_to_save = []
        for o in self.organisms:
            organisms_to_save.append({"organism_name":o.organism_name,"pos_x":o.pos_x,"pos_y":o.pos_y})
        save_game = {"game_width":self.width,"game_height":self.height,"organisms":organisms_to_save}
        with open("saved_game.json", "w") as f:
            json.dump(save_game,f)

    def load_game(self):
        self.game_view.manager.disable()
        self.organisms.clear()
        f = open('saved_game.json')
        data = json.load(f)
        self.width = data["game_width"]
        self.height = data["game_height"]
        for i in data["organisms"]:
            if i["organism_name"] == "HUMAN":
                self.human.pos_y = i["pos_y"]
                self.human.pos_x = i["pos_x"]
            self.generate_organism_at_xy(i["pos_x"],i["pos_y"],i["organism_name"])

        self.game_view.manager.enable()

    def draw_logs(self):
        for i, log in enumerate(self.logs):
            arcade.draw_text(log, 10, SCREEN_HEIGHT - i * 12,
                             arcade.color.BLACK, 10, multiline=False, width=100)

    def add_log(self, log):
        if len(self.logs) < 30:
            self.logs.insert(0, log)
        else:
            self.logs.pop(len(self.logs)-1)
            self.logs.insert(0, log)

