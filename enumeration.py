import hashlib
import logging
from tqdm import tqdm

logger = logging.getLogger()
logger.setLevel('INFO')


def check_card_number(card_number: str, original_hash: str) -> bool:
    return hashlib.sha384(card_number.encode()).hexdigest() == original_hash


def enumerate_number(original_hash: str, last_numbers: str, bins: list) -> str:
    for card_bin in bins:
        for i in tqdm(range(0, 1000000), desc='The process of enumerating a true card number: ', ncols=120):
            if check_card_number(f'{card_bin}{i:06d}{last_numbers}', original_hash):
                logging.info(f" The true card number was found: {f'{card_bin}{i:06d}{last_numbers}'}")
                return f'{card_bin}{i:06d}{last_numbers}'
    logging.info(f" The true card number was not found")
    return ''
