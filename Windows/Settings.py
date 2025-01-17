from CONSTANTS import DISPLAY_SIZE
from .Window import Window


class Settings(Window):
    def __init__(self, parent, size):
        self.delta = int(DISPLAY_SIZE[0] * 0.2), int(DISPLAY_SIZE[1] * 0.1)
        super().__init__(parent, size=size, delta=self.delta)


