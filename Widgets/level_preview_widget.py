from Widgets import TextWindowWidget
from Widgets.widget import Widget
from utils import *


class LevelPreview(Widget):
    def __init__(self, rect, level_num, background_color=pygame.Color("black"), border_color=pygame.Color("orange"),
                 information="Nothing here", count_of_enemies=0, count_of_towers=0, rewards=None, on_click=None):
        if not on_click:
            on_click = lambda: raise_event('SWITCH_WINDOW', name='level', level=level_num)
        super().__init__(rect, background_color, on_click)

        self.border_color = border_color
        self.information = information
        self.data = (count_of_enemies, count_of_towers, rewards)

        self.font_size = int(self.rect.size[1] * 0.3)
        font = pygame.font.Font(None, self.font_size)
        self.text = font.render(self.information, True, self.border_color)

    def draw(self, surface: pygame.Surface):
        """Отображение краткой информации об уровне"""

        pygame.draw.rect(surface, self.border_color, self.rect, 2)

        text_surface = pygame.Surface((self.rect.width, self.rect.height))
        text_surface.fill(self.color)
        # text_surface.blit(self.text, (0, 0))
        surface.blit(text_surface, (self.rect.x, self.rect.y))

        enemy_font = pygame.font.Font(None, self.font_size)
        enemy_text = enemy_font.render(f"Врагов: {self.data[0]}", True, self.border_color)
        surface.blit(enemy_text, (self.rect.x + 2, self.rect.y))

        tower_font = pygame.font.Font(None, self.font_size)
        tower_text = tower_font.render(f"Башен возможно: {self.data[1]}", True, self.border_color)
        surface.blit(tower_text, (self.rect.x + 2, self.rect.y + enemy_text.get_height() + 2))

        tower_font = pygame.font.Font(None, self.font_size)
        tower_text = tower_font.render(f"Награды: {self.data[1]}", True, self.border_color)
        surface.blit(tower_text, (self.rect.x + 2,
                                  self.rect.y + tower_text.get_height() * 2 + 2))

    def handle_event(self, event: pygame.event):
        super().handle_event(event)
        if self.hovered and self.information:
            from GridForge import current_window
            text_widget = TextWindowWidget((*pygame.mouse.get_pos(), 150, 100), self.information)
            current_window.priority_widgets.append(text_widget)
