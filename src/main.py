import json
from game.jumper import DoodleJump


# application entry point
def main():
    game_settings = parse_settings()
    DoodleJump(game_settings).run()


def parse_settings():
    with open('src/utility/settings.json') as sgs:
        settings = json.load(sgs)

    return settings


if __name__ == '__main':
    main()
