import pygame
import utility.inputbox as inputbox


from locations.location import Location
from locations.game import GameLocation


class InputLocation(Location):
    def __init__(self, parent, settings):
        Location.__init__(self, parent, settings)

        pygame.mouse.set_visible(False)

        self.controls = pygame.sprite.Group()
        self.controls_captions = pygame.sprite.Group()

        self.window.blit(self.background, (0, 0))

        self.name = inputbox.ask(self.window, 'Input name')

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)

    def event(self, event):
        if self.name is not None:
            self.parent.location = GameLocation(
                self.parent,
                self.name,
                self.settings
            )
