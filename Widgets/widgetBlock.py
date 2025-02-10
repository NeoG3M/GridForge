import pygame

from math import ceil
from Widgets import Widget, WidgetGroup
from typing import Callable


class ScrollBar(Widget):
    GRID, VERTICAL, HORIZONTAL = 'grid', 'vertical', 'horizontal'

    def __init__(self, rect: tuple, min_position, max_position, layout_mod=VERTICAL,
                 color: pygame.Color = pygame.Color('black'), second_color=pygame.Color("gold"),
                 on_click: Callable = None):
        super().__init__(rect, color, on_click)
        self.second_color = second_color
        self.min_position = min_position
        self.max_position = max_position
        self.layout_mode = layout_mod

    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        middle = self.rect.y + self.rect.height // 2
        pygame.draw.line(surface, self.second_color, (self.rect.x + 2, middle - 4),
                         (self.rect.x + self.rect.width - 2, middle - 4))
        pygame.draw.line(surface, self.second_color, (self.rect.x + 2, middle),
                         (self.rect.x + self.rect.width - 2, middle))
        pygame.draw.line(surface, self.second_color, (self.rect.x + 2, middle + 4),
                         (self.rect.x + self.rect.width - 2, middle + 4))

    def handle_event(self, event: pygame.MOUSEMOTION):
        rel = event.rel[1] if self.layout_mode in (self.GRID, self.VERTICAL) else event.rel[0]
        rel %= self.rect.height // 2
        if self.layout_mode in (self.GRID, self.VERTICAL):
            self.handle_rel_vertical(rel)
        else:
            self.handle_rel_horizontal(rel)

    def handle_rel_vertical(self, rel):
        if (self.rect.y + rel <= self.min_position) or (self.rect.y + self.rect.height + rel >= self.max_position):
            print(self.min_position, self.max_position, self.rect.y, self.rect.height)
            return 0
        self.rect.y += rel
        print(self.rect.y)

    def handle_rel_horizontal(self, rel):
        if (self.rect.x + rel <= self.min_position) or (self.rect.x + self.rect.width + rel >= self.max_position):
            return 0
        self.rect.x += rel


class WidgetBlock(Widget):
    GRID, VERTICAL, HORIZONTAL = 'grid', 'vertical', 'horizontal'

    def __init__(self, rect, background_color=pygame.Color('black'),
                 border_color=pygame.Color('gold'), layout_mode=GRID, on_click=None):
        super().__init__(rect, background_color, on_click)
        self.border_color = border_color
        self.widgets = WidgetGroup()
        self.scroll_offset = 0
        self.scrollbar_rect = pygame.Rect(rect[0] + rect[2] - 3, rect[1], 3, rect[3])
        self.scrollbar_color = pygame.Color('darkgray')
        self.scrollbar_dragging = False
        self.layout_mode = layout_mode
        self.hor_gap = 20
        self.ver_gap = 20

    def add_widget(self, widget):
        self.widgets.add_widget(widget)
        self.distribute_widgets()

    def distribute_widgets(self):
        if self.layout_mode == self.GRID:
            self.distribute_grid()
        elif self.layout_mode == self.VERTICAL:
            self.distribute_vertical()
        elif self.layout_mode == self.HORIZONTAL:
            self.distribute_horizontal()

    def distribute_grid(self):
        num_widgets = len(self.widgets.widgets)
        if num_widgets == 0:
            return
        cols = int(self.rect.width // (self.widgets.widgets[0].rect.width + self.hor_gap))
        for i, widget in enumerate(self.widgets.widgets):
            row, col = divmod(i, cols)
            rect = (self.rect.x + 10 + col * widget.rect.width + col * self.hor_gap,
                    self.rect.y + 10 + row * widget.rect.height +
                    row * self.ver_gap - self.scroll_offset)
            widget.rect.topleft = rect

    def distribute_vertical(self):
        y_offset = self.rect.y - self.scroll_offset

        for i in range(len(self.widgets.widgets)):
            widget = self.widgets.widgets[i]
            queue_offset = y_offset + 13 + i * 4
            widget.rect.topleft = (self.rect.x + 14, queue_offset)
            y_offset += widget.rect.height

    def distribute_horizontal(self):
        x_offset = self.rect.x - self.scroll_offset
        for widget in self.widgets.widgets:
            widget.rect.topleft = (x_offset, self.rect.y)
            x_offset += widget.rect.width

    def handle_event(self, event):
        super().handle_event(event)
        self.widgets.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.scrollbar_rect.collidepoint(event.pos):
                self.scrollbar_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.scrollbar_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.scrollbar_dragging:
                self.scroll_offset += event.rel[1] if self.layout_mode in [self.GRID, self.VERTICAL] else event.rel[0]
                self.scroll_offset = max(0, min(self.scroll_offset, self.get_max_scroll()))
                self.distribute_widgets()

    def get_max_scroll(self):
        return 0
        # if self.layout_mode in [self.GRID, self.VERTICAL]:
        #     total_height = sum(widget.rect.height for widget in self.widgets.widgets)
        #     return max(0, total_height - self.rect.height)
        # else:
        #     total_width = sum(widget.rect.width for widget in self.widgets.widgets)
        #     return max(0, total_width - self.rect.width)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(
            surface, self.border_color,
            (self.rect.x + 4, self.rect.y + 4,
             self.rect.width - 8, self.rect.height - 8), 2)

        self.widgets.draw(surface)
        if self.get_max_scroll() > 0:
            pygame.draw.rect(surface, self.scrollbar_color, self.scrollbar_rect)
