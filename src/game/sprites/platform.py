import pygame
import random
import utility.loader

from sprites.sprite import Sprite
from sprites.spring import Spring


class Platform(Sprite):
    platform_width = get_settings('platform_width')

    def get_surface_area(self):
        left = self.rect.left
        top = self.rect.top
        width = self.rect.width
        height = self.rect.height * 0.1
        return pygame.Rect(left, top, width, height)

    def __init__(self, x, y):
        Sprite.__init__(self, x, y)
        if type(self).__name__ == 'Platform':
            self.init_image('src/assets/green_platform.png')
            rnd = random.randint(-100, 100)
            if rnd >= 0:
                self.spring = Spring(self.x + random.randint(
                    -int(self.platform_width / 2 - 10),
                    int(self.platform_width / 2) - 10),
                                    self.y - 20)
            else:
                self.spring = None
