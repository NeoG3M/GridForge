from CONSTANTS import *


class GridForge:
    __GAME_EVENTS = {'SWITCH_WINDOW': pygame.USEREVENT + 3}
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
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == self.__GAME_EVENTS['SWITCH_WINDOW']:
                    self.switch_window(event.name, event.arg)

    def switch_window(self, new_window, arg=()):
        if self.current_window:
            self.current_window.stop()
        self.current_window = self.__WINDOWS[new_window](*arg)


class Window:
    def __init__(self, gf_game: GridForge, background='black'):
        self.gridforge = gf_game
        self.screen = self.gridforge.screen
        self.events = {}

    def stop(self, *args):
        pass

    def __add_action(self, event, action):
        self.events[event] = action

    def add_widget(self, widget):
        #  TODO Добавление виджета
        if widget.events:
            for event, action in widget.events.items():
                self.__add_action(event, action)


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
