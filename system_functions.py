import logging
import json


logger = logging.getLogger()
logger.setLevel('INFO')


def load_settings(settings_file: str) -> dict:
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
    except OSError as err:
        logging.warning(f"Settings file was not loaded from file {settings_file}\n{err}")
    return settings


def load_text(file_name: str) -> str:
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.read()
    except OSError as err:
        logging.warning(f' Text was not read from file {file_name}\n{err}')
    return text


def load_list(file_name: str) -> list:
    text = []
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.readlines()
        text = list(map(int, text))
    except OSError as err:
        logging.warning(f' Text was not read from file {file_name}\n{err}')
    return text


def write_text(text: str, file_name: str) -> None:
    try:
        with open(file_name, mode='w') as text_file:
            text_file.write(text)
    except OSError as err:
        logging.warning(f' Text was not written to file {file_name}\n{err}')