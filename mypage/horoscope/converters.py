class FourDigitYearConverter:
    regex = '[1-2][9,0][0-9][0-9]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return f'{value}'


class SplitConvertor:
    regex = '(\w+)(,\w+)*'

    def to_python(self, value):
        return value.split(',')

    def to_url(self, value):
        return ','.join(value)

