from sys import exit

import pygame


def terminate():
    pygame.quit()
    pygame.mixer.quit()
    exit()


DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1200, 700
FPS = 100
ALL_SPRITES = pygame.sprite.Group()
