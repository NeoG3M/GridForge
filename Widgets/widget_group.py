import pygame


class WidgetGroup:
    def __init__(self):
        self.widgets = list()

    def add_widget(self, widget):
        self.widgets.append(widget)

    def handle_event(self, event: pygame.event):
        for widget in self.widgets:
            widget.handle_event(event)

    def draw(self, surface: pygame.Surface):
        for widget in self.widgets:
            widget.draw(surface)
