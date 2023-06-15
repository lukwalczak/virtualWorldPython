from Organism import Organism


class Plant(Organism):
    def __init__(self, strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view):
        super().__init__(strength, initiative, pos_x, pos_y, age, organism_char, organism_name, game, game_view)
    
