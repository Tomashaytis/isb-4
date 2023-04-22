import hashlib
from typing import Union, Optional
import multiprocessing as mp
from tqdm import tqdm

BINS = (530114, 544716, 552702, 559992, 512347, 518365, 521155, 522477, 542247, 543367, 543762, 548328, 548791)
ORIGINAL_HASH = '50c6b2ca7a569f006d23b3be8007dd775652c1028c2c44bbb3847008956e179e4f8cc315d8076cf97483279e44075424'
LAST_NUMBERS = 1512
CORES = mp.cpu_count()


def check_card_number(main_card_number_part: int) -> Union[str, bool]:
    """
    The function assemblies a card number and checks the matching the true hash value and a card number hash.

    :param main_card_number_part: unknown part of card_number.
    :return: card number if a card number hash matches to the true hash value and False otherwise.
    """
    for card_bin in BINS:
        card_number = f'{card_bin}{main_card_number_part:06d}{LAST_NUMBERS}'
        if hashlib.sha384(card_number.encode()).hexdigest() == ORIGINAL_HASH:
            return card_number
    return False


def enumerate_card_number(pools=CORES) -> Optional[str]:
    """
    The function enumerates the true card number by known hash.

    :param pools: number of generated processes.
    :return: enumerated card number if it was found and None instead.
    """
    with mp.Pool(processes=pools) as p:
        for result in p.map(check_card_number,
                            tqdm(range(0, 1000000),
                                 desc='The process of enumerating the true card number: ', ncols=120)):
            if result:
                p.terminate()
                return result
    return None
