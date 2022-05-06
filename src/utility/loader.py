import json


def get_settings():
    with open('src/utility/settings.json') as sgs_file:
        settings = json.load(sgs_file)

    return settings
