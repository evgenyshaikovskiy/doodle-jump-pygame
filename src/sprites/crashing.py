from sprites.platform import Platform


class CrashingPlatform(Platform):
    def __init__(self, x, y, settings):
        Platform.__init__(self, x, y, settings)
        self.init_image('src/assets/red_platform.png')
        self.y_speed = 10
        self.crashed = False
        self.spring = None

    def crush(self):
        self.init_image('src/assets/broken_platform.png')
        self.crashed = True

    def move(self):
        if self.crashed == 1:
            self.move_y(self.y_speed)

    def renew(self):
        Platform.renew(self)
        self.init_image('src/assets/red_platform.png')
        self.crashed = True
