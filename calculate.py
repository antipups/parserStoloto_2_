import itertools
import constants


class Calculator:

    def __init__(self, data: tuple):
        self.data = data
        self.first_task()
        self.second_task()

    def first_task(self):
        self.first_dict_answer = {column: int() for column in constants.COLUMNS}
        for key in self.first_dict_answer.keys():
            func = lambda x: (x > float(key[2:]) if key.find('>') > -1 else x < float(key[2:]))
            for bool_, value in itertools.groupby(self.data, func):
                if bool_:
                    value = len(tuple(value))
                    if value > self.first_dict_answer[key]:
                        self.first_dict_answer[key] = value

    def second_task(self):
        self.second_dict_answer = {column: list() for column in constants.COLUMNS}
        self.third_dict_answer = {column: list() for column in constants.COLUMNS}
        self.fourth_dict_answer = {column: list() for column in constants.COLUMNS}

        for key in self.second_dict_answer.keys():
            func = lambda x: (x > float(key[2:]) if key.find('>') > -1 else x < float(key[2:]))
            for bool_, value in itertools.groupby(self.data, func):
                if bool_:
                    length_of_seq = len(tuple(value))
                    self.second_dict_answer[key].append(length_of_seq)
                    if length_of_seq > 1:
                        self.third_dict_answer[key].append(length_of_seq)
                    if length_of_seq > 2:
                        self.fourth_dict_answer[key].append(length_of_seq)

        for key, value in self.second_dict_answer.items():
            if len(self.second_dict_answer[key]) > 0:
                self.second_dict_answer[key] = round(sum(self.second_dict_answer[key]) / len(self.second_dict_answer[key]), 2)
            if len(self.third_dict_answer[key]) > 0:
                self.third_dict_answer[key] = round(sum(self.third_dict_answer[key]) / len(self.third_dict_answer[key]), 2)
            if len(self.fourth_dict_answer[key]) > 0:
                self.fourth_dict_answer[key] = round(sum(self.fourth_dict_answer[key]) / len(self.fourth_dict_answer[key]), 2)


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        print(Calculator(eval(f.read())).first_dict_answer)
    # tuple_ = (
    #     (True, tuple(x for x in range(5))),
    #     (False, tuple(x for x in range(7))),
    #     (True, tuple(x for x in range(6))),
    #     (False, tuple(x for x in range(10))),
    # )
    #
    # print(max(tuple_, key=lambda x: x[0] and len(x[1])))
    pass
