import logging
import json


def load_settings(settings_file: str) -> dict:
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f"Settings file successfully loaded from file {settings_file}")
    except OSError as err:
        logging.warning(f"Settings file was not loaded from file {settings_file}\n{err}")
    return settings
