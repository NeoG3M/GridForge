import math

import pygame.image
from Windows.GameWindow import tower_group, all_sprites, enemy_group


class Tower:
    def __init__(self, maxhp, damage, attack_speed, attack_range, img_name, price, start_consuption, bullet_class,
                 bullet_outpoints: list[tuple[float, float]]):
        '''

        :param maxhp:
        :param damage:
        :param attack_speed: Промежуток между выстрелами - количество обновлений(FPS) между ними
        :param attack_range:
        :param img_name:
        :param price:
        :param start_consuption:
        '''
        self.img = pygame.image.load(img_name)
        self.sprite = pygame.sprite.Sprite(all_sprites)
        self.sprite.image = self.img
        self.sprite.rect = pygame.Rect(0, 0, 32, 32)
        self.position = (16, 16)
        self.rotation = 0

        self.maxhp = maxhp
        self.hp = maxhp

        self.bullet_class = bullet_class
        self.bullet_outpoints = bullet_outpoints
        self.rotated_bul_outpts = [pygame.math.Vector2(p) for p in bullet_outpoints]
        self.damage = damage
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.target = None

        self.price = price
        self.consumption = start_consuption

        tower_group.append(self)

    def get_rotated_sprite(self):
        return pygame.transform.rotate(self.sprite.image, self.rotation)

    def set_position(self, pos):
        self.sprite.rect.topleft = pos
        self.position = (pos[0] + 16, pos[1] + 16)

    def check_for_target(self):
        if not self.target:
            for enemy in enemy_group:
                en_x, en_y = enemy.position
                if math.sqrt((en_x - self.position[0]) ** 2 + (
                        en_y - self.position[1]) ** 2) <= self.attack_range:
                    self.target = enemy
                    break
        else:
            if self.target.hp <= 0:
                self.target = None
                self.check_for_target()

    def predict_angle(self, target):
        en_x, en_y = target.position
        dx = en_x - self.position[0]
        dy = en_y - self.position[1]
        angle = math.atan2(dy, dx) * 180 / math.pi - 90
        return angle

    def attack(self):
        pass

    def rotate(self, to_predict=False):
        if to_predict:
            self.rotation = self.predict_angle(self.target)
        self.sprite.image = self.get_rotated_sprite()
        self.rotated_bul_outpts = [pygame.math.Vector2(p).rotate(self.rotation) for p in self.bullet_outpoints]

    def update(self, tick):
        self.check_for_target()
        if self.target:
            self.rotate(True)
            if tick % self.attack_speed == 0:
                self.attack()
        else:
            self.rotation = 0
            self.rotate()
