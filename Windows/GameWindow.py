from .Window import Window
import csv


class MapUtilit:
    def __init__(self):
        self.map = []

    def unpack_map(self, filename):
        with open(filename, 'r', encoding='utf-8') as level_file:
            reader = csv.reader(level_file, delimiter=';')
            for i, row in enumerate(reader):
                print(i, row)


class GameWindow(Window):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.add_background('darkgray')
        mu = MapUtilit()
        mu.unpack_map('level/level_0/map.csv')
