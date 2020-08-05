from datetime import datetime, timedelta


HEADERS = {
           'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Host': 'www.stoloto.ru',
           'Origin': 'https://www.stoloto.ru',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Site': 'same-origin',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest',
          }

DATA = {
        'page': '1',
        'mode': 'date',
        'super': 'false',
        'from': (datetime.now() - timedelta(days=101)).strftime('%d.%m.%Y'),
        'to': datetime.now().strftime('%d.%m.%Y'),
       }

RESULT_FILE_NAME = 'result.xlsx'


COLUMNS = ('N>140.5', 'N<140.5', 'N>145.5', 'N<145.5',
           'N>148.5', 'N<148.5', 'N>150.5', 'N<150.5',
           'N>152.5', 'N<152.5', 'N>155.5', 'N<155.5',
           'N>160.5', 'N<160.5')

DICT_OF_NAME_COLUMNS = {1: '',
                        3: 'Среднее\n',
                        5: 'Среднее\nбез 1\n',
                        7: 'Среднее\nбез 2\n'}

COLORS = ('00FF6600',) * 2 + \
         ('00008080',) * 2 + \
         ('00660066',) * 2 + \
         ('0099CC00',) * 2 + \
         ('00993300',) * 2 + \
         ('000000FF',) * 2 + \
         ('00808000',) * 2

FONT = dict(color="FFFFFF",
            name='Calibri',
            size=14)

BORDER = {side: 'medium' for side in ('right', 'left', 'top', 'bottom')}


if __name__ == '__main__':
    print()
