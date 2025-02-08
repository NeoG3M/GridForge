import pygame

from Widgets.widget import Widget
from typing import Callable


class LevelPreview(Widget):
    def __init__(self, rect, background_color=pygame.Color("black"), border_color=pygame.Color("orange"),
                information=None, on_click: Callable = None):
        super().__init__(rect, background_color, on_click)

        self.border_color = border_color
        self.information = information

    def draw(self, surface: pygame.Surface):
        """Отображение краткой информации об уровне"""

        pygame.draw.rect(surface, self.border_color, self.rect, 2)