import json


settings = None


def get_settings(key: str):
    if settings is None:
        __parse_settings__()

    return settings[key]


def __parse_settings__():
    with open('src/utility/settings.json') as sgs_file:
        settings = json.load(sgs_file)
