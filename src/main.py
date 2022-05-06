from jumper import DoodleJump
from locations.start import StartLocation
from locations.game import GameLocation
import utility.loader as Loader
import pygame


# application entry point
def main():
    settings = Loader.get_settings()
    game = DoodleJump(settings)
    start_location = StartLocation(game, settings)

    game.location = start_location
    clock = pygame.time.Clock()
    while True:
        clock.tick(settings['max_fps'])
        game.location.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            game.location.event(event)
            game.event(event)


if __name__ == '__main__':
    main()
