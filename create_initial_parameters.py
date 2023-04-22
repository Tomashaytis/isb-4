import json

SETTINGS = {
    'card_number_file': 'files/card_number.txt',
    'statistics_file': 'files/statistics.txt',
    'visual_directory': 'files'
}

if __name__ == '__main__':
    with open('files/settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)
