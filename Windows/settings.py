from .window import Window


class Settings(Window):
    def __init__(self, parent, size):
        super().__init__(parent)
        self.size = size
