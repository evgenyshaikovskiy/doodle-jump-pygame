import pygame as pg


class SoundService:
    def __init__(self):
        self.jump_sound = pg.mixer.Sound('src/assets/jump.wav')
        self.spring_sound = pg.mixer.Sound('src/assets/springshoes.wav')
        self.start_sound = pg.mixer.Sound('src/assets/start.wav')

    def on_jump(self):
        self.__play_sound__(self.jump_sound)

    def on_spring(self):
        self.__play_sound__(self.spring_sound)

    def on_start(self):
        self.__play_sound__(self.start_sound)

    def __play_sound__(self, sound):
        pg.mixer.Sound.play(sound)
        pg.mixer.music.stop()
