from Animal import Animal
import conf
import random


class Sheep(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.SHEEPSTR,conf.SHEEPINITIATIVE,x,y,0,conf.SHEEPCHAR, conf.SHEEPFULLNAME, game, game_view)


class Wolf(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.WOLFSTR,conf.WOLFINITIATIVE,x,y,0,conf.WOLFCHAR, conf.WOLFFULLNAME, game, game_view)


class Turtle(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.TURTLESTR,conf.TURTLEINITIATIVE,x,y,0,conf.TURTLECHAR, conf.TURTLEFULLNAME, game, game_view)

    def action(self, dx, dy):
        chance = random.randint(0, 4)
        if chance == 0:
            super().action(dx, dy)
            return
        self.age += 1
        return


class Antelope(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.ANTELOPESTR, conf.ANTELOPEINITIATIVE, x, y, 0, conf.ANTELOPECHAR, conf.ANTELOPEFULLNAME, game,
                         game_view)

    def action(self, dx, dy):
        super().action(0, 0)
        super().action(0, 0)


class Fox(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.FOXSTR, conf.FOXINITIATIVE, x, y, 0, conf.FOXCHAR, conf.FOXFULLNAME, game,
                         game_view)

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

            if direction == 0 and (self.pos_y - 1 >= 0 or self.pos_y < self.game.height - 1):
                direction = random.randint(0, 1)
                if direction == 0 and self.pos_y - 1 >= 0:
                    colliding_organism = self.game.get_organism_at_xy(self.pos_x, self.pos_y - 1)
                    if colliding_organism is None or self.strength >= colliding_organism.strength:
                        dy -= 1
                        moved = True
                elif direction == 1 and self.pos_y + 1 < self.game.height - 1:
                    colliding_organism = self.game.get_organism_at_xy(self.pos_x, self.pos_y + 1)
                    if colliding_organism is None or self.strength >= colliding_organism.strength:
                        dy += 1
                        moved = True
            if direction == 1 and (self.pos_x - 1 >= 0 or self.pos_x < self.game.width - 1):
                direction = random.randint(0, 1)
                if direction == 0 and self.pos_x - 1 >= 0:
                    colliding_organism = self.game.get_organism_at_xy(self.pos_x - 1, self.pos_y)
                    if colliding_organism is None or self.strength >= colliding_organism.strength:
                        dx -= 1
                        moved = True
                elif direction == 1 and self.pos_x + 1 < self.game.width - 1:
                    colliding_organism = self.game.get_organism_at_xy(self.pos_x + 1, self.pos_y)
                    if colliding_organism is None or self.strength >= colliding_organism.strength:
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


class CyberSheep(Animal):
    def __init__(self, x, y, game, game_view):
        super().__init__(conf.CYBERSHEEPSTR, conf.CYBERSHEEPINITIATIVE, x, y, 0, conf.CYBERSHEEPCHAR, conf.CYBERSHEEPFULLNAME, game,
                         game_view)

    def action(self, dx, dy):
        closest = None
        closest_dist = float('inf')
        for o in self.game.organisms:
            if o.organism_name == "PINEBORSCH":
                distance = abs(o.pos_x - self.pos_x) + abs(o.pos_y - self.pos_y)
                if distance < closest_dist:
                    closest = o
                    closest_dist = distance

        if closest is None:
            super().action(0, 0)
        else:
            if self.pos_x > closest.pos_x:
                dx = -1
            elif self.pos_x < closest.pos_x:
                dx = 1
            elif self.pos_y > closest.pos_y:
                dy = -1
            elif self.pos_y < closest.pos_y:
                dy = 1
        if not self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy):
            self.move(dx, dy)
        elif self.collision(self.game.get_organism_at_xy(self.pos_x + dx, self.pos_y + dy)):
            self.move(dx, dy)
        return

    def fight(self, colliding_organism):
        if colliding_organism.organism_char == "P":
            self.add_fight_log(colliding_organism, True)
            self.game.remove_organism(colliding_organism)
            return True
        else:
            super().fight(colliding_organism)
