import pygame
pygame.init()


def load_img(name):
    """
    Load an image from the assets folder.
    Also scales to image to the set tile size.

    Args:
        name (str): Simple name of the image to load, without extension.
    """
    try:
        img = pygame.image.load('assets/{0}.png'.format(name))
    except pygame.error:
        img = pygame.image.load('./assets/{0}.png'.format(name))

    return pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))


GAME_WIDTH = 1024
GAME_HEIGHT = 640

TILE_SIZE = 32

# Sanity check
if GAME_WIDTH % TILE_SIZE or GAME_HEIGHT % TILE_SIZE:
    print('[ERROR]: Tile size does not match the height of the window!')
    exit()

DEFAULT_MAP_H = int(GAME_HEIGHT / TILE_SIZE)
DEFAULT_MAP_W = int(GAME_WIDTH / TILE_SIZE)

# Colors
COLOR_BLACK = (0, 0, 0)
# COLOR_WHITE = (255, 255, 255)
# COLOR_GREY1 = (100, 100, 100)

BACKGROUND_COLOR = COLOR_BLACK

# Sprites

S_PLAYER = load_img('angel')
S_FLOOR = load_img('vz_05')
S_WALL = load_img('dirt2')
