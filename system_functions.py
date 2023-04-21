import logging
import json


logger = logging.getLogger()
logger.setLevel('INFO')


def load_settings(settings_file: str) -> dict:
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f"Settings file successfully loaded from file {settings_file}")
    except OSError as err:
        logging.warning(f"Settings file was not loaded from file {settings_file}\n{err}")
    return settings


def load_text(file_name: str) -> str:
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.read()
        logging.info(f' Text was successfully read from file {file_name}')
    except OSError as err:
        logging.warning(f' Text was not read from file {file_name}\n{err}')
    return text


def load_list(file_name: str) -> list:
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.readlines()
        logging.info(f' List was successfully read from file {file_name}')
    except OSError as err:
        logging.warning(f' Text was not read from file {file_name}\n{err}')
    return text
