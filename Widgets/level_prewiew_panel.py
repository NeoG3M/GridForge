import pygame

from Widgets.widgetBlock import WidgetBlock


class LevelPanel(WidgetBlock):
    def __init__(self, rect, background_color=pygame.Color('#3e1c03')):
        # border_color=pygame.Color('gold'), layout_mode=None, on_click=None):
        super().__init__(rect, background_color)

        self.scrollbar_is_visible = False

    def add_widget(self, widget):
        pass
