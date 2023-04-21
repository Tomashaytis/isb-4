import hashlib
import logging

logger = logging.getLogger()
logger.setLevel('INFO')


def hashing(number: str) -> str:
    return hashlib.sha384(number.encode()).hexdigest()


def enumerate_number(last_numbers: str, original_hash: str) -> str:
    for i in range(0, 1000000000000):
        if hashing(f'{i:12d}{last_numbers}') == original_hash:
            logging.info(f" The true card number was found: {f'{i:12d}{last_numbers}'}")
            return f'{i:12d}{last_numbers}'
    logging.info(f" The true card number was not found")
    return ''
