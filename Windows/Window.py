from CONSTANTS import *


class Window:
    def __init__(self, parent, size: tuple[float, float] = DISPLAY_SIZE,
                 background=pygame.color.Color('black')):

        from Windows import (GameWindow, Settings, AchievementWindow)

        self.parent = parent
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

    def switch_window(self, new_window):
        self.parent.switch_window(new_window)
