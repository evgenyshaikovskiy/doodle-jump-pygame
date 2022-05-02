from sprites.platform import Platform


class CrashingPlatform(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.init_image('src/assets/red_platform.png')
        self.ySpeed = 10
        self.crashed = 0
        self.spring = None

    def crashed(self):
        self.init_image('src/assets/broken_platform.png')
        self.crashed = 1

    def move(self):
        if self.crashed == 1:
            self.move_y(self.ySpeed)

    def renew(self):
        Platform.renew(self)
        self.init_image('src/assets/red_platform.png')
        self.crashed = 0
