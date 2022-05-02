import pygame
import utility.inputbox as inputbox

from locations.location import Location
from sprites.button import Button


class StartLocation(Location):
    def __init__(self, parent):
        Location.__init__(self, parent)

        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(0)

        self.start_button = Button(240, 200, 'Start')
        self.exit_button = Button(240, 270, 'Exit')

        self.controls = pygame.sprite.Group()
        self.controls.add(self.start_button)
        self.controls.add(self.exit_button)

        self.surfaces = []

        self.controls_captions = pygame.sprite.Group()
        self.controls_captions.add(self.start_button.text_sprite)
        self.controls_captions.add(self.exit_button.text_sprite)

        self.window.blit(self.background, (0, 0))

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)

    def event(self, event):
        here = 'asd'
        if event.type == MOUSE_MOTION:
            for btn in self.controls:
                if btn.rect.collidepoint(pygame.mouse.get_pos()):
                    btn.change_state(1)
                else:
                    btn.change_state(0)
        elif event.type == MOUSE_BUTTON_UP:
            if self.start_button.rect.collidepoint(pygame.mouse.get_pos()):
                name = inputbox.ask(self.window, 'Your name')
                if name:
                    self.parent.location = Game
