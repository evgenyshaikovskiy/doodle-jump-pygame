import pygame
from sprites.sprite import Sprite


class Spring(Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.compressed = 0
        pygame.sprite.Sprite.__init__(self)

        self.init_image('src/assets/spring.png')

    def compress(self):
        self.init_image('src/assets/spring_jumped.png')
        self.compressed = 1

    def get_top_surface(self):
        left = self.rect.left
        top = self.rect.top
        width = self.rect.width
        height = self.rect.height * 0.1
        return pygame.Rect(left, top, width, height)
