from Widgets import *


class NumberWidget(Widget):
    def __init__(self, game_window, rect, color=pygame.Color('black')):
        super().__init__(rect, color)
        self.gw = game_window
        self.showed_description = False
        self.text_color = pygame.Color('gold')
        self.font = pygame.font.Font(None, 40)

    def handle_event(self, event: pygame.event):
        super().handle_event(event)


    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, pygame.Color('orange'),
                         (self.rect.x + 2, self.rect.y + 2, self.rect.w - 4, self.rect.h - 4), 2)

        x_offset = self.rect.w - 30 - self.font.size(str(self.gw.current_money))[0]
        text = self.font.render(str(self.gw.current_money), True, self.text_color)
        surface.blit(text, (self.rect.left + 15 + x_offset, self.rect.top + 15))

        if self.hovered:
            from GridForge import current_window
            text_widget = TextWindowWidget((*pygame.mouse.get_pos(), 100, 100), 'Это ваше финансирование')
            current_window.priority_widgets.append(text_widget)

