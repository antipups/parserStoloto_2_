from os import path
from time import sleep
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Color, PatternFill, Font, Side, Border, Alignment
from constants import *
import calculate


class ExcelFile:

    def __init__(self):
        self.wb = self.create_file()
        self.save()

    def create_file(self) -> Workbook:
        if path.exists(path.abspath(RESULT_FILE_NAME)):
            wb = load_workbook(path.abspath(RESULT_FILE_NAME))
        else:
            wb = Workbook()
            for name in ('Архив', 'Отфильтрованные записи'):
                wb.create_sheet(name)

                for row in range(1, 8, 2):
                    for column, (name_col, color) in enumerate(zip(tuple(DICT_OF_NAME_COLUMNS.get(row) + title for title in COLUMNS), COLORS), start=1):
                        cell = wb[name].cell(row, column, name_col)
                        cell.alignment = Alignment(wrapText=True, horizontal='center')
                        self.cell_decorate(cell, color, {'size': 10})

                for _ in range(3):
                    wb[name].append(('',))

                wb[name].append(('Тираж', *(x for x in range(1, 13)), 'Сумма'))
            wb.remove(wb['Sheet'])
        return wb

    def save(self):
        while True:
            try:
                self.wb.save(path.abspath(RESULT_FILE_NAME))
                # self.wb.close()
            except:
                sleep(1)
                continue
            else:
                return

    def write_data(self, data: tuple, table: str):
        """
        write to excel circulations
        :param table:
        :param data: number_of_circl + tuple a numbers
        :return:
        """
        if table == 'Архив':
            self.wb[table].insert_rows(13, len(data))
            row, column = 13, 1

            for circulation in data:
                column = 1
                for value in (circulation + (sum(circulation[1:]),)):
                    self.wb[table].cell(row, column, value)
                    column += 1
                row += 1

        else:
            for circulation in data:
                self.wb[table].append(circulation + (sum(circulation[1:]),))
        self.save()

    def write_statistics(self, data: tuple):
        calc = calculate.Calculator(data)
        for index, (first, second, third, fourth, color) in enumerate(zip(calc.first_dict_answer.values(),
                                                                          calc.second_dict_answer.values(),
                                                                          calc.third_dict_answer.values(),
                                                                          calc.fourth_dict_answer.values(),
                                                                          COLORS),
                                                                      start=1):

            for row in (2, 4, 6, 8):
                self.cell_decorate(self.wb['Отфильтрованные записи'].cell(row, index, fourth), color)

        self.save()

    def cell_decorate(self, cell, color, Font_=FONT):
        cell.fill = PatternFill(patternType='solid', fgColor=Color(rgb=color))
        cell.font = Font(**Font_)
        cell.border = Border(**{key: Side(style=value) for key, value in BORDER.items()})

    def clear_filter(self):
        self.wb['Отфильтрованные записи'].delete_rows(13, 5000)


def main():
    excel = ExcelFile()


if __name__ == '__main__':
    main()


