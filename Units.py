import pygame

from Widgets import unitWidget, WidgetBlock


class Unit:
    def __init__(self, name: str, icon: pygame.image, description: str = ''):
        self.name = name
        self.icon = pygame.sprite.Sprite()
        self.icon.image = icon
        self.description = description

    def create_as_widget(self, block: WidgetBlock, size: tuple):
        uw = unitWidget((0, 0, *size), self)
        block.add_widget(uw)


class TowerUnit(Unit):
    def __init__(self, name: str, tower, description: str = ''):
        self.tower = tower
        super().__init__(name, tower.img, description)
