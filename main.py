from time import sleep
from datetime import datetime
import requests
import constants
import re
import excel


file = excel.ExcelFile()


def parse_every_page(needed: int, label, ls_of_labels):
    """
        for full download
    :param needed:
    :return:
    """
    file.create_file(True)
    page = 1
    data = constants.DATA.copy()
    circulations = []
    general_amount = needed
    while needed > 0:
        start = datetime.now()
        data['page'] = str(page)
        html = requests.post('https://www.stoloto.ru/draw-results/12x24/load',
                             headers=constants.HEADERS,
                             data=data)
        if not html.ok:
            return

        html = html.text

        if html != '{"status":"ok","data":"","stop":true,"order":false}':   # if amount of record the end
            stat = statistics(html)
            if len(stat) < 5:
                continue
            else:
                circulations += tuple(map(lambda numbers: sum(numbers[1:]), stat))
                needed -= len(re.findall(r'>\d{6}', html))
                page += 1
                label['text'] = str(int((general_amount - needed) / general_amount * 100)) + '%'
                # label['text'] = f'Осталось {str(needed)}, страница - {str(page)}, Время парса одной страницы - {datetime.now() - start}'
                # print(f'Осталось {str(needed)}, страница - {str(page)}, Время парса одной страницы -', datetime.now() - start)
        else:
            label['text'] = '100%'
            break
    # file.write_statistics(tuple(circulations), 'Отфильтрованные записи')
    file.write_statistics(tuple(circulations), 'Архив')

    for btn in ls_of_labels:
        btn['state'] = 'active'

    from windows import timer, autoupdate
    import threading
    autoupdate = True
    threading.Thread(target=timer).start()


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
    file.write_data(circulations, 'Архив')
    return circulations


def every_parsing():
    """
        for every thirty minets
    :return:
    """
    html = requests.post('https://www.stoloto.ru/draw-results/12x24/load',
                         headers=constants.HEADERS,
                         data=constants.DATA)
    if not html.ok:
        return

    file.write_data((get_circulations(html.text)[0], 1), 'Архив')


def get_static(needed: int, label, ls_of_buttons):
    """
        for generate static
    :param needed:
    :return:
    """
    file.clear_filter()
    # return
    file.make_static(needed)
    label['text'] = f'Обработка завершена.'
    for btn in ls_of_buttons:
        btn['state'] = 'active'


if __name__ == '__main__':
    # parse_every_page(5000)    # full download
    # every_parsing()
    # get_static(5000)
    file.close()

