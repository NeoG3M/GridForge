from CONSTANTS import *
from Windows import *


class GridForge:
    __WINDOWS = {'start': StartWindow, 'level': GameWindow}

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption('GridForge')
        self.current_window = None

    def run_game(self):
        game_running = True
        self.switch_window('start', self)
        while game_running:  # основной цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == self.__GAME_EVENTS['SHUTDOWN']:
                    terminate()
                self.current_window.update(event)
                if event.type == GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)
            self.clock.tick(FPS)
            pygame.display.flip()

    def switch_window(self, new_window, *args):
        if self.current_window:
            self.current_window.stop()
        self.current_window = self.__WINDOWS[new_window](*args)

    def get_event(self, event):
        return self.__GAME_EVENTS.get(event, None)


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
