import pygame
import utility.loader as sgs


# base class for locations
class Location(object):
    def __init__(self, parent, settings):
        self.parent = None
        self.window = pygame.display.get_surface()
        self.parent = parent
        self.background = pygame.transform.scale(
            pygame.image.load('src/assets/background.png'),
            (settings['screen_width'], settings['screen_height']),
        )

    def event(self, event):
        pass

    def draw(self):
        pass
