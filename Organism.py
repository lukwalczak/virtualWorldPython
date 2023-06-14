import World


class Organism:
    def __init__(self, strength, initiative, pos_x, pos_y, age, organism_char, breed_cooldown, organism_name, world):
        self.strength = strength
        self.initiative = initiative
        self.posX = pos_x
        self.posY = pos_y
        self.age = age
        self.organism_char = organism_char
        self.breed_cooldown = breed_cooldown
        self.organism_name = organism_name
        self.world = world

    def draw(self):
        pass

    def check_adjacent_free_spaces(self):
        pass

    def action(self):
        pass
