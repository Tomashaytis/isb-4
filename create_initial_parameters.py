import json

SETTINGS = {
    'card_number_file': 'files/card_number.txt',
    'statistic_file': 'files/statistics.txt'
}

if __name__ == '__main__':
    with open('files/settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)
