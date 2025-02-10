import pygame

from Widgets.widgetBlock import WidgetBlock
from Widgets.level_preview_widget import LevelPreview


class LevelPanel(WidgetBlock):
    def __init__(self, rect, background_color=pygame.Color('#3e1c03'),
                 border_color=pygame.Color('gold'), layout_mode=GRID, on_click=None):
        super().__init__(rect, background_color)

        self.scrollbar_is_visible = False

    def add_widget(self, widget):
        pass