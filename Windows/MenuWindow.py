import pygame

from Widgets.Button import Button
from CONSTANTS import ALL_SPRITES, DISPLAY_SIZE, terminate
from Windows.Window import Window


class MenuWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load(f"Windows/Windows_back/StartWindow.jpg")
    __background_sprite.rect = __background_sprite.image.get_rect()
    __BUTTON_DICT: dict = {'Выйти': terminate}
    """
    This class realizes a menu window of the game, where you can can find different buttons for 
    moving to other windows
    """

    def __init__(self, parent):
        super().__init__(parent, background=self.__background_sprite)
        self.create_widgets()
        self.add_background(self.__background_sprite)

    def check_mousebuttondown_event(self, event: pygame.event):
        super().check_mousebuttondown_event(event)
        # mouse_pos = event.pos
        # for button in self.buttons:
        #     if button.rect.collidepoint(mouse_pos):
        #         self.__BUTTON_DICT[button.text]()

    def create_widgets(self):
        """
        This method realises creating buttons and other widgets
        """
        exit_event = lambda: pygame.event.post(pygame.event.Event(self.gridforge.get_event('SHUTDOWN')))
        open_game_window_event = None
        open_achievement_window_event = None

        self.add_widgets(
            Button((DISPLAY_SIZE[0] - 160, 20, 150, 50), pygame.Color("orange"), 'Выйти', on_click=exit_event)
        )

