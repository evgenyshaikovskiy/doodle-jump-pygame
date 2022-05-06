import pygame
import utility.inputbox as inputbox
import sys

from locations.location import Location
from locations.game import GameLocation
from locations.scoreboard import ScoreboardLocation
from sprites.rectangle import Rectangle
from sprites.button import Button


class StartLocation(Location):
    def __init__(self, parent, settings):
        Location.__init__(self, parent, settings)

        self.settings = settings

        pygame.mouse.set_visible(1)
        pygame.key.set_repeat(0)

        self.start_button = Button(
            settings['screen_width'] / 2 ,
            settings['screen_height'] / 2 - 100,
            'Start'
        )

        self.exit_button = Button(
            settings['screen_width'] / 2,
            settings['screen_height'] / 2 - 50,
            'Exit'
        )

        self.scoreboard_button = Button(
            settings['screen_width'] / 2,
            settings['screen_height'] / 2,
            'Scoreboard'
        )

        self.controls = pygame.sprite.Group()
        self.controls.add(self.start_button)
        self.controls.add(self.exit_button)
        self.controls.add(self.scoreboard_button)

        self.surfaces = []

        self.controls_captions = pygame.sprite.Group()
        self.controls_captions.add(self.start_button.text_sprite)
        self.controls_captions.add(self.exit_button.text_sprite)
        self.controls_captions.add(self.scoreboard_button.text_sprite)

        self.window.blit(self.background, (0, 0))

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)

    def event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for btn in self.controls:
                if btn.rect.collidepoint(pygame.mouse.get_pos()):
                    btn.change_state(1)
                else:
                    btn.change_state(0)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.start_button.rect.collidepoint(pygame.mouse.get_pos()):
                name = inputbox.ask(self.window, 'Your name')
                if name:
                    self.parent.location = GameLocation(self.parent, name, self.settings)
            elif self.scoreboard_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.parent.location = ScoreboardLocation(self.parent, self.settings)
            elif self.exit_button.rect.collidepoint(pygame.mouse.get_pos()):
                sys.exit()

    def show_input(self):
        self.input_surf = Rectangle(500, 100, (0, 191, 255, 200))
        self.surfaces.append(self.input_surf)
