from Organism import Organism
import random


class Plant(Organism):
    def __init__(self, strength, pos_x, pos_y, age, organism_char, organism_name, game, game_view):
        super().__init__(strength, 0, pos_x, pos_y, age, organism_char, organism_name, game, game_view)
    
    def action(self, dx, dy):
        breed_chance = random.randint(0, 20)
        if breed_chance == 0:
            for i in range(-1, 2, 2):
                if self.game.get_organism_at_xy(self.pos_x+i, self.pos_y) is None and self.check_move(i, 0):
                    self.game.generate_organism_at_xy((self.pos_x + i), self.pos_y, self.organism_name)
                    return
                if self.game.get_organism_at_xy(self.pos_x, self.pos_y + i) is None and self.check_move(0, i):
                    self.game.generate_organism_at_xy((self.pos_x + i), self.pos_y, self.organism_name)
                    return
