import pygame

from locations.location import Location


class InputLocation(Location):
    def __init__(self, parent, settings):
        Location.__init__(self, parent, settings)

        pygame.mouse.set_visible(False)
        pygame.key.set_repeat(1)

        self.controls = pygame.sprite.Group()
        self.controls_captions = pygame.sprite.Group()

        self.name = None

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                # self.name = 
                if self.name is not None:
                    self.parent.location = GameLocation(
                        self.parent,
                        self.name,
                        self.settings
                    )
