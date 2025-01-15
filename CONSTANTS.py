from sys import exit

import pygame

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1200, 700
FPS = 100
ALL_SPRITES = pygame.sprite.Group()


def terminate():
    pygame.quit()
    exit()


# __all__ = ['DISPLAY_SIZE', 'FPS', 'ALL_SPRITES', 'terminate']
