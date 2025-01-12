from default_constaints import *


class Window:
    def __init__(self, size: tuple[float, float] = DISPLAY_SIZE, background=pygame.color.Color('black')):
        self.surface = pygame.Surface(size)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            self.surface.blit(background.image, (0, 0))
        self.events = {}

    def add_widget(self, widget, dist):
        pass
