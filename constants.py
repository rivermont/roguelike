import pygame

pygame.init()

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

S_PLAYER = pygame.image.load('./assets/angel.png')
S_FLOOR = pygame.image.load('./assets/dirt1.png')
S_WALL = pygame.image.load('./assets/dirt2.png')
