import pygame.mixer


class SoundSettings:
    # Не могу понять, зачем нужен этот класс
    def __init__(self, game):
        from GridForge import GridForge
        self.game: GridForge = game

    @staticmethod
    def set_volume(volume: float):
        pygame.mixer.music.set_volume(volume)

    def run_soundtrack(self, track: str):
        self.game.current_window.soundtrack = pygame.mixer.Sound(f'audio_files/{track}.mp3')
        self.game.current_window.soundtrack.play()
