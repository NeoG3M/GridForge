from sqlite3 import connect

from CONSTANTS import *
from .Window import Window


class AchievementWindow(Window):
    def __init__(self, parent, size: tuple[int, int] = DISPLAY_SIZE):
        super().__init__(parent, size)
        with connect('DATABASE.sqlite') as connection:
            connection.commit()
