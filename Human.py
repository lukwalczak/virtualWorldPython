from Organism import Organism
import conf
from Animal import Animal
from Plant import Plant


class Human(Animal):
    def __init__(self, game, game_view):
        super().__init__(conf.HUMAN_STR, conf.HUMAN_INIT, conf.HUMAN_X, conf.HUMAN_Y,
                         0, conf.HUMAN_CHAR, conf.HUMAN_NAME, game, game_view)
        self.alive = True
        self.ability_last_time = 0
        self.ability_cooldown = 0

    def action(self, dx, dy):
        if not self.alive:
            return
        colliding_organism = self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy)
        print(colliding_organism)
        if dx != 0 and 0 <= self.pos_x + dx < self.game.width:
            if colliding_organism is None or self.collision(colliding_organism):
                self.move(dx, dy)
                self.age += 1
                return True
            elif self.ability_last_time > 0:
                self.age += 1
                return True
            else:
                return False

        if dy != 0 and 0 <= self.pos_y + dy < self.game.height:
            if colliding_organism is None or self.collision(colliding_organism):
                self.move(dx, dy)
                self.age += 1
                return True
            elif self.ability_last_time > 0:
                self.age += 1
                return True
            else:
                return False

        return False

    def fight(self, colliding_organism):
        if colliding_organism is None:
            return True
        if self.strength >= colliding_organism.strength:
            if isinstance(colliding_organism, Animal) and colliding_organism.did_reflect(self):
                return False
            if isinstance(colliding_organism, Plant):
                colliding_organism.collision(self)

            self.add_fight_log(colliding_organism, True)
            self.game.remove_organism(colliding_organism)
            return True
        else:
            if self.ability_last_time > 0:
                self.add_reflection_log(colliding_organism)
                return True
            else:
                self.alive = False
                self.add_fight_log(colliding_organism, False)
                self.game.remove_organism(self)
            return False

    def collision(self, colliding_organism):
        if self.fight(colliding_organism):
            return True
        else:
            return False
