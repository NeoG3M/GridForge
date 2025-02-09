from Windows import *
from Windows.MenuWindow import *


class GridForge:
    __WINDOWS = {'start': StartWindow, 'level': GameWindow, "menu": MenuWindow}

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption('GridForge')
        self.current_window = None
        self.ticks = 0

    def run_game(self):
        game_running = True
        self.switch_window('level', self)
        pygame.time.set_timer(get_event('TICK_UPDATE'), 40)
        while game_running:  # основной цикл игры
            for event in pygame.event.get():
                if event.type == get_event('TICK_UPDATE'):
                    self.ticks += 1
                if event.type == pygame.QUIT or event.type == GAME_EVENTS['SHUTDOWN']:
                    terminate()
                self.current_window.update(event)
                if event.type == GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)

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
