import os
from sys import exit

import pygame

from Widgets.widget import Widget


class Icon(pygame.sprite.Sprite, Widget):
    def __init__(self, position: tuple[int, int], image_name: str, size, *group):
        super().__init__(*group)

        self.image = load_image(image_name)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
