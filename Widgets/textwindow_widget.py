import pygame.font

from .widget import Widget


class TextWindowWidget(Widget):
    def __init__(self, rect, text, color=pygame.Color('orange'), text_color=pygame.Color('black'), on_click=None):
        super().__init__(rect, color, on_click)
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, 26)
        self.lines = []
        self.wrap_text()

    def wrap_text(self):
        words = self.text.split(' ')
        lines = []
        line = ''
        for word in words:
            if self.font.size(line + word)[0] > self.rect.width - 10:
                lines.append(line)
                line = ''
            if self.font.size(word)[0] > self.rect.width - 10:
                self.rect.w = self.font.size(word)[0] + 10
            line += word + ' '
        lines.append(line.rstrip())
        self.lines = lines

    def draw(self, surface):
        self.rect.h = (self.font.size('Д')[1] + 5) * len(self.lines) + 10
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, pygame.Color('black'),
                         (self.rect.x + 2, self.rect.y + 2, self.rect.w - 4, self.rect.h - 4), 2)
        y_offset = 5
        for line in self.lines:
            text = self.font.render(line, True, self.text_color)
            surface.blit(text, (self.rect.x + 5, self.rect.y + y_offset))
            y_offset += self.font.size(line)[1] + 5
