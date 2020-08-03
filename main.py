import requests
import constants


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





if __name__ == '__main__':
    parse()
