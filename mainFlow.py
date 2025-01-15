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
        self.current_window = None

    def run_game(self):
        self.switch_window(StartWindow())
        while self.current_window:
            self.current_window.run()
            self.clock.tick(FPS)

    def switch_window(self, new_window):
        if self.current_window:
            self.current_window.stop()
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))



    def switch_window(self, new_window: Window):
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))
        self.window_events = new_window.events


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
