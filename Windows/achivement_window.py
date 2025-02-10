from utils import *
from .window import Window


class AchievementWindow(Window):
    def __init__(self, parent, size: tuple[int, int] = DISPLAY_SIZE):
        super().__init__(parent, size)
