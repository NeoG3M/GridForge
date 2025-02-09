from Statistic import Statistic

from utils import *
from Windows import *
from Windows.MenuWindow import *


class GridForge:
    __WINDOWS = {'start': StartWindow, 'level': GameWindow, "menu": MenuWindow}

    def __init__(self):
        pygame.init()

        self.connection = Statistic()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.current_window = None

        pygame.display.set_caption('GridForge')

    def run_game(self):
        game_running = True
        self.switch_window('start', self)
        while game_running:  # основной цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == GAME_EVENTS['SHUTDOWN']:
                    self.connection.close()
                    terminate()
                self.current_window.update(event)
                if event.type == GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)
            self.clock.tick(FPS)
            pygame.display.flip()
            self.clock.tick(FPS)

    def switch_window(self, new_window, *args):
        if self.current_window:
            self.current_window.stop()
        self.current_window = self.__WINDOWS[new_window](*args)


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
