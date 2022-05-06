import pygame
from locations.location import Location


class ExitLocation(Location):
    def __init__(self, parent, name, score):
        Location.__init__(self, parent, settings)
        self.background = pygame.image.load('src/assets/background.png')
        print('Exiting...')
