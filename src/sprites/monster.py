import random as RenderPlain


from sprites.sprite import Sprite


class Monster(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y)
        self.init_image('src/assets/monster.png')

    def move(self):
        self.move_x(rnd.randint(-5, 5))
        self.move_y(rnd.randint(-5, 5))
