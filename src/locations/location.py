import pygame
import utility.loader as sgs


# base class for locations
class Location(object):
    def __init__(self, parent, settings):
        self.parent = None
        self.window = pygame.display.get_surface()
        self.parent = parent
        self.settings = settings

        self.screen_height = settings['screen_height']
        self.screen_width = settings['screen_width']
        self.platform_count = settings['platform_count']
        self.platform_width = settings['platform_width']
        self.gravitation = settings['gravitation']
        self.mouse_enabled = settings['mouse_enabled']
        self.transparent_walls = settings['transparent_walls']
        self.spring_speed = settings['spring_speed']
        self.jump_speed = settings['jump_speed']
        self.middle_line = settings['middle_line']

        self.background = pygame.transform.scale(
            pygame.image.load('src/assets/background.png'),
            (self.screen_width, self.screen_height),
        )

    def event(self, event):
        pass

    def draw(self):
        pass
