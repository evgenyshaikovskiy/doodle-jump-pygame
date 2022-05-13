import pygame
import json
import os

from locations.location import Location
from sprites.button import Button
from sprites.text import TextSprite


class ScoreboardLocation(Location):
    def __init__(self, parent, settings):
        Location.__init__(self, parent, settings)
        pygame.mouse.set_visible(True)

        self.controls = pygame.sprite.Group()
        self.controls_captions = pygame.sprite.Group()

        self.names = TextSprite(400, 100, text='Name:')
        self.scores = TextSprite(600, 100, text='Score:')

        self.clear_button = Button(
            settings['screen_width'] / 2,
            settings['screen_height'] - 100,
            'Clear Records'
        )

        self.controls.add(self.clear_button)
        self.controls_captions.add(self.clear_button.text_sprite)

        self.print_scoreboard()

        self.window.blit(self.background, (0, 0))

    def print_scoreboard(self):
        # get sorted scoreboard
        scores_dict = self.upload_leaderboard()
        sorted_scores = list(sorted(scores_dict.items(), key=lambda item: item[1], reverse=True))

        # take first top 10 users
        if len(sorted_scores) > 10:
            sorted_scores = sorted_scores[:10]

        x_align = 400
        y_align = 150
        for key_value in sorted_scores:
            record = TextSprite(
                x_align,
                y_align,
                text=f'{key_value[0]}'
            )

            y_align += 50
            self.controls_captions.add(record)

        y_align = 150
        x_align = 600
        for key_value in sorted_scores:
            record = TextSprite(x_align, y_align, text=f'{key_value[1]}')
            y_align += 50
            self.controls_captions.add(record)

        self.controls_captions.add(self.names)
        self.controls_captions.add(self.scores)

    def event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for btn in self.controls:
                if btn.rect.collidepoint(pygame.mouse.get_pos()):
                    btn.change_state(1)
                else:
                    btn.change_state(0)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.clear_button.rect.collidepoint(pygame.mouse.get_pos()):
                self.clear_scoreboard()
                self.print_scoreboard()
                self.parent.location = ScoreboardLocation(self, self.settings)

    def upload_leaderboard(self):
        if os.path.exists('src/utility/scores.json'):
            with open('src/utility/scores.json', 'r', encoding='UTF-8') as score_file:
                scores = json.load(score_file)

            return scores
        else:
            return {}

    def draw(self):
        self.controls.clear(self.window, self.background)
        self.controls.draw(self.window)
        self.controls_captions.draw(self.window)

    def clear_scoreboard(self):
        if os.path.exists('src/utility/scores.json'):
            os.remove('src/utility/scores.json')
