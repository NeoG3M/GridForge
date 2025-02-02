import pygame

from Widgets.unitWidget import unitWidget
from Widgets.widgetBlock import WidgetBlock


class Unit:
    def __init__(self, name, icon, description=''):
        self.name = name
        self.icon = pygame.sprite.Sprite()
        self.icon.image = icon
        self.description = description

    def create_as_widget(self, block: WidgetBlock, size: tuple):
        uw = unitWidget((0, 0, *size), self)
        block.add_widget(uw)


class TowerUnit(Unit):
    def __init__(self, name, icon, tower, description=''):
        super().__init__(name, icon, description)
        self.tower = tower
