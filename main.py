from Menu import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "193530 Łukasz Walczak"



def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
