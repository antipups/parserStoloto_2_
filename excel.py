from os import path
from time import sleep
import openpyxl
from constants import *


class ExcelFile:

    def __init__(self):
        self.wb = self.create_file()
        self.save()

    def create_file(self) -> openpyxl.Workbook:
        if path.exists(path.abspath(RESULT_FILE_NAME)):
            wb = openpyxl.load_workbook(path.abspath(RESULT_FILE_NAME))
        else:
            wb = openpyxl.Workbook()
            for name in ('Архив', 'Отфильтрованные записи'):
                wb.create_sheet(name)
                for i in range(4):
                    wb[name].append((DICT_OF_NAME_COLUMNS.get(i) + title for title in COLUMNS))
                    wb[name].append((1, ) * 14)
                for _ in range(3):
                    wb[name].append(('',))
                wb[name].append(('Тираж', *(x for x in range(1, 13)), 'Сумма'))
            wb.remove(wb['Sheet'])
        return wb

    def save(self):
        while True:
            try:
                self.wb.save(path.abspath(RESULT_FILE_NAME))
            except:
                sleep(1)
                continue
            else:
                return

    def write_circulations(self, data: tuple):
        """
        write to excel circulations
        :param data: number_of_circl + tuple a numbers
        :return:
        """
        for circulation in data:
            temp_circulation = tuple(map(lambda x: int(x), circulation[1]))
            self.wb['Архив'].append((int(circulation[0]), *temp_circulation, sum(temp_circulation)))
        self.save()


def main():
    excel = ExcelFile()


if __name__ == '__main__':
    main()


