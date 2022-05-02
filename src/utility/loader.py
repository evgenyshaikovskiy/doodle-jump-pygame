import json

# there is a problem with settings
# each time we get setting, we read file again


def __parse_settings__():
    with open('src/utility/settings.json') as sgs_file:
        settings = json.load(sgs_file)

    return settings


settings = __parse_settings__()


def get_setting(key: str):
    return settings[key]
