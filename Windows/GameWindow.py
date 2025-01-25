import pygame.sprite

import Widgets.widget
from .Window import Window
import csv
import plates
from Widgets.Field import Field
from Widgets.widgetBlock import WidgetBlock
from Widgets.Button import Button


class GameWindow(Window):
    def __init__(self, gf_game):
        super().__init__(gf_game)
        self.create_widgets()
        self.add_background('darkgray')
        self.sprites = pygame.sprite.Group()

    def create_widgets(self):
        self.widgets.add_widget(Field((400, 50, 700, 560), level='level/level_0/map.csv'))
        self.towers_block = WidgetBlock((20, 50, 290, 560))

        self.widgets.add_widget(self.towers_block)
        exit_event = lambda: pygame.event.post(pygame.event.Event(self.gridforge.get_event('SHUTDOWN')))
        self.widgets.add_widget(Button((20, 10, 100, 30), pygame.Color('orange'), 'Меню', on_click=lambda: exit_event))