import pygame

from CONSTANTS import *
from Widgets.widgetGroup import WidgetGroup

class Window:
    def __init__(self, gf_game, background='black'):
        self.gridforge = gf_game
        self.screen = self.gridforge.screen
        self.events = {}
        self.widgets = WidgetGroup()
        self.create_widgets()

    def stop(self, *args):
        # особое завершение у дочерних
        pass

    def update(self, event):
        self.widgets.handle_event(event)
        self.widgets.draw(self.screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.check_mousebuttondown_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.check_mousebuttonup_event(event)
        if event.type == pygame.KEYDOWN:
            self.check_keydown_event(event)
        if event.type == pygame.KEYUP:
            self.check_keyup_event(event)

    def check_mousebuttondown_event(self, event):
        pass

    def check_mousebuttonup_event(self, event):
        pass

    def check_keydown_event(self, event):
        if event.key == pygame.K_ESCAPE and event.mod == pygame.KMOD_ALT:
            pygame.event.post(self.gridforge.get_event('SHUTDOWN'))

    def check_keyup_event(self, event):
        pass

    def add_background(self, background):
        '''
        Добавление заднего фона
        :param background:
        :return:
        '''
        if isinstance(background, str):
            background = pygame.Color(background)
        if isinstance(background, pygame.color.Color):
            self.screen.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            self.screen.blit(background.image, (0, 0))
        elif isinstance(background, tuple):
            self.screen.fill(background)

    def __add_action(self, event, action):
        self.events[event] = action

    def create_widgets(self):
        pass

    def add_widget(self, widget):
        #  TODO Добавление виджета
        if widget.events:
            for event, action in widget.events.items():
                self.__add_action(event, action)