import pygame

from Widgets.widget import Widget
from typing import Callable


class LevelPreview(Widget):
    def __int__(self, rect, background_color=pygame.Color("black"), border_color=pygame.Color("orange"),
                information=None, on_click: Callable = None):
        super().__int__(rect, background_color, on_click)

        self.border_color = border_color
        self.information = information

    def draw(self, surface: pygame.Surface):
        """Отображение краткой информации об уровне"""

        level_surface = pygame.Surface((self.rect.width, self.rect.height))
        pygame.draw.rect(surface, pygame.Color("orange"), self.rect, 4)
        surface.blit(level_surface, (self.rect.x, self.rect.y))