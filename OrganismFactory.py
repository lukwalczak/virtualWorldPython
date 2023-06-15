from Plants import Grass,Dandelion,Nightshade,Pineborsch,Guarana
from Animals import Wolf,Fox,Sheep,Antelope,Turtle,CyberSheep


def createOrganism(name, rand_x, rand_y, game, game_view):
    o = None
    if name == "WOLF":
        o = Wolf(rand_x, rand_y, game, game_view)
    if name == "FOX":
        o = Fox(rand_x, rand_y, game, game_view)
    if name == "SHEEP":
        o = Sheep(rand_x, rand_y, game, game_view)
    if name == "ANTELOPE":
        o = Antelope(rand_x, rand_y, game, game_view)
    if name == "TURTLE":
        o = Turtle(rand_x, rand_y, game, game_view)
    if name == "CYBERSHEEP":
        o = CyberSheep(rand_x, rand_y, game, game_view)
    if name == "GRASS":
        o = Grass(rand_x, rand_y, game, game_view)
    if name == "DANDELION":
        o = Dandelion(rand_x, rand_y, game, game_view)
    if name == "NIGHTSHADE":
        o = Nightshade(rand_x, rand_y, game, game_view)
    if name == "PINEBORSCH":
        o = Pineborsch(rand_x, rand_y, game, game_view)
    if name == "GUARANA":
        o = Guarana(rand_x, rand_y, game, game_view)
    if o is None:
        return
    else:
        game.organisms.append(o)
