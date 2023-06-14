import arcade
from Menu import Menu

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "193530 Łukasz Walczak"


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,resizable=True)
    arcade.set_window(window)
    main_view = Menu()
    window.show_view(main_view)
    arcade.run()


if __name__ == "__main__":
    main()
