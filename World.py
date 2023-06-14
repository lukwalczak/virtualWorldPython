from Organism import Organism


class World:
    def __init__(self, width, height):
        self.logs = []
        self.organisms = []
        self.width = width
        self.height = height
        self.game_turn = 0
        #self.human = Human()
        self.organism = Organism(10, 10, 10, 10, 10, 10, 10, 10, self)

