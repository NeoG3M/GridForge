import pygame

from Widgets import TextWindowWidget
from utils import all_sprites, raise_event
from .window import Window


class VictoryWindow(Window):
    __background_sprite = pygame.sprite.Sprite(all_sprites)
    __background_sprite.image = pygame.image.load("data/start_window_screen.png")

    def __init__(self, game):
        super().__init__(game, background=self.__background_sprite)
        self.create_widgets()

    def create_widgets(self):
        text = TextWindowWidget((500, 300, 200, 200), 'YOU WIN!\n\n',
                                on_click=lambda: raise_event('SWITCH_WINDOW', name='menu'))

        self.widgets.add_widget(text)
        self.widgets.draw(self.screen)
