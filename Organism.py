import MainGame


class Organism:
    def __init__(self, strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view):
        self.strength = strength
        self.initiative = initiative
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.age = age
        self.organism_char = organism_char
        self.organism_name = organism_name
        self.game = game
        self.game_view = game_view

    def draw(self):
        self.game_view.change_char_game_point_at_xy(self.pos_x, self.pos_y, self.organism_char)

    def check_adjacent_free_spaces(self):
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                if self.game.get_organism_at_xy(self.pos_x + i, self.pos_y + j):
                    return False

    def action(self, dx, dy):
        pass


    def collision(self, colliding_organism):
        return False

    def check_move(self, dx, dy):
        if (self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy) is None and
                0 <= self.pos_y + dy < self.game.height - 1 and
                0 <= self.pos_x + dx < self.game.width-1):
            return True
        else:
            return False

    def move(self, dx, dy):
        if self.check_move(dx, dy):
            self.pos_y += dy
            self.pos_x += dx


    def compare_to(self, other):
        if self.initiative > other.initiative:
            return -1
        elif self.initiative < other.initiative:
            return 1
        elif self.age >= other.age:
            return -1
        else:
            return 1
