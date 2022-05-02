import pygame


class Rectangle(pygame.Surface):
    def __init__(self, width, height, color):
        pygame.Surface.__init__(self, (width, height))
        self.fill(color)
