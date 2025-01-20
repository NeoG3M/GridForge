import pygame.sprite

from CONSTANTS import *
from static_window_sprites.Button import Button as Btn


class Window:
    def __init__(self, parent, size: tuple[float, float] = DISPLAY_SIZE,
                 background: pygame.Color | pygame.sprite.Sprite | str | tuple = pygame.color.Color('black'),
                 delta: tuple[int, int] = (0, 0)):

        from mainFlow import GridForge
        from Windows import StartWindow

        self.parent: GridForge = parent
        self.surface = pygame.Surface(size)
        self.add_back(background)
        self.events = {'Выйти': terminate, 'Главное меню': lambda: self.switch_window(StartWindow(self.parent))}
        self.buttons = self.create_buttons()
        self.delta = delta
        self.local_events = dict()
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                x, y, width, height = button.rect.x, button.rect.y, button.rect.width, button.rect.height
                x += self.delta[0]
                y += self.delta[1]
                if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height:
                    self.local_events.get(button.text, lambda: None)()

    def add_back(self, background: str | pygame.sprite.Sprite | pygame.Color | tuple):
        if isinstance(background, str):
            background = pygame.Color(background)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            self.surface.blit(background.image, self.delta)
        elif isinstance(background, tuple):
            self.surface.fill(background)

    def switch_window(self, new_window):
        self.parent.switch_window(new_window)

    def create_buttons(self):
        buttons = pygame.sprite.Group()
        Btn(self.surface, "Выйти", (self.surface.get_rect().width - 160, 20), (150, 50), pygame.Color((208, 122, 240)),
            buttons)
        return buttons

    def draw(self):
        self.buttons.draw(self.surface)
        self.parent.screen.blit(self.surface, self.delta)
