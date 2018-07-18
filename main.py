#!/usr/bin/env python3
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
#     --> Creature
#          --> NPC
#              --> Shopkeep
#          --> Monster

class Object:
    """The base object class for everything in the game."""
    pass


class Item(Object):
    """Base class for items in the game."""

    def __init__(self):
        super(Item, self).__init__()
        pass


class Tile(Object):
    """
    The main class for all tiles in the game.
    This can apply to basic tiles like floors and walls,
    or to other things such as placed items.

    Args:
        passable (bool): Whether entities can pathfind and walk on this tile.
        block_sight (bool): Whether line of sight is stopped by this tile.
    """

    def __init__(self, passable=True, block_sight=False):
        super(Tile, self).__init__()
        self.passable = passable
        self.block_sight = block_sight


class Entity(Object):
    """
    Base class for entities in the game.
    Entities can move, interact with tiles, items and other entities and take damage.

    Args:
        x (int): The map coordinate (not pixel coordinate) of the entity at creation.
        y (int): The map coordinate (not pixel coordinate) of the entity at creation.
        sprite (pygame.Surface): An image.
    """

    def __init__(self, x, y, sprite):
        super(Entity, self).__init__()
        self.x = x
        self.y = y
        self.sprite = sprite

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x*constants.TILE_SIZE, self.y*constants.TILE_SIZE))

    def move(self, dx, dy):
        if GAME_MAP.map[self.x+dx][self.y+dy].passable:
            self.x += dx
            self.y += dy
        else:
            # Can't move onto that tile
            pass


class Player(Entity):
    """The player character."""

    def __init__(self, x, y):
        super(Player, self).__init__(x, y, constants.S_PLAYER)


class Creature(Entity):
    """
    Wrapper class for entities other than the player character.
    Handles things such as AI.

    Args:
        name (str): A name for the creature.
        hp (int): Number of hit points the creature starts with.
    """

    def __init__(self, x, y, sprite, name="", hp=-1):
        super(Creature, self).__init__(x, y, sprite)
        self.name = name
        self.hp = hp

    # TODO: Attack function

    # TODO: Death behaviour

    # TODO: AI


class Monster(Creature):
    """Any creature passively hostile towards the player character."""

    def __init__(self, x, y):
        sprite = None
        super(Monster, self).__init__(x, y, sprite)


class NPC(Creature):
    """Non-hostile characters in game that the player can interact with."""

    def __init__(self, x, y, sprite=None):
        # TODO: Need default NPC sprite
        super(NPC, self).__init__(x, y, sprite)

    # TODO: Dialogue AI and trading


class Shopkeep(NPC):
    """
    TODO
    """

    def __init__(self, x, y):
        sprite = None
        super(Shopkeep, self).__init__(x, y, sprite)


#  _____                   _
# (____ \                 (_)
#  _   \ \ ____ ____ _ _ _ _ ____   ____
# | |   | / ___) _  | | | | |  _ \ / _  |
# | |__/ / |  ( ( | | | | | | | | ( ( | |
# |_____/|_|   \_||_|\____|_|_| |_|\_|| |
#                                 (_____|

def draw_game():
    """Draws the game window."""

    # Clear the window
    SURFACE_MAIN.fill(constants.BACKGROUND_COLOR)

    draw_map(GAME_MAP)

    # Draw entities
    PLAYER.draw()

    # Update display
    pygame.display.flip()


def draw_map(map_):
    """
    Draws the map onto the main surface.

    Args:
        map_ (Map):
    """
    for x in range(0, map_.width):
        for y in range(0, map_.height):
            if map_.map[x][y].passable:
                SURFACE_MAIN.blit(constants.S_FLOOR, (x*constants.TILE_SIZE, y*constants.TILE_SIZE))
            else:
                SURFACE_MAIN.blit(constants.S_WALL, (x*constants.TILE_SIZE, y*constants.TILE_SIZE))


# ___  ___
# |  \/  |
# | .  . | __ _ _ __
# | |\/| |/ _` | '_ \
# | |  | | (_| | |_) |
# \_|  |_/\__,_| .__/
#              | |
#              |_|

class Map:
    """
    TODO
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[Tile() for y in range(0, height)] for x in range(0, width)]

    def get_tile(self, tile_x, tile_y):
        return self.map[tile_x][tile_y]


#   ______
#  / _____)
# | /  ___  ____ ____   ____
# | | (___)/ _  |    \ / _  )
# | \____/( ( | | | | ( (/ /
#  \_____/ \_||_|_|_|_|\____)

def game_main_loop():
    """
    TODO
    """
    running = True
    while running:

        print(int(clock.get_fps()))

        try:
            # Get user inputs
            events = pygame.event.get()

            # Process inputs
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Arrow key movement
                    if event.key == pygame.K_UP:
                        PLAYER.move(0, -1)
                    if event.key == pygame.K_DOWN:
                        PLAYER.move(0, 1)
                    if event.key == pygame.K_LEFT:
                        PLAYER.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        PLAYER.move(1, 0)

        except KeyboardInterrupt:
            running = False

        # Draw the game window
        draw_game()

        clock.tick()

    pygame.quit()
    exit()


def game_init():
    """
    TODO
    """
    global SURFACE_MAIN, GAME_MAP, PLAYER, clock

    clock = pygame.time.Clock()

    pygame.init()

    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))

    GAME_MAP = Map(constants.DEFAULT_MAP_W, constants.DEFAULT_MAP_H)

    PLAYER = Player(0, 0)


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