import pygame

from utils import *

import math


class BaseBullet:
    def __init__(self, start_point, base_velocity: int, rotation, damage, target, img):
        self.damage = damage
        self.target = target
        self.image = pygame.transform.rotozoom(img, rotation, 1)
        self.rect = pygame.Rect(self.image.get_rect(center=start_point))

        bx, by = self.rect.center
        ex, ey = target.center
        self.rotation = math.degrees(math.atan2(ey - by, ex - bx)) - 90
        # self.rotation = rotation
        self.velocity = [base_velocity * math.sin(-self.rotation), base_velocity * math.cos(-self.rotation)]
        print(self.velocity)

        bullet_group.append(self)

    def set_damage(self, damage):
        self.damage = damage

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.colliderect(pygame.Rect(*self.target.cur_position, 32, 32)):
            self.target.decrease_hp(self.damage)
            bullet_group.remove(self)
            del self


class TurretBullet(BaseBullet):
    def __init__(self, start_point, rotation, damage, target):
        super().__init__(start_point, 3, rotation, damage, target, pygame.image.load('data/turret_bullet.png'))


bullet_types = [TurretBullet]
