import json

SETTINGS = {
    'bins_file': 'files/BINs.txt',
    'hash_file': 'files/hash.txt',
    'card_number_file': 'files/card_number.txt',
    'last_numbers_file': 'files/last_numbers.txt',
}

if __name__ == '__main__':
    with open('files/settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)
