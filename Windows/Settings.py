from CONSTANTS import *
from static_window_sprites import Button
from .Window import Window


class Settings(Window):
    def __init__(self, parent, size):
        self.delta = int(DISPLAY_SIZE[0] * 0.2), int(DISPLAY_SIZE[1] * 0.1)
        self.local_buttons_size = 250, 70

        super().__init__(parent, size=size, delta=self.delta)
        self.local_events = {'Основные': self.main_settings, 'Звук': self.sound_settings,
                             'Дисплей': self.display_settings}

    def create_buttons(self):
        buttons = super().create_buttons()
        Button(self.surface, 'Основные', (self.surface.get_rect().width * 0.23, self.surface.get_rect().height * 0.2),
               self.local_buttons_size, (208, 122, 240), buttons)
        Button(self.surface, 'Звук', (self.surface.get_rect().width * 0.23, self.surface.get_rect().height * 0.4),
               self.local_buttons_size, (208, 122, 240), buttons)
        Button(self.surface, 'Дисплей', (self.surface.get_rect().width * 0.23, self.surface.get_rect().height * 0.6),
               self.local_buttons_size, (208, 122, 240), buttons)
        return buttons

    def main_settings(self):
        pass

    def display_settings(self):
        pass

    def sound_settings(self):
        pass

    def update(self, event: pygame.event):
        super().update(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                x, y, width, height = button.rect.x, button.rect.y, button.rect.width, button.rect.height
                x += self.delta[0]
                y += self.delta[1]
                if x <= event.pos[0] <= x + width and y <= event.pos[1] <= y + height:
                    self.local_events.get(button.text, lambda: None)()
    # TODO: should optimize update func superclass
