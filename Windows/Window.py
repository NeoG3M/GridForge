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

    def __add_action(self, event, action):
        self.events[event] = action

    def add_widget(self, widget):
        #  TODO Добавление виджета
        if widget.events:
            for event, action in widget.events.items():
                self.__add_action(event, action)