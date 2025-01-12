import pygame

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 600, 600
FPS = 100


class Window:
    def __init__(self, size, background=pygame.color.Color('black')):
        self.surface = pygame.Surface(size)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            pass
            #  TODO заполнение спрайта по центру

    def add_widget(self, widget, dist):
        pass


class GridForge:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        black_window = Window(DISPLAY_SIZE)
        self.switch_window(black_window)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            self.clock.tick(FPS)

    def switch_window(self, new_window):
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))
