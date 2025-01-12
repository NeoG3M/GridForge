import pygame

PLATE_SIZE = 32


class PlateConstructor:
    FACING = {'N': 0, 'E': 90, 'S': 180, 'W': 270}

    def __init__(self, img_name: str, rotation: str, group):
        self.sprite = pygame.sprite.Sprite(group)
        self.image = pygame.image.load(f'plates/{img_name}.png').convert_alpha()

        self.sprite.image = pygame.transform.rotate(self.image, self.FACING[rotation])
        self.sprite.rect = self.image.get_rect()

    def get_info(self):
        return None


class DynamicPlate(PlateConstructor):
    def __init__(self, img_name: str, states: int, rotation: str, group):
        super().__init__(img_name, rotation, group)
        self.states_imgs = []
        for state in range(states):
            img = self.image.subsurface((PLATE_SIZE * state, 0, PLATE_SIZE * (state + 1), PLATE_SIZE))
            img = pygame.transform.rotate(img, self.FACING[rotation])
            self.states_imgs.append(img)
        self.cur_state = 0
        self.states = states

    def switch_state(self, state: int):
        self.cur_state = state
        self.update_state()

    def increase_state(self):
        self.cur_state = (self.cur_state + 1) % self.states
        self.update_state()

    def switch_to_max_state(self):
        self.cur_state = self.states - 1
        self.update_state()

    def update_state(self):
        self.sprite.image = self.states_imgs[self.cur_state]

class SolidPlate(PlateConstructor):
    pass