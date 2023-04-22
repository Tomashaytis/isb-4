import os
import argparse
from system_functions import load_settings, write_text
from enumeration import enumerate_card_number

SETTINGS_FILE = os.path.join('files', 'settings.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sbf', '--settings', type=str, help='Использование собственного файла с настройками')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-enu', '--enumeration', type=int, help='Подбирает номер карты по её хэшу (Введите количество '
                                                               'порождаемых процессов)')
    group.add_argument('-cor', '--correction', help='Проверяет корректность полученного номера карты')
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTINGS_FILE)
    if settings:
        if args.enumeration:
            card_number = enumerate_card_number(args.settings if args.settings else SETTINGS_FILE, args.enumeration)
            if card_number:
                write_text(card_number, settings['card_number_file'])
        else:
            pass
