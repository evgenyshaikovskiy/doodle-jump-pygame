import random


from sprites.platform import Platform


class MovingPlatform(Platform):
    def __init__(self, x, y, settings):
        Platform.__init__(self, x, y, settings)
        self.init_image('src/assets/blue_platform.png')
        # possible states -1 and 1
        self.way = -1
        self.x_speed = int(random.randint(2, 6))
        self.spring = None

    def move(self):
        self.move_x(self.x_speed * self.way)
        if 10 < self.x < 100 or 700 < self.x < 800:
            self.way = -self.way
