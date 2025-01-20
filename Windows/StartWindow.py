import pygame

from CONSTANTS import ALL_SPRITES, DISPLAY_SIZE
from static_window_sprites import Button
from .Window import Window


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load(f"Windows/Windows_back/StartWindow.jpg")
    __background_sprite.rect = __background_sprite.image.get_rect()
    """
    This class realizes a start window of the game, where you can 
    """

    def __init__(self, parent):
        self.delta = 0, 0
        super().__init__(parent, background=self.__background_sprite)
        self.buttons = self.create_buttons()
        from Windows import (GameWindow, Settings, AchievementWindow, WorkshopWindow)
        self.local_events = {key: value for key, value in
                             ({'Играть': lambda: self.switch_window(GameWindow(self.parent)),
                               'Настройки': lambda: self.switch_window(Settings(self.parent, (600, 600))),
                               'Достижения': lambda: self.switch_window(AchievementWindow(self.parent)),
                               'Мастерская': lambda: self.switch_window(
                                   WorkshopWindow(self.parent))} | self.events).items()}

    def create_buttons(self) -> pygame.sprite.Group:
        """
        This method create buttons for this window
        :return: Group of buttons
        """
        buttons = super().create_buttons()

        Button(self.surface, "Мастерская", (int(DISPLAY_SIZE[0] * 0.72), int(DISPLAY_SIZE[1] * 0.65)), (200, 90),
               (208, 122, 240), buttons)
        Button(self.surface, "Достижения", (int(DISPLAY_SIZE[0] * 0.72), int(DISPLAY_SIZE[1] * 0.80)), (200, 90),
               (208, 122, 240), buttons)
        Button(self.surface, "Настройки", (10, 20), (150, 50), pygame.Color((208, 122, 240)), buttons)
        Button(self.surface, "Играть", (int(DISPLAY_SIZE[0] * 0.35), int(DISPLAY_SIZE[1] * 0.6)), (250, 70),
               pygame.Color((208, 122, 240)), buttons)
        # (167, 96, 56)
        return buttons
