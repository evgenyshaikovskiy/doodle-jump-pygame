import pygame
import utility.loader
from sprites.sprite import Sprite


class Doodle(Sprite):
    # initialize fields
    alive = 1
    y_speed = 5
    score = 0
    image_r = pygame.image.load('src/assets/doodle_right.png')
    image_l = pygame.image.load('src/assets/doodle_left.png')

    def __init__(self, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.name = kwargs['name']
        self.x = kwargs['x_position']
        self.y = kwargs['y_position']
        self.image = self.image_r
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def _move(self):
        self.rect.center = (self.x, self.y)
        if self.y >= get_settings('screen_height'):
            self.alive = 0

    def get_legs_rect(self):
        left = self.rect.left + self.rect.width * 0.1
        top = self.rect.top + self.rect.height * 0.9
        width = self.rect.width * 0.6
        height = self.rect.height * 0.1

    def set_x(self, x):
        if x < self.x:
            self.image = self.image_l
        elif x > self.x:
            self.image = self.image_r

        self.x = x
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self._move()

    def increase_y_speed(self, speed):
        self.y_speed = self.y_speed + speed

    def increase_score(self, score):
        self.score = self.score + score
