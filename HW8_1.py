class Data:

    @staticmethod
    def is_right_date(input_data):
        date_to_validate = input_data.split('-')
        return int(date_to_validate[0]) <= 31 and int(date_to_validate[1]) <= 12

    def __init__(self, input_data):
        if self.is_right_date(input_data) is False:
            print('Неверный формат даты')
        else:
            self.input_data = input_data

    @classmethod
    def split_date(cls, input_data):
        return input_data.split('-')


date1 = Data('12-35-2012')

