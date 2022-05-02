import pygame


from sprites.sprite import Sprite
from sprites.text import TextSprite


class Button(Sprite):
    def __init__(self, x, y, text):
        self.x = x
        self.y = y

        pygame.sprite.Sprite.__init__(self)

        self.image_selected = pygame.image.load('src/assets/menu_selected.png')
        self.image_unselected = pygame.image.load('src/assets/menu_unselected.png')

        self.text_sprite = TextSprite(self.x, self.y, text)
        self.change_state(0)

    def change_state(self, state):
        if state == 0:
            self.image = self.image_unselected
            self.text_sprite.set_color((255, 165, 149))
        elif state == 1:
            self.image = self.image_selected
            self.text_sprite.set_color((243, 227, 200))

        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
