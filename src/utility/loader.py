import json


settings = None


def get_settings():
    if settings is None:
        __parse_settings__()

    return settings


def __parse_settings__():
    with open('src/utility/settings.json') as sgs_file:
        settings = json.load(sgs_file)
