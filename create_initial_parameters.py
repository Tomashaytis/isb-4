import json

SETTINGS = {
    'card_number_file': 'files/card_number.txt',
    'statistics_file': 'files/statistics.txt',
    'hash_file': 'files/hash.txt',
    'bins_file': 'files/bins.txt',
    'last_numbers_file': 'files/last_numbers.txt',
    'visual_directory': 'files'
}

if __name__ == '__main__':
    with open('files/settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)
