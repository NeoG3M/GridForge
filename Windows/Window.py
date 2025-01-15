from CONSTANTS import *


class Window:
    def __init__(self, background=pygame.Color('black')):
        self.surface = pygame.Surface(DISPLAY_SIZE)
        if isinstance(background, pygame.color.Color):
            self.surface.fill(background)
        elif isinstance(background, pygame.sprite.Sprite):
            pass
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