import pygame

from CONSTANTS import *
from Windows import (GameWindow, Settings, AchievementWindow)
from mainFlow import GridForge


class Window:
    def __init__(self, gf_game: GridForge, background='black'):
        self.gridforge = gf_game
        self.screen = self.gridforge.screen
        self.events = {}

    def stop(self, *args):
        # особое завершение у дочерних
        pass

    def update(self, event):
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
            pygame.event.post(self.gridforge.__GAME_EVENTS['SHUTDOWN'])

    def check_keyup_event(self, event):
        pass

    def __add_action(self, event, action):
        self.events[event] = action

    def add_widget(self, widget):
        #  TODO Добавление виджета
        if widget.events:
            for event, action in widget.events.items():
                self.__add_action(event, action)