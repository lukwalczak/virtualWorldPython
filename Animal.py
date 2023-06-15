from Organism import Organism
import conf
import random

class Animal(Organism):
    def __init__(self, strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view):
        super().__init__(strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view)
        self.breed_cooldown = conf.BREEDCOOLDOWN

    def action(self):
        dx = 0
        dy = 0
        return_counter = 0
        self.age += 1
        moved = False

        if self.check_adjacent_free_spaces():
            return

        if self.breed_cooldown > 0:
            self.breed_cooldown -= 1

        while not moved:
            direction = random.randint(0, 1)

            if direction == 0 and (self.pos_y - 1 >= 0 or self.pos_y < self.game.height -1):
                direction = random.randint(0, 1)

                if direction == 0 and self.pos_y - 1 >= 0:
                    dy -= 1
                    moved = True
                elif direction == 1 and self.pos_y + 1 < self.game.height - 1:
                    dy += 1
                    moved = True

            if direction == 1 and (self.pos_x - 1 >= 0 or self.pos_x < self.game.width - 1):
                direction = random.randint(0, 1)

                if direction == 0 and self.pos_x - 1 >= 0:
                    dx -= 1
                    moved = True
                elif direction == 1 and self.pos_x + 1 < self.game.width - 1:
                    dx += 1
                    moved = True


