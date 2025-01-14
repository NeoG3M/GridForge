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

        self.base_events = {}
        self.window_events = {pygame.MOUSEBUTTONDOWN: lambda event: self.current_window.update(event)}

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                for subevent, action in (self.window_events | self.base_events).items():
                    if event.type == subevent:
                        action(event)
            self.screen.blit(self.current_window.surface, (0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()
        pygame.mixer.quit()

    def switch_window(self, new_window: Window):
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))
        self.window_events = new_window.events
