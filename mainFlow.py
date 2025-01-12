from Windows import *
from default_constaints import *


class GridForge:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        black_window = StartWindow()
        self.switch_window(black_window)

        self.base_events = {}
        self.window_events = {}

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for subevent, action in (self.window_events | self.base_events).items():
                    if event.type == subevent:
                        action()
            self.screen.blit(self.current_window.surface, (0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)

    def switch_window(self, new_window: Window):
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))
        self.window_events = new_window.events
