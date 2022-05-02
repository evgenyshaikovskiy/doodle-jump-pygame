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
    def __init__(self, parent, name):
        Location.__init__(self, parent)

        pygame.key.set_repeat(10)
        pygame.mouse.set_visible(0)

        self.doodle = Doodle(name)
        # self.doodle.name = name

        self.allsprites = pygame.sprite.Group()
        self.allsprites.add(self.doodle)
        for i in range(0, sgs.get_setting('platform_count')):
            self.allsprites.add(self.random_platform(False))
        for platform in self.allsprites:
            if isinstance(platform, Platform) and platform.spring is not None:
                self.allsprites.add(platform.spring)

        self.score_sprite = TextSprite(50, 25, self.doodle.name, 45, (0, 0, 0))
        self.allsprites.add(self.score_sprite)

        color = (0, 191, 255, 128)
        self.header = Rectangle(sgs.get_setting('screen_width'), 50, color)
        self.window.blit(self.background, (0, 0))

        # optional
        self.monster = None

    def random_platform(self, top=True):
        x = rand.randint(
            0,
            sgs.get_setting('screen_width') - sgs.get_setting('platform_width')
        )

        bad_y = []
        for sprite in self.allsprites:
            bad_y.append((sprite.y - 7, sprite.y + 7, sprite.rect.height))

        good = False
        while not good:
            if top:
                y = rand.randint(-100, 50)
            else:
                y = rand.randint(0, sgs.get_setting('screen_height'))
            good = True
            for bad_y_item in bad_y:
                if bad_y_item[0] <= y <= bad_y_item[1]:
                    good = False
                    break

        dig = rand.randint(0, 100)
        if dig < 35:
            return MovingPlatform(x, y)
        elif dig >= 35 and dig < 50:
            return CrashingPlatform(x, y)
        else:
            return Platform(x, y)

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
                            sgs.get_setting('screen_width')
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
            self.doodle.increase_y_speed(-sgs.get_setting('gravitation'))
            if sgs.get_setting('mouse_enabled') == 'True':
                self.doodle.set_x(mouse_pos[0])
            else:
                if sgs.get_setting('transparent_walls') == 'True':
                    if self.doodle.x < 0:
                        self.doodle.set_x(sgs.get_setting('screen_width'))
                    elif self.doodle.x > sgs.get_setting('screen_width'):
                        self.doodle.set_x(0)

            self.doodle.move_y(-self.doodle.y_speed)

            for sprite in self.allsprites:
                # spring under legs => doodle jumps up
                if isinstance(sprite, Spring) and self.doodle.get_legs_rect().colliderect(sprite.get_top_surface()) and self.doodle.y_speed <= 0:
                    sprite.compress()
                    self.doodle.y_speed = sgs.get_setting('spring_speed')

                # update platforms
                if isinstance(sprite, Platform):
                    if sprite.y >= sgs.get_setting('screen_height'):
                        self.allsprites.remove(sprite)
                        platform = self.random_platform()
                        self.allsprites.add(platform)
                        if isinstance(platform, Platform) and platform.spring:
                            self.allsprites.add(platform.spring)
                            
                if isinstance(sprite, Platform) and self.doodle.get_legs_rect().colliderect(sprite.get_surface_area()):
                    self.doodle.y_speed = sgs.get_setting('jump_speed')

                # move for crashed and moving platforms
                if isinstance(sprite, MovingPlatform) or (isinstance(sprite, CrashingPlatform) and not sprite.crashed):
                    sprite.move()

            if self.doodle.y < sgs.get_setting('middle_line'):
                self.doodle.increase_score(self.doodle.y_speed)
                for sprite in self.allsprites:
                    if not isinstance(sprite, TextSprite):
                        sprite.move_y(self.doodle.y_speed)

            self.allsprites.draw(self.window)
            self.score_sprite.set_text("               %s,    %s" % (self.doodle.name, int(self.doodle.score/10)))
            self.window.blit(self.header, (0, 0))
        else:
            self.parent.location = GameLocation(self.parent, self.doodle.name)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.doodle.set_x(self.doodle.x - 10)
            elif event.key == pygame.K_RIGHT:
                self.doodle.set_x(self.doodle.x + 10)
