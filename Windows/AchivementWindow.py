from CONSTANTS import *
from .Window import Window


class AchievementWindow(Window):
    def __init__(self, size: tuple[int, int] = DISPLAY_SIZE):
        super().__init__(size)
