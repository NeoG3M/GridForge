import pygame

from Button import Button
from CONSTANTS import ALL_SPRITES, DISPLAY_SIZE, terminate
from .Window import Window


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load(f"Windows/Windows_back/StartWindow.jpg")
    __background_sprite.rect = __background_sprite.image.get_rect()
    __BUTTON_DICT: dict = {'Выйти': terminate}
    """
    This class realizes a start window of the game, where you can 
    """

    def __init__(self):
        super().__init__(background=self.__background_sprite)
        self.buttons = self.create_buttons()
        for btn in self.buttons:
            btn.draw()

    def update(self, event: pygame.event):
        """
        This method connect buttons with their funcs
        :param event: event
        :return: pass
        """
        for button in self.buttons:
            if button.rect.x <= event.pos[0] <= button.rect.x + button.rect.width and \
                    button.rect.y <= event.pos[1] <= button.rect.y + button.rect.height:
                self.__BUTTON_DICT.get(button.text, lambda: None)()

    def create_buttons(self) -> pygame.sprite.Group:
        """
        This method create buttons for this window
        :return: Group of buttons
        """
        buttons = pygame.sprite.Group()
        Button(self.surface, "Выйти", (DISPLAY_SIZE[0] - 160, 20), (150, 50), pygame.Color("orange"),
               buttons)
        Button(self.surface, "Мастерская", (int(DISPLAY_SIZE[0] * 0.72), int(DISPLAY_SIZE[1] * 0.65)), (200, 90),
               (167, 96, 56), buttons)
        Button(self.surface, "Достижения", (int(DISPLAY_SIZE[0] * 0.72), int(DISPLAY_SIZE[1] * 0.80)), (200, 90),
               (167, 96, 56), buttons)
        Button(self.surface, "Настройки", (10, 10), (180, 70), pygame.Color("orange"), buttons)
        return buttons
