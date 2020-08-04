from datetime import datetime
import requests
import constants
import re
import excel
import numpy as np


def parse_every_page():
    pass


def parse():
    html = requests.post('https://www.stoloto.ru/draw-results/12x24/load',
                         headers=constants.HEADERS,
                         data=constants.DATA)
    if not html.ok:
        return

    html = html.text

    #######################################################################

    numbers = tuple(x[3:] for x in re.findall(r'<b>[^&]*', html))
    circulations = []
    for index, game in enumerate(re.findall(r'>\d{6}', html)):
        circulations.append((game[1:], numbers[index * 12: 12 * (index + 1)]))
    file = excel.ExcelFile()
    file.write_circulations(tuple(circulations))





if __name__ == '__main__':
    parse()
