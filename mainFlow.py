from CONSTANTS import *


class GridForge:
    __GAME_EVENTS = {'SWITCH_WINDOW': pygame.USEREVENT + 3, 'SHUTDOWN': pygame.USEREVENT + 1}
    __WINDOWS = {'start': None}

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.current_window = None

    def run_game(self):
        self.game_running = True
        self.switch_window('start')
        while self.game_running: # основной цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == self.__GAME_EVENTS['SHUTDOWN']:
                    terminate()
                self.current_window.update(event)
                if event.type == self.__GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)


    def switch_window(self, new_window, arg=()):
        if self.current_window:
            self.current_window.stop()
        self.current_window = self.__WINDOWS[new_window](*arg)


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
