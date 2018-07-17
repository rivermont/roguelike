import pygame

import constants

# Object
# --> Item
# --> Tile
#     --> SolidTile
# --> Entity
#     --> Player
#     --> NPC
#         --> Shopkeep
#     --> Monster


class Object():
    pass


class Item(Object):
    pass


def draw_window():
    global SURFACE_MAIN

    # Clear the window
    SURFACE_MAIN.fill(constants.BACKGROUND_COLOR)

    # Draw background

    # Draw player
    SURFACE_MAIN.blit(constants.S_PLAYER, (0, 0))

    # Update display
    pygame.display.flip()


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


if __name__ == '__main__':
    game_init()

    game_main_loop()