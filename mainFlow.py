import pygame.event

from CONSTANTS import *
from Windows import *


class GridForge:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.current_window: Window | None = None
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption('GridForge')
        black_window = StartWindow(self)
        self.switch_window(black_window)

    def catch_events(self):
        for event in pygame.event.get():
            self.current_window.update(event)

    def draw(self):
        self.current_window.draw()

    def run_game(self):
        running = True
        while running:
            self.catch_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        terminate()

    def switch_window(self, new_window: Window):
        self.current_window = new_window
