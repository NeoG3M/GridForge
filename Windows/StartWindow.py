from Windows.Window import Window
from utils import *


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(all_sprites)
    __background_sprite.image = pygame.image.load("data/start_window_screen.png")
    __background_sprite.image = pygame.Surface(DISPLAY_SIZE)
    __background_sprite.rect = __background_sprite.image.get_rect()
    """This class realises the start window of the game"""

    def __int__(self, parent):
        """This class waits for user action,
        then closes himself and open MenuWindow"""
        super().__init__(parent, background=self.__background_sprite)
        self.add_background(self.__background_sprite)
        self.screen.blit(self.__background_sprite.image, (0, 0))

    def update(self, event: pygame.event):
        """This method just closes StartWindow and opens MenuWindow"""
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            raise_event("SWITCH_WINDOW", name="menu", arg=self.gridforge)
        self.screen.blit(self.__background_sprite.image, (0, 0))
