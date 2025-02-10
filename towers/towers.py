import gc
import math

from utils import *


class Tower:
    def __init__(self, maxhp, damage, attack_speed, attack_range, img_name, price, start_consuption, bullet_class,
                 bullet_outpoints: list[tuple[float, float]]):

        self.img_name = img_name
        self.img = pygame.image.load('towers/img/' + img_name + '.png')
        self.sprite = pygame.sprite.Sprite(all_sprites)
        self.sprite.image = self.img
        self.sprite.rect = pygame.Rect(0, 0, 32, 32)
        self.center = (16, 16)
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
        """
        :param maxhp:
        :param damage:
        :param attack_speed: Промежуток между выстрелами - количество обновлений(FPS) между ними
        :param attack_range:
        :param img_name:
        :param price:
        :param start_consuption:
        """
    def create_child(self):

        tw = Tower(self.maxhp, self.damage, self.attack_speed, self.attack_range, self.img_name, self.price,
                   self.consumption, self.bullet_class, self.bullet_outpoints)

        tower_group.append(tw)
        return tw

    def set_position(self, pos):
        self.sprite.rect.topleft = pos
        self.center = (pos[0] + 16, pos[1] + 16)

    def check_for_target(self):
        if not self.target:
            for enemy in enemy_group:
                en_x, en_y = enemy.center
                if math.sqrt((en_x - self.center[0]) ** 2 + (
                        en_y - self.center[1]) ** 2) <= self.attack_range:
                    self.target = enemy
                    break
        else:
            if self.target.hp <= 0:
                self.target = None
            en_x, en_y = self.target.center
            if math.sqrt((en_x - self.center[0]) ** 2 + (
                    en_y - self.center[1]) ** 2) > self.attack_range:
                self.target = None
            del en_x, en_y
            gc.collect()

    def predict_angle(self, target):
        ty, tx = self.center
        ey, ex = target.center
        return math.degrees(math.atan2(ey - ty, ex - tx)) - 180

    def attack(self):
        pass

    def heal_hp(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def decrease_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

    def update(self):
        self.check_for_target()
        if self.target:
            self.rotation = self.predict_angle(self.target)
        else:
            self.rotation = 0
