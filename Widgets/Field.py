import csv
import json

from .widget import Widget
from CONSTANTS import *
import plates


class Camera:
    def __init__(self, field):
        """
        Инициализация камеры.

        :param widget_rect: pygame.Rect, определяющий границы виджета на экране.
        :param map_matrix: двумерный массив (матрица), представляющий плитки карты.
        :param sprite_group: группа спрайтов, которые нужно отрисовать.
        """
        self.field = field
        self.widget_rect = field.rect
        self.map_matrix = field.level_map
        self.sprite_group = field.sprites

        self.offset_x = 0  # Сдвиг камеры по X
        self.offset_y = 0  # Сдвиг камеры по Y
        self.zoom = 3  # Масштаб камеры

        self.dragging = False  # Флаг, указывает, перемещает ли игрок камеру
        self.last_mouse_pos = None  # Последняя позиция мыши для расчёта сдвига
        self.last_global_mouse_pos = (0, 0)

    def handle_event(self, event):
        """
        Обработка событий мыши.

        :param event: событие pygame.Event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.widget_rect.collidepoint(event.pos) and not self.field.is_dragging_unit:
                self.dragging = True
                self.last_mouse_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
                self.last_mouse_pos = None

        elif event.type == pygame.MOUSEMOTION:
            self.last_global_mouse_pos = event.pos
            if self.dragging:
                dx = event.pos[0] - self.last_mouse_pos[0]
                dy = event.pos[1] - self.last_mouse_pos[1]
                self.offset_x -= dx / self.zoom
                self.offset_y -= dy / self.zoom
                self.last_mouse_pos = event.pos
                self.clamp_camera()

        elif event.type == pygame.MOUSEWHEEL:
            # Масштабирование
            if self.widget_rect.collidepoint(self.last_global_mouse_pos):
                scale_factor = 0.25 if event.y > 0 else -0.25
                self.zoom += scale_factor
                self.zoom = max(1.5, min(self.zoom, 4))

    def clamp_camera(self):
        max_offset_x = len(self.map_matrix[0]) * 32 - self.widget_rect.width / self.zoom
        max_offset_y = len(self.map_matrix) * 32 - self.widget_rect.height / self.zoom
        self.offset_x = max(0, min(self.offset_x, max_offset_x))
        self.offset_y = max(0, min(self.offset_y, max_offset_y))

    def apply(self, rect):
        """
        Применить сдвиг и масштаб к прямоугольнику (например, для спрайта).

        :param rect: pygame.Rect.
        :return: преобразованный pygame.Rect.
        """
        x = round((rect.x - self.offset_x) * self.zoom, 1)
        y = round((rect.y - self.offset_y) * self.zoom, 1)
        w = round(rect.width * self.zoom, 1)
        h = round(rect.height * self.zoom, 1)
        return pygame.Rect(x, y, w, h)

    def get_hp_color(self, percent):
        if percent > 0.5:
            g = 255
            r = int(255 * (1 - percent) * 2)
        else:
            r = 255
            g = int(255 * percent * 2)
        return r, g, 0

    def render(self, surface):
        surface.fill('#edc9a5')
        for plate in self.field.plates:
            transformed_rect = self.apply(plate.sprite.rect)
            surface.blit(pygame.transform.scale_by(plate.sprite.image, self.zoom), transformed_rect)
            if isinstance(plate, plates.TowerPlate) and plate.tower:
                rtd_tower = pygame.transform.rotate(pygame.transform.scale_by(plate.tower.img, self.zoom), 0)

                surface.blit(rtd_tower, rtd_tower.get_rect(center=transformed_rect.center))

                # TODO: ПРОВЕРКА НА ОТОБРАЖЕНИЕ HP - НАСТРОЙКА В ОТДЕЛЬНОМ ФАЙЛЕ
                hp_bord = pygame.Rect(transformed_rect.left + 2 * self.zoom, transformed_rect.top,
                                      transformed_rect.w - 4 * self.zoom, 4 * self.zoom)
                pygame.draw.rect(surface, (0, 0, 0), hp_bord)
                percent_of_hp = plate.tower.hp / plate.tower.maxhp
                hp_bar = pygame.Rect(hp_bord.left + self.zoom, hp_bord.top + self.zoom,
                                     (hp_bord.w - 2 * self.zoom) * percent_of_hp, hp_bord.h - 2 * self.zoom)

                pygame.draw.rect(surface, self.get_hp_color(percent_of_hp), hp_bar)

        # for sprite in self.sprite_group:
        #     transformed_rect = self.apply(sprite.rect)
        #     surface.blit(pygame.transform.scale_by(sprite.image, self.zoom), transformed_rect)


class Field(Widget):
    __plates = {'W0': {'img_name': 'wall0'}, 'E0': {'img_name': 'E0', 'rotation': 'N'},
                'E': {'rotation': 'N'}, 'TB0': {'img_name': 'old_TB', 'rotation': 'N', 'level': 0, 'states': 1},
                'TB1': {'img_name': 'tb_gama', 'rotation': 'N', 'level': 1, 'states': 1},
                'R': {'img_name': 'reactor', 'states': 5, 'rotation': 'N'}}

    def __init__(self, rect, level: str):
        super().__init__(rect)
        self.level_directory = level

        self.x, self.y, self.width, self.height = rect
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.sprites = pygame.sprite.Group()

        self.plates = []
        self.level_map = []
        self.path_map = []
        self.danger_path_map = []
        self.reactor_coords = (0, 0)
        self.unpack_map(self.level_directory + 'map.csv')

        self.is_dragging_unit = False  # Флаг, указывающий, что игрок перетаскивает plate, башню или инструмент
        self.camera = Camera(self)

    def handle_event(self, event):
        self.camera.handle_event(event)
        super().handle_event(event)

    def check_cell(self, mousepos, unit):
        cell = self.get_cell(mousepos)
        if cell:
            return self.level_map[int(cell[1])][int(cell[0])].can_use_unit(unit)

    def apply_unit(self, mousepos, unit):
        cell = self.get_cell(mousepos)
        self.level_map[int(cell[1])][int(cell[0])].apply_unit(unit)

    def get_cell(self, mouse_pos):

        x_mouse, y_mouse = mouse_pos
        if self.rect.collidepoint(mouse_pos):
            field_top_x, field_top_y = self.rect.topleft
            x_cell = (x_mouse - field_top_x + self.camera.offset_x * self.camera.zoom) // (32 * self.camera.zoom)
            y_cell = (y_mouse - field_top_y + self.camera.offset_y * self.camera.zoom) // (32 * self.camera.zoom)
            return x_cell, y_cell
        return None

    def draw(self, surface):
        super().draw(surface)
        self.camera.render(self.surface)
        surface.blit(self.surface, self.rect)

    def unpack_map(self, filename):
        with open(filename, 'r', encoding='utf-8') as level_file:
            reader = csv.reader(level_file, delimiter=';')
            for i, row in enumerate(reader, 0):
                self.level_map.append([])
                self.danger_path_map.append([])
                self.path_map.append([])
                for j, plate in enumerate(row, 0):
                    plate = self.create_plate(plate, j, i)
                    if isinstance(plate, plates.ReactorPlate):
                        self.reactor_coords = (j, i)
                    self.level_map[i].append(plate)
                    self.plates.append(plate)
                    if isinstance(plate, plates.TrailPlate) or isinstance(plate, plates.ReactorPlate):
                        self.path_map[i].append(0)
                    else:
                        self.path_map[i].append(1)

    def create_plate(self, code: str, x, y):
        rotation = code[-1]
        if code.startswith('W'):
            return plates.SolidPlate(**self.__plates[code[:-1]], x=x, y=y, group=self.sprites)
        elif code.startswith('E'):
            return plates.PlateConstructor(x=x, y=y, img_name=code, **self.__plates['E'], group=self.sprites)
        elif code.startswith('TB'):
            return plates.TowerPlate(**self.__plates[code], x=x, y=y, group=self.sprites)
        elif code.startswith('R'):
            with open(self.level_directory + 'lvl.json', 'r', encoding='UTF8') as lvl_file:
                lvl = json.load(lvl_file)
                return plates.ReactorPlate(lvl['reactor']['hp'], **self.__plates[code], x=x, y=y, group=self.sprites)
