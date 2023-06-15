from Organism import Organism
import conf


class Human(Organism):
    def __init__(self, game, game_view):
        super().__init__(conf.HUMAN_STR, conf.HUMAN_INIT, conf.HUMAN_X, conf.HUMAN_Y,
                         0, conf.HUMAN_CHAR, conf.HUMAN_NAME, game, game_view)
        self.alive = True

    def action(self, dx, dy):
        print("human action")
        if dx != 0 and 0 <= self.pos_x + dx < self.game.width:
            self.pos_x += dx
            print("x")
            return

        if dy != 0 and 0 <= self.pos_y + dy < self.game.height:
            self.pos_y += dy
            print("y")
            return
