import pygame

from Widgets.Button import Button
from Widgets.widget import Widget
from CONSTANTS import ALL_SPRITES, DISPLAY_SIZE, terminate
from Windows.Window import Window


class StartWindow(Window):
    __background_sprite = pygame.sprite.Sprite(ALL_SPRITES)
    __background_sprite.image = pygame.image.load(f"Windows/Windows_back/StartWindow.jpg")
    __background_sprite.rect = __background_sprite.image.get_rect()
    __BUTTON_DICT: dict = {'Выйти': terminate}
    """
    This class realizes a start window of the game, where you can 
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
        exit_event = lambda: pygame.event.post(pygame.event.Event(self.gridforge.get_event('SHUTDOWN')))
        self.widgets.add_widget(
            Button((DISPLAY_SIZE[0] - 160, 20, 150, 50), pygame.Color("orange"), 'Выйти', on_click=exit_event))
        # block = Widgets.widgetBlock.WidgetBlock((20, 20, 150, 400), pygame.Color("gray"), layout_mode='grid')
        # block.add_widget(Widget((0, 0, 50, 50), pygame.Color('red')))
        # block.add_widget(Widget((60, 0, 50, 50), pygame.Color('blue')))
        # block.add_widget(Widget((0, 0, 50, 50), pygame.Color('red')))
        # block.add_widget(Widget((60, 0, 50, 50), pygame.Color('blue')))
        # block.add_widget(Widget((0, 0, 50, 50), pygame.Color('red')))
        # block.add_widget(Widget((60, 0, 50, 50), pygame.Color('blue')))
        # block.add_widget(Widget((0, 0, 50, 50), pygame.Color('red')))
        # block.add_widget(Widget((60, 0, 50, 50), pygame.Color('blue')))
        # block.add_widget(Widget((0, 0, 50, 50), pygame.Color('red')))
        # block.add_widget(Widget((60, 0, 50, 50), pygame.Color('blue')))
        # self.widgets.add_widget(block)


