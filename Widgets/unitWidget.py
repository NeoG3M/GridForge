import pygame

from Widgets.widget import Widget


class unitWidget(Widget):
    def __init__(self, rect, unit, color=pygame.Color('orange')):
        from GridForge import get_event
        on_click = lambda: pygame.event.post(pygame.event.Event(get_event('PICK_UNIT'), unit=unit))
        super().__init__(rect, color, on_click)
        self.unit = unit

    def draw(self, surface):
        if self.hovered:
            self_rect = self.rect.copy()
            #  Увеличение при наведении мыши
            self_rect.x -= 2
            self_rect.y -= 2
            self_rect.w += 4
            self_rect.h += 4
        else:
            self_rect = self.rect.copy()
        pygame.draw.rect(surface, self.color, self_rect)
        un_image = self.unit.icon
        surface.blit(pygame.transform.scale(un_image.image, (self_rect.w - 10, self_rect.w - 10)),
                     (self_rect.x + 5, self_rect.y + 5))

        font = pygame.font.Font(None, int(self.rect.w * 0.65))
        text = font.render(self.unit.name, True, pygame.Color('black'))
        surface.blit(pygame.transform.scale(text, (self_rect.w - 10, self_rect.h - self_rect.w)), (self_rect.bottomleft[0] + 5, self_rect.bottomleft[1] - (self_rect.h - self_rect.w)))

