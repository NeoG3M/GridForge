import pygame

from Widgets.widget import Widget


class Button(Widget):
    def __init__(self,rect, color, text, text_color=pygame.Color('black'), on_click=None):
        super().__init__(rect, color, on_click)

        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.text_color = text_color

    def draw(self, surface):
        super().draw(surface)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)


