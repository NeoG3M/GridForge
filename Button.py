import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, text,
                 dist: tuple[int, int],
                 size: tuple[int, int],
                 color,
                 *group):
        super().__init__(*group)
        self.rect = pygame.rect.Rect(*dist, *size)
        self.screen = screen
        self.text = text
        self.dist = dist
        self.color = color
        self.size = self.width, self.height = size
        self.draw()

    def draw(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill(pygame.Color("black"))

        font = pygame.font.Font(None, int(self.size[1] * 0.5))
        text = font.render(self.text, True, self.color)
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2

        surface.blit(text, (text_x, text_y))
        pygame.draw.rect(surface, self.color, (5, 5, self.width - 10, self.height - 10), 2)
        self.screen.blit(surface, self.dist)
