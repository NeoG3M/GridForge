from CONSTANTS import *
from Units import TowerUnit
from Units import Unit
from Widgets.Button import Button
from Widgets.Field import Field
from Widgets.widgetBlock import WidgetBlock
from .Window import Window


class GameWindow(Window):
    def __init__(self, gf_game):
        super().__init__(gf_game)
        self.is_dragging_unit = False
        self.picked_unit = None
        self.last_mouse_pos = (0, 0)
        self.create_widgets()
        self.add_background('darkgray')
        self.sprites = pygame.sprite.Group()

    def create_widgets(self):
        self.field = Field((400, 50, 700, 560), level='level_0')
        self.widgets.add_widget(self.field)
        self.towers_block = WidgetBlock((20, 50, 290, 560))

        un = Unit('80KW', pygame.image.load('plates/E1.png'),
                  'Это текстовое поле, которое баганно отображается из-за порядка отрисовки в игре (')
        un.create_as_widget(self.towers_block, (70, 98))
        un = Unit('40KW', pygame.image.load('plates/E2.png'))
        un.create_as_widget(self.towers_block, (70, 98))
        un = Unit('10KW', pygame.image.load('plates/E3.png'),
                  'Это всеголишь обычная земля в мире постапокалипсиса. Вы можете попробовать её сварить!')
        un.create_as_widget(self.towers_block, (70, 98))
        import towers.towers

        un = TowerUnit('20KW',
                       towers.towers.Tower(100, 20, 30, 80, 'test_tower', 60, 20, None, [(3, 12)]),
                       'Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана Мана ')
        un.create_as_widget(self.towers_block, (70, 98))

        self.widgets.add_widget(self.towers_block)
        exit_event = lambda: raise_event('SWITCH_WINDOW', name='start', arg=[self.gridforge])
        self.widgets.add_widget(Button((20, 10, 100, 30), pygame.Color('orange'), 'Меню', on_click=exit_event))

    def display_picked_unit(self):
        if self.is_dragging_unit:
            camera_zoom = self.field.camera.zoom

            mouse_pos = self.last_mouse_pos
            unit_icon = self.picked_unit.icon.image.copy().convert_alpha()
            if self.field.check_cell(mouse_pos, self.picked_unit):
                unit_icon.fill((200, 255, 200, 200), special_flags=pygame.BLEND_RGBA_MULT)
                if isinstance(self.picked_unit, TowerUnit):
                    attack_range = self.picked_unit.tower.attack_range

                    range_surf = pygame.Surface(
                        (attack_range * camera_zoom * 2, attack_range * camera_zoom * 2), pygame.SRCALPHA)

                    pygame.draw.circle(range_surf, (10, 255, 10, 100), (
                        attack_range * camera_zoom, attack_range * self.field.camera.zoom
                    ),
                                       attack_range * camera_zoom)
                    self.field.surface.blit(range_surf, (
                        mouse_pos[0] - self.field.rect.left - attack_range * camera_zoom,
                        mouse_pos[1] - self.field.rect.top - attack_range * camera_zoom))

                    self.screen.blit(self.field.surface, self.field.rect)
            else:
                unit_icon.fill((255, 200, 200, 200), special_flags=pygame.BLEND_RGBA_MULT)
            self.screen.blit(pygame.transform.scale_by(unit_icon, camera_zoom),
                             (mouse_pos[0] - 16 * camera_zoom, mouse_pos[1] - 16 * camera_zoom))

    def update(self, event):
        if event.type == get_event('PICK_UNIT'):
            self.is_dragging_unit = True
            self.field.is_dragging_unit = True
            self.picked_unit = event.unit
        if event.type == pygame.MOUSEMOTION:
            self.last_mouse_pos = event.pos
        super().update(event)
        if event.type == get_event('TICK_UPDATE'):
            if self.gridforge.ticks % 10 == 0:
                for enemy in enemy_group:
                    enemy.update()
                for tower in tower_group:
                    tower.update(self.gridforge.ticks)
        self.display_picked_unit()

    def check_mousebuttondown_event(self, event):
        if event.button == 3 and self.is_dragging_unit:
            self.is_dragging_unit = False
            self.field.is_dragging_unit = False
        if event.button == 1:
            print(self.field.get_cell(event.pos))
        if event.button == 1 and self.is_dragging_unit and self.field.check_cell(event.pos, self.picked_unit):
            self.field.apply_unit(event.pos, self.picked_unit)
            self.is_dragging_unit = False
            self.field.is_dragging_unit = False

    def check_keydown_event(self, event: pygame.event):
        super().check_keydown_event(event)
        if event.key == pygame.K_j:
            from enemies import Enemy

            Enemy((13, 7), 200, 4, 1000, 'en_test', 20, 160, 50, None, [(0, 0)], self.field)
