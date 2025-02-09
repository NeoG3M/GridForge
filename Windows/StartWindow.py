import pygame

from Windows.Window import Window
from CONSTANTS import ALL_SPRITES


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load("data/start_window_screen.png")
    __background_sprite.rect = __background_sprite.image.get_rect()
    """This class realises the start window of the game"""

    def __int__(self, parent):
        """This class wait for user action,
        then closes himself and open MenuWindow"""
        super().__init__(parent, background=self.__background_sprite)
        self.add_background(self.__background_sprite)
        self.screen.blit(self.__background_sprite.image, (0, 0))

    def update(self, event):
        """This method just closes StartWindow and open MenuWindow"""
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            pygame.event.post(pygame.event.Event(self.gridforge.get_event("SWITCH_WINDOW"),
                                                 name="menu", arg=self.gridforge))
        self.screen.blit(self.__background_sprite.image, (0, 0))