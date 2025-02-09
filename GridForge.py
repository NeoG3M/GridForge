from Statistic import Statistic

from utils import *
from Windows import *
from Windows.MenuWindow import *

current_window = None

class GridForge:
    __WINDOWS = {'start': StartWindow, 'level': GameWindow, "menu": MenuWindow}

    def __init__(self):
        pygame.init()

        self.connection = Statistic()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        global current_window
        self.current_window = current_window
        self.ticks = 0

        pygame.display.set_caption('GridForge')

    def run_game(self):
        game_running = True
        self.switch_window('level', self)
        pygame.time.set_timer(get_event('TICK_UPDATE'), 50)
        while game_running:  # основной цикл игры
            for event in pygame.event.get():
                if event.type == get_event('TICK_UPDATE'):
                    self.ticks += 1
                if event.type == pygame.QUIT or event.type == GAME_EVENTS['SHUTDOWN']:
                    self.connection.close()
                    terminate()
                self.current_window.update(event)
                if event.type == GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)
            pygame.display.flip()
            self.clock.tick(FPS)

    def switch_window(self, new_window, *args):
        global current_window
        if current_window:
            current_window.stop()
        current_window = self.__WINDOWS[new_window](*args)
        self.current_window = current_window


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
