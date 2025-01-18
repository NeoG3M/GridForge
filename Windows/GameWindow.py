import pygame.event

from CONSTANTS import *
from .Window import Window


class GameWindow(Window):
    __INTRO_EVENT_TYPE = pygame.USEREVENT + 7
    __OUTRO_EVENT_TYPE = pygame.USEREVENT + 8

    def __init__(self, parent):
        super().__init__(parent)
        self.intro()
        self.events['Главное меню'] = self.outro
        self.back: tuple[int, int, int] = (255, 255, 255)

    def update(self, event: pygame.event):
        if event.type in (self.__INTRO_EVENT_TYPE, self.__OUTRO_EVENT_TYPE):
            way = -1 if event.type == self.__INTRO_EVENT_TYPE else 1
            self.back = tuple(map(lambda x: x + way, self.back))
            self.surface.fill(self.back)
            if 255 > self.back[0] > 0:
                pygame.event.post(pygame.event.Event(event.type))
            else:
                if event.type == self.__OUTRO_EVENT_TYPE:
                    from Windows import StartWindow
                    self.switch_window(StartWindow(self.parent))
        super().update(event)

    def outro(self):
        self.back = (0, 0, 0)
        pygame.event.post(pygame.event.Event(self.__OUTRO_EVENT_TYPE))

    def intro(self):
        pygame.event.post(pygame.event.Event(self.__INTRO_EVENT_TYPE))
        self.back = (255, 255, 255)
