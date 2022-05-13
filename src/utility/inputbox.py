import pygame
from pygame.locals import *


def display_box(screen, message):
    fontobject = pygame.font.Font('src/assets/papernotes_font.ttf', 25)

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (
            (screen.get_width() / 2) - 200,
            (screen.get_height() / 2) - 10,
            350,
            50),
        0
    )

    # pygame.draw.rect(
    #     screen,
    #     (255, 255, 255),
    #     (
    #         (screen.get_width() / 2) - 102,
    #         (screen.get_height() / 2) - 12,
    #         204,
    #         42
    #     ),
    #     1
    # )

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
    text: str = ''
    display_box(screen, question + ':  ' + text)
    typing = True
    while typing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Enter button
                if (event.key) == 13:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        display_box(screen, question + ':' + text)

    return text
