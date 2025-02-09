from Units import *

PLATE_SIZE = 32


class PlateConstructor:
    FACING = {'N': 0, 'W': 90, 'S': 180, 'E': 270}

    def __init__(self, img_name: str, rotation: str, x: int, y: int, group: pygame.sprite.Group):
        self.sp_group = group
        self.sprite = pygame.sprite.Sprite(group)
        self.image = pygame.image.load(f'plates/{img_name}.png').convert_alpha()

        self.sprite.image = pygame.transform.rotate(self.image, self.FACING[rotation])
        self.x, self.y = x, y
        self.sprite.rect = pygame.Rect(x * PLATE_SIZE, y * PLATE_SIZE, PLATE_SIZE, PLATE_SIZE)

    def get_info(self) -> str:
        pass

    def can_use_unit(self, unit):
        return False

    def is_solid(self) -> bool:
        return False

    def apply_unit(self, unit):
        pass


class DynamicPlate(PlateConstructor):
    def __init__(self, img_name: str, states: int, rotation: str, x, y, group):
        super().__init__(img_name, rotation, x, y, group)
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
    def is_solid(self):
        return True


class TowerPlate(DynamicPlate):
    def __init__(self, level: int, img_name: str, states: int, rotation: str, x: int, y: int, group):
        super().__init__(img_name, states, rotation, x, y, group)
        self.tower = None
        self.tower_hp = None
        if level == 0:
            self.max_consumption = 0
        elif level == 1:
            self.max_consumption = 25
        elif level == 2:
            self.max_consumption = 40
        elif level == 3:
            self.max_consumption = 80

    def heal_tower_hp(self, amount):
        self.tower.heal_hp(amount)
        self.tower_hp = self.get_hp()

    def decrease_tower_hp(self, amount):
        self.tower.decrease_hp(amount)
        self.tower_hp = self.get_hp()
        if self.tower_hp == 0:
            del self.tower
            self.tower = None
            self.tower_hp = None

    def get_hp(self):
        return self.tower.hp

    def can_use_unit(self, unit):
        if isinstance(unit, TowerUnit) and not self.tower and unit.tower.consumption <= self.max_consumption:
            return True
        return False

    def apply_unit(self, unit):
        if isinstance(unit, TowerUnit):
            self.tower = unit.tower.create_child()
            self.tower.set_position((self.x * 32, self.y * 32))
            self.tower_hp = self.tower.maxhp
            # self.switch_state(1)

            self.tower_sprite = pygame.sprite.Sprite(self.sp_group)
            self.tower_image = self.tower.img

            self.tower_sprite.image = self.tower_image
            self.tower_sprite.rect = pygame.Rect(self.sprite.rect.x, self.sprite.rect.y, PLATE_SIZE, PLATE_SIZE)


class TrailPlate(PlateConstructor):
    def is_solid(self) -> bool:
        return False


class ReactorPlate(DynamicPlate):
    class Reactor:
        def __init__(self, maxhp, center):
            self.maxhp = maxhp
            self.hp = maxhp

            self.center = center

        def heal_hp(self, amount):
            self.hp += amount
            self.hp = min(self.hp, self.maxhp)

        def decrease_hp(self, amount):
            self.hp -= amount
            self.hp = max(self.hp, 0)
            if self.hp == 0:
                raise_event('REACTOR_EXPLOSION')

    def __init__(self, reactor_hp, img_name: str, states: int, rotation: str, x: int, y: int,
                 group: pygame.sprite.Group):
        super().__init__(img_name, states, rotation, x, y, group)
        self.reactor = self.Reactor(reactor_hp, (32 * x + 16, 32 * y + 16))

    def can_use_unit(self, unit):
        if isinstance(unit, RepairUnit):
            return self.reactor.hp < self.reactor.maxhp
        return False

    def is_solid(self) -> bool:
        return True

    def get_info(self) -> str:
        return 'Это основной реактор - важнейший элемент нашей победы! Это спасение наших жизней от угрозы республики!'
