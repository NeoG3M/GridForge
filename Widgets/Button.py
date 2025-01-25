import pygame

from Widgets.widget import Widget
from math import ceil


class Button(Widget):
    def __init__(self, rect, color, text, text_color=pygame.Color('black'), on_click=None):
        """Инициализация кнопки"""

        super().__init__(rect, color, on_click)

        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
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

    def handle_event(self, event):
        """Обработка события нажатия на кнопку"""

        if (event.type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(event.pos)):
            pass