from sys import exit

import pygame
from statistic import *

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1200, 700
FPS = 100

tower_group = []
enemy_group = []
all_sprites = pygame.sprite.Group()


def terminate():
    pygame.quit()
    pygame.mixer.quit()
    exit()


GAME_EVENTS = {'SWITCH_WINDOW': pygame.USEREVENT + 3, 'SHUTDOWN': pygame.USEREVENT + 1,
               'DISPLAY_TEXT_WINDOW': pygame.USEREVENT + 4,
               'PICK_UNIT': pygame.USEREVENT + 10, 'REACTOR_EXPLOSION': pygame.USEREVENT + 11,
               'TICK_UPDATE': pygame.USEREVENT + 100, 'GAME_WIN': pygame.USEREVENT + 12}

BASE_MUSIC_VOLUME = 0.4


def get_event(event):
    return GAME_EVENTS.get(event, None)


def raise_event(event: str, **kwargs):
    pygame.event.post(pygame.event.Event(get_event(event), **kwargs))

# __all__ = ['DISPLAY_SIZE', 'FPS', 'ALL_SPRITES', 'terminate']
