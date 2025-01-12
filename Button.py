import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, text,
                 dist: tuple[int, int],
                 size: tuple[int, int],
                 color: tuple[int, int, int] | pygame.Color,
                 *group):
        super().__init__(*group)

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

# buttons = pygame.sprite.Group()
# new_button = Button(screen, "Выйти", (10, 10), (100, 30), pygame.Color("orange"), buttons)
# new_button = Button(screen, "Мастерская", (10, 40), (600, 130), (167, 96, 56), buttons)
# new_button = Button(screen, "Достижения", (10, 250), (600, 130), (167, 96, 56), buttons)
# new_button = Button(screen, "Настройки", (10, 460), (200, 70), pygame.Color("orange"), buttons)
# new_button = Button(screen, "Выйти", (10, 540), (300, 100), pygame.Color("orange"), buttons)
