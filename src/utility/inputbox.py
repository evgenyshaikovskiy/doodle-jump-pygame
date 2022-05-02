import pygame
import string
from pygame.locals import *


def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message):
    fontobject = pygame.font.Font(None, 18)

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (
            (screen.get_width() / 2) - 100,
            (screen.get_height() / 2) - 10,
            200,
            20),
        0
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (
            (screen.get_width() / 2) - 102,
            (screen.get_height() / 2) - 12,
            204,
            42
        ),
        1
    )

    if len(message) != 0:
        screen.blit(
            fontobject.render(message, True, (255, 255, 255)),
            (
                (screen.get_width() / 2) - 100,
                (screen.get_height() / 2) - 10
            ))

    pygame.display.flip()


def ask(screen, question):
    pygame.font.init()
    current_string = []

    display_box(screen, question + ': ' + string.join(current_string, ''))
    while True:
        token = get_key()
        if token == K_BACKSPACE:
            current_string = current_string[0: -1]
        elif token == K_RETURN:
            break
        elif token == K_MINUS:
            current_string.append("_")
        elif token == K_ESCAPE:
            return None
        elif token <= 127:
            current_string.append(str(token))

        display_box(screen, question + ': ' + string.join(current_string, ''))

    return string.join(current_string, '')
