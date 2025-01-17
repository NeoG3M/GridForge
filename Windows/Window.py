import pygame.sprite

from Button import Button as Btn
from CONSTANTS import *


class Window:
    def __init__(self, parent, size: tuple[float, float] = DISPLAY_SIZE,
                 background: pygame.Color | pygame.sprite.Sprite | str = pygame.color.Color('black'),
                 delta: tuple[int, int] = (0, 0)):

        from Windows import (GameWindow, Settings, AchievementWindow, StartWindow)
        from mainFlow import GridForge
        self.parent: GridForge = parent
        self.surface = pygame.Surface(size)
        self.add_back(background)
        self.events = {'Выйти': terminate, 'Играть': lambda: self.switch_window(GameWindow(self.parent)),
                       'Настройки': lambda: self.switch_window(Settings(self.parent, (600, 600))),
                       'Достижения': lambda: self.switch_window(AchievementWindow(self.parent)),
                       'Главное меню': lambda: self.switch_window(StartWindow(self.parent))}
        self.buttons = self.create_buttons()
        self.delta = delta
        self.draw()

    def update(self, event: pygame.event):
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            x1, y1 = self.buttons.sprites()[0].rect.x + self.delta[0], self.buttons.sprites()[0].rect.y + self.delta[1]
            width, height = self.buttons.sprites()[0].rect.size
            if x1 <= x <= x1 + width and y1 <= y <= y1 + height:
                self.events['Главное меню']()

    def add_back(self, background: str | pygame.sprite.Sprite | pygame.Color):
        if isinstance(background, str):
            background = pygame.Color(background)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            self.surface.blit(background.image, self.delta)

    def switch_window(self, new_window):
        self.parent.switch_window(new_window)

    def create_buttons(self):
        buttons = pygame.sprite.Group()
        Btn(self.surface, "Выйти", (self.surface.get_rect().width - 160, 20), (150, 50), pygame.Color("orange"),
            buttons)
        return buttons

    def draw(self):
        self.buttons.draw(self.surface)
        self.parent.screen.blit(self.surface, self.delta)
