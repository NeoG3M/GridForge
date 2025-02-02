import pygame.sprite

from GridForge import get_event
from .Window import Window
from Widgets.Field import Field
from Widgets.widgetBlock import WidgetBlock
from Widgets.Button import Button
from Units import Unit


class GameWindow(Window):
    def __init__(self, gf_game):
        super().__init__(gf_game)
        self.create_widgets()
        self.add_background('darkgray')
        self.sprites = pygame.sprite.Group()

    def create_widgets(self):
        self.widgets.add_widget(Field((400, 50, 700, 560), level='level/level_0/map.csv'))
        self.towers_block = WidgetBlock((20, 50, 290, 560))

        un = Unit('80KW', pygame.image.load('plates/E1.png'), 'пока бессмысленно здесь что-то писать')
        un.create_as_widget(self.towers_block, (70, 98))
        un = Unit('40KW', pygame.image.load('plates/E2.png'), 'пока бессмысленно здесь что-то писать')
        un.create_as_widget(self.towers_block, (70, 98))
        un = Unit('10KW', pygame.image.load('plates/E3.png'), 'пока бессмысленно здесь что-то писать')
        un.create_as_widget(self.towers_block, (70, 98))
        un = Unit('20KW', pygame.image.load('plates/E4.png'), 'пока бессмысленно здесь что-то писать')
        un.create_as_widget(self.towers_block, (70, 98))


        self.widgets.add_widget(self.towers_block)
        exit_event = lambda: pygame.event.post(pygame.event.Event(get_event('SWITCH_WINDOW'), name='start', arg=[self.gridforge]))
        self.widgets.add_widget(Button((20, 10, 100, 30), pygame.Color('orange'), 'Меню', on_click=exit_event))
