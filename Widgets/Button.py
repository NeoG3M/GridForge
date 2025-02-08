from math import ceil

import pygame
from typing import Callable
from .widget import Widget


class Button(Widget):
    def __init__(self, rect: tuple, color: pygame.Color, text: str, text_color: pygame.Color = pygame.Color('black'),
                 on_click: Callable = None):
        """Инициализация кнопки"""

        super().__init__(rect, color, on_click)

        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.text_color = text_color

    def draw(self, surface: pygame.Surface):
        """Рисование кнопки"""

        super().draw(surface)
        text_surface = pygame.Surface((self.rect.width, self.rect.height))
        text_surface.fill(self.color)

        font = pygame.font.Font(None, int(self.rect.size[1] * 0.65))
        text = font.render(self.text, True, self.text_color)
        text_position_x = self.rect.width // 2 - text.get_width() // 2
        text_position_y = self.rect.height // 2 - text.get_height() // 2

        frame_border = ceil(5 * (self.rect.width / 200))

        text_surface.blit(text, (text_position_x, text_position_y))
        pygame.draw.rect(
            text_surface, self.text_color,
            (frame_border, frame_border,
            self.rect.width - frame_border * 2,
            self.rect.height - frame_border * 2), 2
        )
        surface.blit(text_surface, (self.rect.x, self.rect.y))
