import os
import time
import argparse
import logging
from system_functions import load_settings, load_text, write_text, add_to_statistics, load_statistics
from enumeration import enumerate_card_number
from vizualization import visualize_statistics
from correction import luhn_algorithm

SETTINGS_FILE = os.path.join('files', 'settings.json')
logger = logging.getLogger()
logger.setLevel('INFO')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sbf', '--settings', type=str, help='Использование собственного файла с настройками')
    parser.add_argument('-sts', '--statistics', help='Сохраняет статистику в файл')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-enu', '--enumeration', type=int, help='Подбирает номер карты по её хэшу (Введите количество '
                                                               'порождаемых процессов)')
    group.add_argument('-cor', '--correction', help='Проверяет корректность полученного номера карты')
    group.add_argument('-vis', '--visualization', help='Визуализирует данные из файла со статистиками')
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTINGS_FILE)
    if settings:
        if args.enumeration:
            t0 = time.perf_counter()
            card_number = enumerate_card_number(args.enumeration)
            t1 = time.perf_counter()
            if args.statistics:
                add_to_statistics(args.enumeration, t1 - t0, settings['statistic_file'])
            if card_number:
                logging.info(f" The true card number was found: {card_number} ({t1 - t0} seconds required)")
                write_text(card_number, settings['card_number_file'])
            else:
                logging.info(f" The true card number was not found")
        elif args.visualization:
            statistics = load_statistics(settings['statistics_file'])
            visualize_statistics(statistics, settings['visual_directory'])
        else:
            card_number = load_text(settings['card_number_file'])
            if luhn_algorithm(card_number):
                logging.info(f" Card number {card_number} is correct")
            else:
                logging.info(f" Card number {card_number} is not correct")
