import pygame

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 600, 600
FPS = 100
ALL_SPRITES = pygame.sprite.Group()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()