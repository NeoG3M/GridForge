import pygame.mixer

from Widgets.widgetGroup import WidgetGroup
from utils import *


class Window:

    def __init__(self, gf_game, background='black'):
        self.gridforge = gf_game
        self.background = background
        self.screen = self.gridforge.screen
        self.events = dict()
        self.widgets = WidgetGroup()
        self.sprites = pygame.sprite.Group()
        self.create_widgets()
        try:
            self.sound_track = pygame.mixer.Sound(f'audio_files/{self.__class__.__name__}.mp3')
        except FileNotFoundError:
            pass
        else:
            self.sound_track.play(-1)
            self.sound_track.set_volume(BASE_MUSIC_VOLUME)

    def stop_music(self):
        self.sound_track.stop()

    def stop(self, *args):
        # особое завершение у дочерних
        pass

    def update(self, event):
        self.screen.fill((0, 0, 0))
        self.show_background()
        self.widgets.handle_event(event)
        self.widgets.draw(self.screen)
        self.sprites.draw(self.screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.check_mousebuttondown_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.check_mousebuttonup_event(event)
        if event.type == pygame.KEYDOWN:
            self.check_keydown_event(event)
        if event.type == pygame.KEYUP:
            self.check_keyup_event(event)

    def check_mousebuttondown_event(self, event: pygame.event):
        pass

    def check_mousebuttonup_event(self, event: pygame.event):
        pass

    def check_keydown_event(self, event: pygame.event):
        if event.key == pygame.K_ESCAPE and event.mod == pygame.KMOD_ALT:
            pygame.event.post(get_event('SHUTDOWN'))

    def check_keyup_event(self, event):
        pass

    def add_background(self, background=None):
        """
        Добавление заднего фона
        :param background: задний фон
        :return: None
        """
        if not background:
            background = self.background
        if isinstance(background, str):
            background = pygame.Color(background)
        self.background = background

    def show_background(self):
        if isinstance(self.background, pygame.color.Color):
            self.screen.fill(self.background)
        elif isinstance(self.background, pygame.sprite.Sprite):
            self.screen.blit(self.background.image, (0, 0))
        elif isinstance(self.background, tuple):
            self.screen.fill(self.background)

    def __add_action(self, event: pygame.event, action: callable):
        self.events[event] = action

    def create_widgets(self):
        pass

    def add_widget(self, widget):
        #  TODO Добавление виджета
        if widget.events:
            for event, action in widget.events.items():
                self.__add_action(event, action)
        self.widgets.add_widget(widget)

    def add_widgets(self, *args):
        """
        This method realises adding of different count of widgets.
        It would be good if made any ways to give class widgetGroup()
        to this method.
        :param args:
        :return:
        """
        try:
            for widget in args:
                self.widgets.add_widget(widget)
        except TypeError:
            pass

    def set_volume(self, volume: float = BASE_MUSIC_VOLUME):
        self.sound_track.set_volume(volume)

    def pause_music(self):
        self.sound_track.stop()

    def play_music(self):
        self.sound_track.play(-1)
