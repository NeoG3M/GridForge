import pygame

from Widgets.widget import Widget
from typing import Callable


class LevelPreview(Widget):
    def __init__(self, rect, background_color=pygame.Color("black"), border_color=pygame.Color("orange"),
                information="None", count_of_enemies=0, count_of_towers=0, rewards=None, on_click: Callable = None):
        super().__init__(rect, background_color, on_click)

        self.border_color = border_color
        self.information = information
        self.data = (count_of_enemies, count_of_towers, rewards)

        font = pygame.font.Font(None, int(self.rect.size[1] * 0.05))
        self.text = font.render(self.information, True, self.border_color)

    def draw(self, surface: pygame.Surface):
        """Отображение краткой информации об уровне"""

        pygame.draw.rect(surface, self.border_color, self.rect, 2)

        text_surface = pygame.Surface((self.rect.width, self.rect.height))
        text_surface.fill(self.color)
        text_surface.blit(self.text, (0, 0))
        surface.blit(text_surface, (self.rect.x, self.rect.y))

        enemy_font = pygame.font.Font(None, int(self.rect.size[1] * 0.05))
        enemy_text = enemy_font.render(f"Врагов: {self.data[0]}", True, self.border_color)
        surface.blit(enemy_text, (self.text.get_height() + 2, 0))

        tower_font = pygame.font.Font(None, int(self.rect.size[1] * 0.05))
        tower_text = tower_font.render(f"Башен возможно: {self.data[1]}", True, self.border_color)
        surface.blit(tower_text, (self.text.get_height() + 2, enemy_text.get_width() + 2))

        tower_font = pygame.font.Font(None, int(self.rect.size[1] * 0.05))
        tower_text = tower_font.render(f"Награды: {self.data[1]}", True, self.border_color)
        surface.blit(tower_text, (self.text.get_height() + 2,
                                  enemy_text.get_width() + tower_text.get_width() + 2))