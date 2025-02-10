<<<<<<<<< Temporary merge branch 1
import pygame

from utils import *
from Statistic import Statistic
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
        global current_window
        self.current_window = current_window
        self.ticks = 0
        pygame.display.set_caption('GridForge')
        self.current_window = None

    def run_game(self):
        game_running = True
        self.switch_window('start', self)
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
                    self.connection.add_victory()
            self.clock.tick(FPS)
            pygame.display.flip()

    def switch_window(self, new_window, *args):
        global current_window
        if current_window:
            current_window.stop()
            current_window.stop_music()
        current_window = self.__WINDOWS[new_window](*args)
        self.current_window = current_window


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
