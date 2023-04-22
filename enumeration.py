import hashlib
from typing import Union
import logging
import multiprocessing as mp
from system_functions import load_settings, load_text, load_list, write_text
from tqdm import tqdm

CORES = mp.cpu_count()
logger = logging.getLogger()
logger.setLevel('INFO')


def check_card_number(main_card_number_part: int) -> Union[str, bool]:
    path_to_settings = load_text('path_to_settings.txt')
    settings = load_settings(path_to_settings)
    original_hash = load_text(settings['hash_file'])
    last_numbers = load_text(settings['last_numbers_file'])
    bins = load_list(settings['bins_file'])
    for card_bin in bins:
        card_number = f'{card_bin}{main_card_number_part:06d}{last_numbers}'
        if hashlib.sha384(card_number.encode()).hexdigest() == original_hash:
            return card_number
    return False


def enumerate_card_number(path_to_settings, pools=CORES) -> str:
    write_text(path_to_settings, 'path_to_settings.txt')
    with mp.Pool(processes=pools) as p:
        for result in p.map(check_card_number, tqdm(range(0, 1000000),
                                                    desc='The process of enumerating the true card number: ', ncols=120)):
            if result:
                logging.info(f" The true card number was found: {result}")
                p.terminate()
                return result
    logging.info(f" The true card number was not found")
    return ''

# tqdm(range(0, 1000000), desc='The process of enumerating the true card number: ', ncols=120):
