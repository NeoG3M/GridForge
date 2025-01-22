import pygame.sprite

from .Window import Window
import csv
import plates
from Widgets.Field import Field, Camera


class GameWindow(Window):
    def __init__(self, gf_game):
        super().__init__(gf_game)
        self.create_widgets()
        self.add_background('darkgray')
        self.sprites = pygame.sprite.Group()


    def create_widgets(self):
        self.widgets.add_widget(Field((400, 50, 640, 480), level='level/level_0/map.csv'))
