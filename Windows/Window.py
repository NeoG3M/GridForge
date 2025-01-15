from CONSTANTS import *
from Windows import (GameWindow, Settings, AchievementWindow)

class Window:
    def __init__(self, size: tuple[float, float] = DISPLAY_SIZE, background=pygame.color.Color('black')):
        self.surface = pygame.Surface(size)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            self.surface.blit(background.image, (0, 0))
        self.events = {'Выйти': terminate, 'Играть': lambda: self.switch_window(GameWindow(self.parent)),
                       'Настройки': lambda: self.switch_window(Settings(self.parent, (600, 600))),
                       'Достижения': lambda: self.switch_window(AchievementWindow(self.parent))}

    def update(self, event: pygame.event):
        pass

    def add_widget(self, widget, dist):
        pass

    def add_action(self, event, action):
        self.events[event] = action

    def add_widget(self, widget):
        self.surface.blit(widget.surface, widget.position)
        if widget.events:
            for event, action in widget.events.items():
                self.add_action(event, action)