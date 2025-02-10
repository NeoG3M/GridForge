import pygame

from Widgets.Button import Button
from Widgets.level_preview_widget import LevelPreview
from Widgets.widgetBlock import WidgetBlock
from Widgets.widgetGroup import WidgetGroup
from Windows.Window import Window
from utils import all_sprites, DISPLAY_SIZE, terminate


class MenuWindow(Window):
    __background_sprite = pygame.sprite.Sprite(all_sprites)
    __background_sprite.image = pygame.image.load(f"data/menu_window_screen.png")
    __background_sprite.rect = __background_sprite.image.get_rect()
    __BUTTON_DICT: dict = {'Выйти': terminate}
    """
    This class realizes a menu window of the game, where you can can find different buttons for 
    moving to other windows
    """

    def __init__(self, parent):
        super().__init__(parent, background=self.__background_sprite)

        self.sprites = pygame.sprite.Group()
        self.widgets = WidgetGroup()
        self.create_widgets()
        self.add_background(self.__background_sprite)

    def check_mousebuttondown_event(self, event: pygame.event):
        super().check_mousebuttondown_event(event)
        # mouse_pos = event.pos
        # for button in self.buttons:
        #     if button.rect.collidepoint(mouse_pos):
        #         self.__BUTTON_DICT[button.text]()

    @staticmethod
    def exit_event():
        from GridForge import get_event
        pygame.event.post(pygame.event.Event(get_event('SHUTDOWN')))

    def create_widgets(self):
        exit_event = self.exit_event
        self.widgets.add_widget(
            Button((DISPLAY_SIZE[0] - 160, 20, 150, 50),
                   pygame.Color("gold"), 'Выйти', on_click=exit_event)
        )

        self.widgets.add_widget(
            Button((DISPLAY_SIZE[0] - 380, DISPLAY_SIZE[1] - 250, 350, 50),
                   pygame.Color("black"), "Достижения", pygame.Color("gold"), on_click=None)
        )

        self.widgets.add_widget(
            Button((DISPLAY_SIZE[0] - 380, DISPLAY_SIZE[1] - 190, 350, 50),
                   pygame.Color("black"), "Магазин", pygame.Color("gold"), on_click=None)
        )

        self.widgets.add_widget(
            Button((DISPLAY_SIZE[0] - 380, DISPLAY_SIZE[1] - 130, 350, 50),
                   pygame.Color("black"), "Поддержать авторов", pygame.Color("gold"), on_click=None)
        )

        block = WidgetBlock((20, 330, 250, 300), pygame.Color("black"),
                            pygame.Color("gold"), layout_mode='vertical')
        self.widgets.add_widget(block)

        block.add_widget(LevelPreview((0, 0, 220, 75), pygame.Color("black"), pygame.Color("gold")))
        block.add_widget(LevelPreview((0, 0, 220, 75), pygame.Color("black"), pygame.Color("gold")))
        block.add_widget(LevelPreview((0, 0, 220, 75), pygame.Color("black"), pygame.Color("gold")))
        block.add_widget(LevelPreview((0, 0, 220, 75), pygame.Color("black"), pygame.Color("gold")))

        # sprite = Icon((DISPLAY_SIZE[0] - 445, DISPLAY_SIZE[1] - 255), -1,
        #               "achievement_icon.png", (60, 60), self.sprites)
        # sprite = Icon((DISPLAY_SIZE[0] - 445, DISPLAY_SIZE[1] - 195), -1,
        #               "shop_icon.png", (60, 60), self.sprites)
        # sprite = Icon((DISPLAY_SIZE[0] - 445, DISPLAY_SIZE[1] - 140), -1,
        #               "support_authors_icon.png", (60, 60), self.sprites)

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
