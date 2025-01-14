import sys

import pygame


def terminate():
    pygame.quit()
    sys.exit()


class GridForge:
    DISPLAY_SIZE = (600, 600)
    FPS = 100

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.DISPLAY_SIZE)
        self.current_window = None

    def run_game(self):
        self.switch_window(self.MenuWindow(self.DISPLAY_SIZE))
        while self.current_window:
            self.current_window.run()
            self.clock.tick(self.FPS)

    def switch_window(self, new_window):
        if self.current_window:
            self.current_window.stop()
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))

    class Window:
        def __init__(self, size, background='black'):
            self.surface = pygame.Surface(size)
            self.surface.fill(pygame.Color(background))
            self.events = {}
            self.running = True

        def run(self):
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    for subevent, action in self.events.items():
                        if event.type == subevent:
                            action()
                pygame.display.flip()

        def stop(self):
            self.running = False

        def add_action(self, event, action):
            self.events[event] = action

        def add_widget(self, widget):
            self.surface.blit(widget.surface, widget.position)
            if widget.events:
                for event, action in widget.events.items():
                    self.add_action(event, action)

    class LevelWindow(Window):
        def __init__(self, size, background='black'):
            super().__init__(size, background)
            # Add level-specific initialization here

    class MenuWindow(Window):
        def __init__(self, size, background='black'):
            super().__init__(size, background)
            # Add menu-specific initialization here


# Example usage
if __name__ == '__main__':
    game = GridForge()
    game.run_game()
