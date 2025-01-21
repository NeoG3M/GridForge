import pygame

from CONSTANTS import *


class Widget:
    def __init__(self, rect, color=pygame.Color('gray'), on_click=None):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.hovered = False  # Состояние наведения
        self.on_click = on_click

    def handle_event(self, event):
        """Обработка событий."""
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and self.on_click:
                self.on_click()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
