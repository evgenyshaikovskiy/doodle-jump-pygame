import random


from sprites.platform import Platform


class MovingPlatform(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.init_image('src/assets/blue_platform.png')
        # possible states -1 and 1
        self.way = -1
        self.xSpeed = random.randint(2, 6)
        self.spring = None

    def move(self):
        self.move_x(self.xSpeed * self.way)
        if 10 < self.x < 19 or 460 < self.x < 469:
            self.way = -self.way
