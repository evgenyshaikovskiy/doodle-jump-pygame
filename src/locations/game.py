import pygame
import utility.loader as sgs
import random as rand

from sprites.platform import Platform
from locations.location import Location

from sprites.doodle import Doodle
from sprites.spring import Spring
from sprites.text import TextSprite
from sprites.rectangle import Rectangle
from sprites.moving import MovingPlatform
from sprites.crashing import CrashingPlatform
from sprites.monster import Monster


class GameLocation(Location):
    def __init__(self, parent, name, settings):
        Location.__init__(self, parent, settings)

        pygame.key.set_repeat(10)
        pygame.mouse.set_visible(0)

        self.doodle = Doodle(name, settings)

        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.doodle)
        for i in range(0, settings['platform_count']):
            self.allsprites.add(self.random_platform(False))
        for platform in self.allsprites:
            if isinstance(platform, Platform) and platform.spring is not None:
                self.allsprites.add(platform.spring)

        self.score_sprite = TextSprite(100, 40, self.doodle.name, 45)
        self.allsprites.add(self.score_sprite)

        self.window.blit(self.background, (0, 0))

        # optional
        self.monster = None

    def random_platform(self, top=True):
        x = rand.randint(
            0,
            self.settings['screen_width'] - self.settings['platform_width']
        )

        bad_y = []
        for sprite in self.allsprites:
            bad_y.append((sprite.y - 7, sprite.y + 7, sprite.rect.height))

        good = False
        while not good:
            if top:
                y = rand.randint(-100, 50)
            else:
                y = rand.randint(0, self.settings['screen_height'])
            good = True
            for bad_y_item in bad_y:
                if bad_y_item[0] <= y <= bad_y_item[1]:
                    good = False
                    break

        dig = rand.randint(0, 100)
        if dig < 35:
            return MovingPlatform(x, y, self.settings)
        elif dig >= 35 and dig < 50:
            return CrashingPlatform(x, y, self.settings)
        else:
            return Platform(x, y, self.settings)

    def draw(self):
        if self.doodle.alive:
            if self.monster is None:
                case = rand.randint(-1000, 5)
                if case > 0:
                    self.monster = Monster
                    (
                        rand.randint
                        (
                            0,
                            self.settings['screen_width']
                        ),
                        rand.randint(-50, 50)
                    )
                    # self.allsprites.add(self.monster)
                    # self.monster.move()
            # else:
                # self.monster.move()

                # if self.doodle.rect.colliderect(self.monster.rect):
                #     self.doodle.alive == 0
                # if self.monster.y >= sgs.get_setting('screen_height'):
                #     self.allsprites.remove(self.monster)
                #     self.monster = None

            self.allsprites.clear(self.window, self.background)

            mouse_pos = pygame.mouse.get_pos()
            self.doodle.increase_y_speed(-self.settings['gravitation'])
            if self.settings['mouse_enabled'] == 'True':
                self.doodle.set_x(mouse_pos[0])
            else:
                if self.settings['transparent_walls'] == 'True':
                    if self.doodle.x < 0:
                        self.doodle.set_x(self.settings['screen_width'])
                    elif self.doodle.x > self.settings['screen_width']:
                        self.doodle.set_x(0)

            self.doodle.move_y(-self.doodle.y_speed)

            for sprite in self.allsprites:
                # spring under legs => doodle jumps up
                if isinstance(sprite, Spring) and self.doodle.get_legs_rect().colliderect(sprite.get_top_surface()) and self.doodle.y_speed <= 0:
                    sprite.compress()
                    self.doodle.y_speed = self.settings['spring_speed']

                if isinstance(sprite, Platform) and self.doodle.get_legs_rect().colliderect(sprite.get_surface_area()) and self.doodle.y_speed <= 0:
                    if isinstance(sprite, CrashingPlatform) and not sprite.crashed:
                        sprite.crush()

                    self.doodle.y_speed = self.settings['jump_speed']

                # update platforms
                if isinstance(sprite, Platform):
                    if sprite.y >= self.settings['screen_height']:
                        self.allsprites.remove(sprite)
                        platform = self.random_platform()
                        self.allsprites.add(platform)
                        if isinstance(platform, Platform) and platform.spring:
                            self.allsprites.add(platform.spring)

                # move for crashed and moving platforms
                if isinstance(sprite, MovingPlatform) or (isinstance(sprite, CrashingPlatform) and not sprite.crashed):
                    sprite.move()

            if self.doodle.y < self.settings['middle_line']:
                self.doodle.increase_score(self.doodle.y_speed)
                for sprite in self.allsprites:
                    if not isinstance(sprite, TextSprite):
                        sprite.move_y(self.doodle.y_speed)

            self.allsprites.draw(self.window)
            self.score_sprite.set_text(f'SCORE: {int(self.doodle.score / 10)}.')
        else:
            self.parent.location = GameLocation(self.parent, self.doodle.name, self.settings)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.doodle.set_x(self.doodle.x - 10)
            elif event.key == pygame.K_RIGHT:
                self.doodle.set_x(self.doodle.x + 10)
