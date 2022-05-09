import pygame
import sys

from locations.game import GameLocation
from locations.start import StartLocation
from locations.input import InputLocation
from locations.scoreboard import ScoreboardLocation


class DoodleJump:
    def __init__(self, settings):
        pygame.init()
        self.settings = settings
        window = pygame.display.set_mode((
                settings['screen_width'],
                settings['screen_height']
            )
        )
        pygame.display.set_caption('Not doodle jump yet')

        self.location = None

    def event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if isinstance(self.location, StartLocation):
                    return
                if isinstance(self.location, GameLocation) or isinstance(self.location, InputLocation) or isinstance(self.location, ScoreboardLocation):
                    self.location = StartLocation(self, self.settings)
                    return
