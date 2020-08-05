from datetime import datetime
import requests
import constants
import re
import excel


file = excel.ExcelFile()


def parse_every_page(needed: int):
    file.clear_filter()
    page = 1
    data = constants.DATA.copy()
    circulations = []
    while needed > 0:
        start = datetime.now()
        data['page'] = str(page)
        html = requests.post('https://www.stoloto.ru/draw-results/12x24/load',
                             headers=constants.HEADERS,
                             data=data)
        if not html.ok:
            return

        html = html.text
        circulations += tuple(map(lambda numbers: sum(numbers[1:]), statistics(html)))
        needed -= len(re.findall(r'>\d{6}', html))
        page += 1
        print('Время парса одной страницы -', datetime.now() - start)
    file.write_statistics(tuple(circulations))


def get_circulations(html) -> tuple:
    """
        Вычленение тиражей.
    :param html:    исходный код
    :return:        Тиражи в кортеже, первый элемент номер, второй кортеж чисел
    """
    numbers = tuple(x[3:] for x in re.findall(r'<b>[^&]*', html))
    circulations = []
    for index, game in enumerate(re.findall(r'>\d{6}', html)):
        circulations.append((int(game[1:]), *map(lambda number: int(number), numbers[index * 12: 12 * (index + 1)])))
    return tuple(circulations)


def statistics(html: str) -> tuple:
    """
        Запись тиражей параллельно с сохранением данных
    :param html:
    :return:
    """
    circulations = get_circulations(html)
    file.write_data(circulations, 'Отфильтрованные записи')
    return circulations


def every_parsing():
    html = requests.post('https://www.stoloto.ru/draw-results/12x24/load',
                         headers=constants.HEADERS,
                         data=constants.DATA)
    if not html.ok:
        return

    file.write_data(get_circulations(html.text), 'Архив')


if __name__ == '__main__':
    # parse_every_page(500)
    every_parsing()

