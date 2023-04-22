import os
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel('INFO')


def visualize_statistics(statistics: dict, visual_directory: str) -> None:
    fig = plt.figure(figsize=(30, 5))
    plt.ylabel('Work time, s')
    plt.xlabel('Processes')
    plt.title('Enumeration statistics')
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color='teal', width=0.5)
    plt.savefig(os.path.join(visual_directory, 'statistics.png'))
    logging.info(f'Visual was successfully saved to the directory "{visual_directory}"')

