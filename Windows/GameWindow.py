from Units import *
from Widgets import *
from utils import *
from .Window import Window


class GameWindow(Window):
    def __init__(self, gf_game):
        super().__init__(gf_game)
        self.is_dragging_unit = False
        self.picked_unit = None
        self.last_mouse_pos = (0, 0)
        self.current_money = 100
        self.create_widgets()
        self.add_background('black')
        self.sprites = pygame.sprite.Group()

    def create_widgets(self):
        self.field = Field((400, 80, 700, 560), level='level_0')
        self.widgets.add_widget(self.field)
        self.towers_block = WidgetBlock((20, 80, 290, 560))

        # un = Unit('80KW', pygame.image.load('plates/E1.png'),
        #           'Это текстовое поле, которое баганно отображается из-за порядка отрисовки в игре (')
        # un.create_as_widget(self.towers_block, (70, 98))

        import towers.towers
        with open('data/player.json', encoding='utf8') as js:
            dat = json.loads(js.read())
        for tower in dat['avialable_towers']:
            tower_data = dat['towers'][tower]
            un = TowerUnit(tower_data['name'],
                           towers.towers.Tower(img_name=tower_data['img'], **tower_data['creation_data']),
                           tower_data[
                               'description'] + f'\n ПОТРЕБЛЕНИЕ:{tower_data["creation_data"]["start_consuption"]}\n'
                                                f'СТОИМОСТЬ:{tower_data["creation_data"]["price"]}')
            un.create_as_widget(self.towers_block, (70, 98))

        self.units_block = WidgetBlock((400, 10, 600, 50))
        un = RepairUnit()
        un.create_as_widget(self.units_block, (30, 30))

        un = RadiusUpgradeUnit()
        un.create_as_widget(self.units_block, (30, 30))

        un = DamageUpgradeUnit()
        un.create_as_widget(self.units_block, (30, 30))

        un = AttackSpeedUpgradeUnit()
        un.create_as_widget(self.units_block, (30, 30))

        self.widgets.add_widget(self.units_block)
        self.widgets.add_widget(self.towers_block)

        self.widgets.add_widget(NumberWidget(self, (140, 10, 170, 50)))

        exit_event = lambda: raise_event('SWITCH_WINDOW', name='menu', arg=self.gridforge)
        self.widgets.add_widget(
            Button((20, 10, 100, 50), pygame.Color('black'), 'Меню', pygame.Color('orange'), on_click=exit_event))

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
            if self.gridforge.ticks % 3 == 0:
                self.field.reactor.increase_state()
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
