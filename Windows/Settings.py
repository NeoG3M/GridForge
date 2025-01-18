import pygame

from CONSTANTS import DISPLAY_SIZE
from static_window_sprites import Button
from .Window import Window


class Settings(Window):
    def __init__(self, parent, size):
        self.delta = int(DISPLAY_SIZE[0] * 0.2), int(DISPLAY_SIZE[1] * 0.1)
        super().__init__(parent, size=size, delta=self.delta)

    def create_buttons(self):
        buttons = super().create_buttons()
        Button(self.surface, 'Основные', (self.surface.get_rect().width * 0.23, self.surface.get_rect().height * 0.2),
               (250, 70), (208, 122, 240), buttons)
        return buttons
