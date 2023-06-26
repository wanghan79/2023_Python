class ChooseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def choose_input(m, y=4, z=1):
    while True:
        try:
            x = input(m)
            if not x.isdigit():
                raise ChooseError('请输入数字')
            x = int(x)
            if x > y or x < z:
                raise ChooseError('请输入正确的数字')
            return x
        except ChooseError as e:
            print("输入错误:", e.value)


class CityError(Exception):
    def __init__(self, message):
        self.message = message
