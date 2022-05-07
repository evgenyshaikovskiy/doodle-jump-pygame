import pygame


from sprites.sprite import Sprite


class TextSprite(Sprite):
    def __init__(self, x, y, text='',
                 size=35, color=(0, 0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        # upload font later
        self.font = pygame.font.Font('src/assets/papernotes_font.ttf', size)
        self.color = color
        self.text = text
        self.generate_image()

    def set_text(self, text):
        self.text = text
        self.generate_image()

    def set_color(self, color):
        self.color = color
        self.generate_image()

    def set_size(self, size):
        self.font = pygame.font.Font('src/assets/papernotes_font.ttf', size)
        self.generate_image()

    def generate_image(self):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
