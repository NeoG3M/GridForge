import pygame

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 600, 600
FPS = 100


class Window:
    def __init__(self, size: tuple[float, float], background=pygame.color.Color('black')):
        self.surface = pygame.Surface(size)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            pass
            #  TODO заполнение спрайта по центру
        self.events = {}

    def add_widget(self, widget, dist):
        pass


class GridForge:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        black_window = Window(DISPLAY_SIZE)
        self.switch_window(black_window)

        self.base_events = {}
        self.window_events = {}

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for subevent, action in (self.window_events | self.base_events).items():
                    if event.type == subevent:
                        action()

            pygame.display.flip()
            self.clock.tick(FPS)

    def switch_window(self, new_window: Window):
        self.current_window = new_window
        self.screen.blit(new_window.surface, (0, 0))
        self.window_events = new_window.events
