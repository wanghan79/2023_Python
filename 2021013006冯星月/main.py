import Weather
import dataSampling
import Computing
def function_one():
    a = 5

    b = {'data': {'datatype': str, 'datarange': ('f', 'x', 'y'), 'len': 7},
    'data1': {'datatype': str, 'datarange': ('f', 'x', 'y'), 'len': 7}}
    h1 = dataSampling.hw01()
    h1.show(a, b)


def function_two():
    h2 = Computing.hw02()
    h2.show(5, 60)

def function_three():
    h3 = Weather.hw03()
    a = ['北京', '长春']
    h3.show(a)
while True:
    user_input = int(input("请输入一个值【1】随机数【2】计算【3】天气 输入其他值退出："))

    if user_input == 1:
        function_one()
    elif user_input == 2:
        function_two()
    elif user_input == 3:
        function_three()
    else:
        break


