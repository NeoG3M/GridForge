import pygame
from mainFlow import GridForge

ALL_SPRITES = pygame.sprite.Group()


def main():
    gf = GridForge()
    gf.run_game()


if __name__ == '__main__':
    main()
