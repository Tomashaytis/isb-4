import logging
import json


logger = logging.getLogger()
logger.setLevel('INFO')


def load_settings(settings_file: str) -> dict:
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info(f' Settings file successfully loaded from the file "{settings_file}"')
    except OSError as err:
        logging.warning(f' Settings file was not loaded from the file "{settings_file}"\n{err}')
    return settings


def load_text(file_name: str) -> str:
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.read()
        logging.info(f' Text was successfully loaded from the file "{file_name}"')
    except OSError as err:
        logging.warning(f' Text was not read from the file "{file_name}"\n{err}')
    return text


def load_list(file_name: str) -> list:
    text = []
    try:
        with open(file_name, mode='r') as text_file:
            text = text_file.readlines()
        text = list(map(int, text))
        logging.info(f' List was successfully loaded from the file "{file_name}"')
    except OSError as err:
        logging.warning(f' Text was not read from the file "{file_name}"\n{err}')
    return text


def load_statistics(file_name: str) -> dict:
    statistics = {}
    try:
        with open(file_name, mode='r') as text_file:
            lines = text_file.readlines()
    except OSError as err:
        logging.warning(f' Statistics was not loaded from the file "{file_name}"\n{err}')
    for line in lines:
        line = list(map(float, line.split()))
        statistics[line[0]] = line[1]
    logging.info(f' Statistics was successfully loaded from the file "{file_name}"')
    return statistics


def write_text(text: str, file_name: str) -> None:
    try:
        with open(file_name, mode='w') as text_file:
            text_file.write(text)
        logging.info(f' Text was successfully written to the file "{file_name}"')
    except OSError as err:
        logging.warning(f' Text was not written to the file "{file_name}"\n{err}')


def add_to_statistics(pools: int, time: float, file_name: str) -> None:
    try:
        with open(file_name, mode='a') as text_file:
            text_file.write(f'{pools} {time}\n')
        logging.info(f' Statistics was successfully added to the file "{file_name}"')
    except OSError as err:
        logging.warning(f' Statistics was not added to the file "{file_name}"\n{err}')

