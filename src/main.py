from jumper import DoodleJump
from locations.start import StartLocation
from locations.game import GameLocation
import utility.loader as sgs
import pygame


# application entry point
def main():
    game = DoodleJump()
    start_location = StartLocation(game)

    game.location = start_location
    clock = pygame.time.Clock()
    while True:
        clock.tick(sgs.get_setting('max_fps'))
        game.location.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            game.location.event(event)
            game.event(event)


if __name__ == '__main__':
    main()
