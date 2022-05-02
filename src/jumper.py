import pygame
import sys
import utility.loader as sgs

from locations.game import GameLocation
from locations.start import StartLocation


class DoodleJump:
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(
            (
                sgs.get_setting('screen_width'),
                sgs.get_setting('screen_height')
            )
        )
        pygame.display.set_caption('Not doodle jump yet')

        self.location = None

    def event(self, event):
        # ??
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEY_UP:
            if event.type == K_ESCAPE:
                if isinstance(self.location, GameLocation):
                    self.location = StartLocation(self)
                elif isinstance(self.location, StartLocation):
                    pass
