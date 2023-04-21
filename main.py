import argparse
from system_functions import load_settings, load_text
SETTINGS_FILE = "settings.json"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-sbf', '--settings', type=str, help='Использование собственного файла с настройками')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-enu', '--enumeration', help='Подбирает номер карты по её хэшу')
    group.add_argument('-cor', '--correction', help='Проверяет корректность полученного номера карты')
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTINGS_FILE)
    if settings:
        if args.enumeration:
            original_hash = load_text(settings['hash_file'])
            last_numbers = load_text(settings['last_numbers_file'])
        else:
            pass
