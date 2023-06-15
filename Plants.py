from Plant import Plant
import conf
import random
from Animal import Animal
from Human import Human


class Grass(Plant):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.GRASSSTR, x, y, 0, conf.GRASSCHAR, conf.GRASSFULLNAME, game, game_view)


class Dandelion(Plant):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.DANDELIONSTR, x, y, 0, conf.DANDELIONCHAR, conf.DANDELIONFULLNAME, game, game_view)

    def action(self, dx, dy):
        super().action(dx, dy)
        super().action(dx, dy)
        super().action(dx, dy)


class Guarana(Plant):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.GUARANASTR, x, y, 0, conf.GUARANACHAR, conf.GUARANAFULLNAME, game, game_view)

    def collision(self, colliding_organism):
        if isinstance(colliding_organism, Animal):
            colliding_organism.increase_strength()
        return False


class Nightshade(Plant):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.NIGHTSHADESTR, x, y, 0, conf.NIGHTSHADECHAR, conf.NIGHTSHADEFULLNAME, game, game_view)

    def collision(self, colliding_organism):
        if isinstance(colliding_organism,Human) and colliding_organism.ability_last_time > 0:
            return True
        self.game.remove_organism(colliding_organism)
        self.game.remove_organism(self)
        return False


class Pineborsch(Plant):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.PINEBORSCHSTR, x, y, 0, conf.PINEBORSCHCHAR, conf.PINEBORSCHFULLNAME, game, game_view)

    def collision(self, colliding_organism):
        if isinstance(colliding_organism, Human) and colliding_organism.ability_last_time > 0:
            return True
        self.game.remove_organism(colliding_organism)
        self.game.remove_organism(self)
        return False

    def action(self, dx, dy):
        for i in range(-1,2,2):
            organism = self.game.get_organism_at_xy(self.pos_x + i, self.pos_y)
            if organism is not None:
                if isinstance(organism, Human) and organism.ability_last_time > 0:
                    continue
                self.game.remove_organism(organism)

        for i in range(-1,2,2):
            organism = self.game.get_organism_at_xy(self.pos_x, self.pos_y + i)
            if organism is not None:
                if isinstance(organism, Human) and organism.ability_last_time > 0:
                    continue
                self.game.remove_organism(organism)

