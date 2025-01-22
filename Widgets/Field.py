import csv

from .widget import Widget
import pygame
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
        self.zoom = 1.6  # Масштаб камеры

        self.dragging = False  # Флаг, указывает, перемещает ли игрок камеру
        self.last_mouse_pos = None  # Последняя позиция мыши для расчёта сдвига

    def handle_event(self, event):
        """
        Обработка событий мыши.

        :param event: событие pygame.Event.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.widget_rect.collidepoint(event.pos):  # Левая кнопка мыши
                self.dragging = True
                print("draggin'")
                self.last_mouse_pos = event.pos

            elif event.button == 4:  # Прокрутка вверх (увеличение масштаба)
                self.zoom = round(min(self.zoom + 0.1, 2.5), 2)

            elif event.button == 5:  # Прокрутка вниз (уменьшение масштаба)
                self.zoom = round(max(self.zoom - 0.1, 1), 2)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                self.dragging = False
                self.last_mouse_pos = None

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                dx = event.pos[0] - self.last_mouse_pos[0]
                dy = event.pos[1] - self.last_mouse_pos[1]
                self.offset_x -= dx / self.zoom
                self.offset_y -= dy / self.zoom
                self.last_mouse_pos = event.pos
                self.clamp_camera()

        elif event.type == pygame.MOUSEWHEEL:
            # Масштабирование
            scale_factor = 1.1 if event.y > 0 else 0.9
            self.zoom *= scale_factor
            self.zoom = max(0.5, min(self.zoom, 3.0))  # Ограничиваем масштаб от 0.5 до 3.0

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
        x = (rect.x - self.offset_x) * self.zoom + self.widget_rect.x
        y = (rect.y - self.offset_y) * self.zoom + self.widget_rect.y
        w = rect.width * self.zoom
        h = rect.height * self.zoom
        return pygame.Rect(x, y, w, h)

    def render(self, surface):
        """
        Отрисовать видимый участок карты и спрайты в пределах виджета.

        :param surface: поверхность pygame.Surface для отрисовки.
        """
        # Отрисовка плиток
        tile_width = 32  # Ширина плитки (px)
        tile_height = 32  # Высота плитки (px)

        # for row_idx, row in enumerate(self.map_matrix):
        #     for col_idx, tile in enumerate(row):
        #         tile_x = col_idx * tile_width - self.offset_x
        #         tile_y = row_idx * tile_height - self.offset_y
        #
        #         # Применяем масштаб и сдвиг
        #         tile_rect = pygame.Rect(tile_x, tile_y, tile_width, tile_height)
        #         transformed_rect = self.apply(tile_rect)
        #
        #         # Отрисовываем плитку, если она в пределах виджета
        #         if self.widget_rect.colliderect(transformed_rect):
        #             pygame.draw.rect(surface, tile, transformed_rect)

        # Отрисовка спрайтов
        surface.fill('#edc9a5')
        for sprite in self.sprite_group:
            # print('rendering')
            transformed_rect = self.apply(sprite.rect)
            # if self.widget_rect.colliderect(transformed_rect):
            surface.blit(pygame.transform.scale_by(sprite.image, self.zoom), transformed_rect)


class Field(Widget):
    __plates = {'W0': {'img_name': 'wall0'}, 'E0': {'img_name': 'E0', 'rotation': 'N'},'E1': {'img_name': 'E1', 'rotation': 'N'}}

    def __init__(self, rect, level: str):
        super().__init__(rect)
        self.x, self.y, self.width, self.height = rect
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
        self.sprites = pygame.sprite.Group()
        self.level_map = self.unpack_map(level)
        self.camera = Camera(self)


    def handle_event(self, event):
        self.camera.handle_event(event)
        super().handle_event(event)

    def draw(self, surface):
        super().draw(surface)
        self.camera.render(self.surface)
        surface.blit(self.surface, self.rect)


    def unpack_map(self, filename):
        level = []
        with open(filename, 'r', encoding='utf-8') as level_file:
            reader = csv.reader(level_file, delimiter=';')
            for i, row in enumerate(reader, 0):
                level.append([])
                for j, plate in enumerate(row, 0):
                    level[i].append(self.create_plate(plate, j, i))
        return level

    def create_plate(self, code: str, x, y):
        rotation = code[-1]
        if code.startswith('W'):
            return plates.SolidPlate(**self.__plates[code[:-1]], x=x, y=y, group=self.sprites)
        elif code.startswith('E'):
            return plates.PlateConstructor(x=x, y=y, **self.__plates[code], group=self.sprites)
