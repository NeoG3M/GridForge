import pygame

from Button import Button
from default_constaints import ALL_SPRITES
from .Window import Window


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load(f"Windows/Sprites/StartWindow.png").convert_alpha()
    __background_sprite.rect = __background_sprite.image.get_rect()
    """
    This class realizes a start window of the game, where you can 
    """

    def __init__(self):
        super().__init__(background=self.__background_sprite)
        buttons = pygame.sprite.Group()
        Button(self.surface, "Выйти", (10, 10), (100, 30), pygame.Color("orange"), buttons)
        Button(self.surface, "Мастерская", (10, 40), (600, 130), (167, 96, 56), buttons)
        Button(self.surface, "Достижения", (10, 250), (600, 130), (167, 96, 56), buttons)
        Button(self.surface, "Настройки", (10, 460), (200, 70), pygame.Color("orange"), buttons)
        Button(self.surface, "Выйти", (10, 540), (300, 100), pygame.Color("orange"), buttons)
        buttons.draw(self.surface)
