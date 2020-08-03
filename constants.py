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


if __name__ == '__main__':
    print()
