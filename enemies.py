import heapq
import math

import pygame.transform

from utils import *


class Enemy:
    FACING = {'N': 0, 'W': 90, 'S': 180, 'E': 270}

    def __init__(self, start_plate, max_hp, move_speed, reward, img_name, damage, attack_range, attack_speed,
                 bullet_class, bullet_outpoints, game_field,
                 is_self_healing=False, healing_amount=0,
                 is_flying=False):
        self.img = pygame.image.load('data/enemies/' + img_name + '.png')
        self.top_img = self.img.subsurface((32, 0, 32, 32))
        self.base_img = self.img.subsurface((0, 0, 32, 32))
        self.sprite = pygame.sprite.Sprite(all_sprites)
        spr_img = self.base_img.copy()
        spr_img.blit(self.top_img, (0, 0))
        self.sprite.image = spr_img
        self.next_plate = None
        self.base_facing = 'W'
        self.top_rotation = 90
        self.sprite.rect = pygame.Rect(0, 0, 32, 32)
        self.abs_position = start_plate
        self.cur_position = (start_plate[0] * 32, start_plate[1] * 32)
        self.center = (self.cur_position[0] + 16, self.cur_position[1] + 16)
        self.velocity = [0, 0]
        self.is_flying = is_flying
        self.max_hp = max_hp
        self.hp = max_hp
        self.is_healing = is_self_healing
        self.heal_amount = healing_amount

        self.speed = move_speed
        self.reward = reward

        self.bullet_class = bullet_class
        self.bullet_outpoints = bullet_outpoints
        self.rotated_bul_outpts = [pygame.math.Vector2(p) for p in bullet_outpoints]
        self.damage = damage
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.target = None

        self.rotate()
        self.game_field = game_field
        self.path = self.search_path(self.game_field.get_path_map(), self.game_field.get_danger_map())

        enemy_group.append(self)

    def get_scaled_image(self, scale):
        scaled = pygame.transform.rotozoom(pygame.transform.scale_by(self.base_img, scale),
                                           self.FACING[self.base_facing], 1)
        rtd_top = pygame.transform.rotozoom(pygame.transform.scale_by(self.top_img, scale), self.top_rotation, 1)
        scaled.blit(rtd_top,
                    rtd_top.get_rect(center=scaled.get_rect().center))
        return scaled

    def rotate(self):

        if self.velocity[0] > 0:
            self.base_facing = 'E'
        elif self.velocity[0] < 0:
            self.base_facing = 'W'
        elif self.velocity[1] > 0:
            self.base_facing = 'S'
        elif self.velocity[1] < 0:
            self.base_facing = 'N'
        if self.target:
            ty, tx = self.center
            ey, ex = self.target.center
            self.top_rotation = math.degrees(math.atan2(ey - ty, ex - tx)) - 180  # Угол к врагу (в радианах)
        else:
            self.top_rotation = self.FACING[self.base_facing]
        spr_img = pygame.transform.rotate(self.base_img, self.FACING[self.base_facing])
        rotated = pygame.transform.rotate(self.top_img, self.top_rotation)
        spr_img.blit(rotated, rotated.get_rect(center=self.sprite.rect.center))
        self.sprite.image = spr_img

        # self.sprite.image = pygame.transform.rotate(self.base_img, self.FACING[self.base_facing])
        # self.sprite.image.blit(pygame.transform.rotate(self.top_img, self.top_rotation), (0, 0))

        self.rotated_bul_outpts = [pygame.math.Vector2(p).rotate(self.top_rotation) for p in self.bullet_outpoints]

    def heal_hp(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def decrease_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

    def check_for_target(self):
        if math.dist(self.game_field.get_reactor().center, self.center) <= self.attack_range:
            self.target = self.game_field.get_reactor()
        else:
            enemies_in_range = [tower for tower in tower_group if
                                math.dist(tower.center, self.center) <= self.attack_range]
            self.target = min(enemies_in_range, key=lambda e: math.dist(e.center, self.center), default=None)
        if self.target:
            if self.target.hp <= 0:
                self.target = None
                self.check_for_target()
            en_x, en_y = self.target.center
            if math.sqrt((en_x - self.center[0]) ** 2 + (
                    en_y - self.center[1]) ** 2) > self.attack_range:
                self.target = None

    @staticmethod
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def search_path(self, path_map, danger_map):
        """
        Поиск пути по A* с учетом штрафов опасности.
        """
        rows, cols = len(path_map), len(path_map[0])
        open_set = []
        start = self.abs_position[1], self.abs_position[0]
        r_coords = self.game_field.get_reactor_coords()
        reactor = r_coords[1], r_coords[0]

        heapq.heappush(open_set, (0, start))

        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, reactor)}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == reactor:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path  # Возвращаем оптимальный путь

            x, y = current
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for nx, ny in neighbors:
                if rows > nx >= 0 == path_map[nx][ny] and 0 <= ny < cols:  # Проходимость
                    tentative_g_score = g_score[current] + 1 + danger_map[nx][ny]  # + штраф

                    if (nx, ny) not in g_score or tentative_g_score < g_score[(nx, ny)]:
                        came_from[(nx, ny)] = current
                        g_score[(nx, ny)] = tentative_g_score
                        f_score[(nx, ny)] = tentative_g_score + self.heuristic((nx, ny), reactor)
                        heapq.heappush(open_set, (f_score[(nx, ny)], (nx, ny)))
        return None

    def attack(self):
        pass

    def move(self):
        # print(self.velocity)
        self.cur_position = (self.cur_position[0] + self.velocity[0], self.cur_position[1] + self.velocity[1])
        self.center = (self.cur_position[0] + 16, self.cur_position[1] + 16)

    def update(self):
        if self.cur_position[0] % 32 == 0 and self.cur_position[1] % 32 == 0:

            if self.path:
                self.abs_position = (self.cur_position[0] // 32, self.cur_position[1] // 32)
                self.next_plate = self.path.pop(0)
                self.next_plate = (self.next_plate[1], self.next_plate[0])

            self.velocity[0] = self.speed * (self.next_plate[0] - self.abs_position[0])
            self.velocity[1] = self.speed * (self.next_plate[1] - self.abs_position[1])
            if self.next_plate == self.game_field.get_reactor_coords():
                self.velocity = [0, 0]
                self.target = self.game_field.get_reactor()
        if self.velocity[0] or self.velocity[1]:
            self.move()
        self.check_for_target()
        self.rotate()
        if self.target:
            self.attack()
