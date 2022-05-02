import pygame


# base class for locations
class Location(object):
    def __init__(self, parent):
        self.parent = None
        self.window = pygame.display.get_surface()
        self.parent = parent
        self.background = pygame.image.load('src/assets/background.png')

    def event(self, event):
        pass

    def draw(self):
        pass
