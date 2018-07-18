import pygame
pygame.init()


def load_img(name):
    """
    Load an image from the assets folder.

    Args:
        name (str): Simple name of the image to load, without extension.
    """
    try:
        img = pygame.image.load('assets/{0}.png'.format(name))
    except pygame.error:
        img = pygame.image.load('./assets/{0}.png'.format(name))

    return img


GAME_WIDTH = 800
GAME_HEIGHT = 600

DEFAULT_MAP_H = 128
DEFAULT_MAP_TILE_H = 8
DEFAULT_MAP_TILE_W = 8
DEFAULT_MAP_W = 128

TILE_SIZE = 16

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY1 = (100, 100, 100)

BACKGROUND_COLOR = COLOR_BLACK

# Sprites

S_PLAYER = load_img('angel')
S_FLOOR = load_img('dirt1')
S_WALL = load_img('dirt2')
