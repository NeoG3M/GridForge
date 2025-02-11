import pygame

from Widgets.widget_block import WidgetBlock
from Widgets.unit_widget import UnitWidget


class Unit:
    def __init__(self, name: str, icon: pygame.image, description: str = '', price=0):
        self.price = price
        self.name = name
        self.icon = pygame.sprite.Sprite()
        self.icon.image = icon
        self.description = description

    def create_as_widget(self, block: WidgetBlock, size: tuple):
        uw = UnitWidget((0, 0, *size), self)
        block.add_widget(uw)


class TowerUnit(Unit):
    def __init__(self, name: str, tower, description: str = ''):
        self.tower = tower
        super().__init__(name, tower.img, description, tower.price)


class HelpUnit(Unit):
    pass


class RepairUnit(HelpUnit):
    def __init__(self):
        icon = pygame.image.load('data/icons/repair.png')
        super().__init__('', icon,
                         'Самый обычный инструмент для починки старого хлама. Восстанавливает 30% здоровья. Инструмент на века. \nЦЕНА:50',
                         50)
        self.heal_am = 0.3


class RadiusUpgradeUnit(HelpUnit):
    def __init__(self):
        icon = pygame.image.load('data/icons/radius.png')
        super().__init__('', icon,
                         'Новая разработка, позваляющая увеличить дальность атаки ваших башен!\nЦЕНА:70',
                         70)
        self.range = 0.2


class DamageUpgradeUnit(HelpUnit):
    def __init__(self):
        icon = pygame.image.load('data/icons/damage.png')
        super().__init__('', icon,
                         'ВЛЕЙ ГНЕВ ЭЛЕКТРОНОВ В ТУРЕЛЬ и усиль её урон :3\nЦЕНА:60',
                         60)
        self.percent = 0.2


class AttackSpeedUpgradeUnit(HelpUnit):
    def __init__(self):
        icon = pygame.image.load('data/icons/speed.png')
        super().__init__('', icon,
                         '"Редбул" в мире турелей! Ускорь скорость атаки твоей башни\nЦЕНА:100',
                         100)
        self.percent = 0.3
