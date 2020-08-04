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


COLUMNS = ('N>140,5', 'N<140,5', 'N>145,5', 'N<145,5',
           'N>148,5', 'N<148,5', 'N>150,5', 'N<150,5',
           'N>152,5', 'N<152,5', 'N>155,5', 'N<155,5',
           'N>160,5', 'N<160,5')

DICT_OF_NAME_COLUMNS = {0: '',
                        1: 'Среднее\n',
                        2: 'Среднее\nбез 1\n',
                        3: 'Среднее\nбез 2\n'}


if __name__ == '__main__':
    print()
