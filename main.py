import pygame

import constants


#   ____ _
#  / ___| | __ _ ___ ___  ___  ___
# | |   | |/ _` / __/ __|/ _ \/ __|
# | |___| | (_| \__ \__ \  __/\__ \
#  \____|_|\__,_|___/___/\___||___/

# Object
# --> Item
# --> Tile
# --> Entity
#     --> Player
#     --> NPC
#         --> Shopkeep
#     --> Monster

class Object:
    """The base object class for everything in the game."""
    pass


class Item(Object):
    """A wrapper class for items in the game."""
    pass


class Tile(Object):
    """The main class for all tiles in the game.
    """
    def __init__(self, passable=True, block_sight=False):
        self.passable = passable
        self.block_sight = block_sight


class Entity(Object):
    pass


class Player(Entity):
    pass


class NPC(Entity):
    pass


class Monster(Entity):
    pass


class Shopkeep(NPC):
    pass


#  _____                   _
# (____ \                 (_)
#  _   \ \ ____ ____ _ _ _ _ ____   ____
# | |   | / ___) _  | | | | |  _ \ / _  |
# | |__/ / |  ( ( | | | | | | | | ( ( | |
# |_____/|_|   \_||_|\____|_|_| |_|\_|| |
#                                 (_____|

def draw_window():
    global SURFACE_MAIN

    # Clear the window
    SURFACE_MAIN.fill(constants.BACKGROUND_COLOR)

    # Draw background

    # Draw player
    SURFACE_MAIN.blit(constants.S_PLAYER, (0, 0))

    # Update display
    pygame.display.flip()


def draw_map(map_):
    pass


# ___  ___
# |  \/  |
# | .  . | __ _ _ __
# | |\/| |/ _` | '_ \
# | |  | | (_| | |_) |
# \_|  |_/\__,_| .__/
#              | |
#              |_|

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[Tile() for y in range(0, height)] for x in width]


#   ______
#  / _____)
# | /  ___  ____ ____   ____
# | | (___)/ _  |    \ / _  )
# | \____/( ( | | | | ( (/ /
#  \_____/ \_||_|_|_|_|\____)

def game_main_loop():

    running = True
    frame = 0

    while running:
        # print(frame)
        frame += 1

        # Get inputs
        try:
            events = pygame.event.get()

            for event in events:
                print(event.type)
                if event.type == pygame.QUIT:
                    running = False

        except KeyboardInterrupt:
            running = False

        # Process inputs

        # Draw game

        draw_window()

    pygame.quit()
    exit()


def game_init():

    global SURFACE_MAIN

    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))


#  ██▀███      █    ██     ███▄    █
# ▓██ ▒ ██▒    ██  ▓██▒    ██ ▀█   █
# ▓██ ░▄█ ▒   ▓██  ▒██░   ▓██  ▀█ ██▒
# ▒██▀▀█▄     ▓▓█  ░██░   ▓██▒  ▐▌██▒
# ░██▓ ▒██▒   ▒▒█████▓    ▒██░   ▓██░
# ░ ▒▓ ░▒▓░   ░▒▓▒ ▒ ▒    ░ ▒░   ▒ ▒
#   ░▒ ░ ▒░   ░░▒░ ░ ░    ░ ░░   ░ ▒░
#   ░░   ░     ░░░ ░ ░       ░   ░ ░
#    ░           ░                 ░

if __name__ == '__main__':
    game_init()

    game_main_loop()