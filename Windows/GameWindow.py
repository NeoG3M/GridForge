import pygame.event

from CONSTANTS import *

from .Window import Window


class GameWindow(Window):
    __INTRO_EVENT = pygame.USEREVENT + 7

    def __init__(self, parent):
        super().__init__(parent)
        pygame.event.post(pygame.event.Event(self.__INTRO_EVENT))
        self.back = (0, 0, 0)

    def update(self, event: pygame.event):
        if event.type == self.__INTRO_EVENT:
            self.back = tuple(map(lambda x: x + 1, self.back))
            self.surface.fill(self.back)
            if self.back[0] < 255:
                pygame.event.post(pygame.event.Event(self.__INTRO_EVENT))
        super().update(event)