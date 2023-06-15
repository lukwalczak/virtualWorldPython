from Organism import Organism
import conf
import random
import Human
from Plant import Plant


class Animal(Organism):
    def __init__(self, strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view):
        super().__init__(strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view)
        self.breed_cooldown = conf.BREEDCOOLDOWN

    def breed(self):
        for i in range(-1, 2, 2):
            if self.game.get_organism_at_xy(self.pos_x + i, self.pos_y) is None:
                self.game.generate_organism_at_xy((self.pos_x + i), self.pos_y, self.organism_name)
                return

        for i in range(-1, 2, 2):
            if self.game.get_organism_at_xy(self.pos_x, self.pos_y + i) is None:
                self.game.generate_organism_at_xy((self.pos_x + i), self.pos_y, self.organism_name)
                return

    def fight(self, colliding_organism):
        if self.strength >= colliding_organism.strength:
            if colliding_organism.organism_char == 'H':
                if colliding_organism.ability_last_time > 0:
                    self.add_reflection_log(colliding_organism)
                    return False
                else:
                    self.game.human.alive = False
            if isinstance(colliding_organism, Animal) and colliding_organism.did_reflect(self):
                return False
            if isinstance(colliding_organism, Plant):
                colliding_organism.collision(self)

            self.add_fight_log(colliding_organism, True)
            self.game.remove_organism(colliding_organism)
            return True
        else:
            self.add_fight_log(colliding_organism, False)
            self.game.remove_organism(self)
            return False

    def action(self, dx, dy):
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

            if return_counter == 32:
                return

            return_counter += 1

        if not self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy):
            self.move(dx, dy)
        elif self.collision(self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy)):
            self.move(dx, dy)
        return

    def collision(self, colliding_organism):
        if colliding_organism is None:
            return True
        if colliding_organism.organism_char == self.organism_char:
            if self.breed_cooldown == 0 and colliding_organism.breed_cooldown == 0:
                self.breed_cooldown = 10
                colliding_organism.breed_cooldown = 10
                self.breed()
                return False

        if self.fight(colliding_organism):
            return True

        return False

    def increase_strength(self):
        self.strength += 3

    def did_reflect(self, colliding_organism):
        return False

    def add_move_log(self, dx, dy):
        log = self.organism_name + " moved to " + (self.pos_x+dx) + " " + (self.pos_y+dy)
        self.game.add_log(log)

    def add_fight_log(self, colliding_organism, won):
        if won:
            log = self.organism_name + " killed " + colliding_organism.organism_name
        else:
            log = self.organism_name + " was killed by " + colliding_organism.organism_name
        self.game.add_log(log)

    def add_breed_log(self):
        log = self.organism_name + " has been born"
        self.game.add_log(log)

    def add_reflection_log(self, colliding_organism):
        log = colliding_organism.organism_name + " reflected " + self.organism_name + " attack"
        self.game.add_log(log)
