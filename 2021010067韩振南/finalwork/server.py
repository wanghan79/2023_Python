import string

from weather.WeatherServer import WeatherIterable, func, city_input
from utils.Modifier import aop2
from utils.MyException import choose_input
from utils.RandomDataUtil import dataSampling, structDataSampling


def main_server():
    while True:
        print("以下是可选择的作业：")
        print("1.第一次作业：随机数生成")
        print("2.第二次作业：随机数据生成+aop处理")
        print("3.第三次作业：天气查询")
        print("4.退出系统")
        choose = choose_input("请输入你要查看的作业：")
        if choose == 1:
            print("<--作业1相关操作-->")
            print("int数据范围默认为0~100，float数据范围默认为0~5，str数据范围为string.ascii_letters.format('&*_')")
            print("1.生成int类型数据")
            print("2.生成float类型数据")
            print("3.生成str类型数据")
            print("4.生成结构体数据")
            print("5.展示样例")
            first_work(choose_input("请输入你要进行的操作：", 5))
            print("----------")
        elif choose == 2:
            print("<--作业2相关操作-->")
            print("1.对数据进行求和")
            print("2.对数据进行求均值")
            print("3.对数据进行求和以及均值")
            print("4.不进行任何操作")
            print(second_work(choose_input("请输入你要进行的操作：")))
            print("----------")
        elif choose == 3:
            print("<--作业3相关操作-->")
            print("1.实例展示")
            print("2.自主查询")
            third_work(choose_input("请输入你要进行的操作：", 2))
            print("----------")
        elif choose == 4:
            print("拜拜^_^")
            break


def first_work(x):
    if x == 1:
        n = choose_input("要生成多少组数据（最多100）", 100)
        print(dataSampling(int, (0, 100), n))
    elif x == 2:
        n = choose_input("要生成多少组数据（最多100）", 100)
        print(dataSampling(float, (0.0, 5.0), n))
    elif x == 3:
        n = choose_input("要生成多少组数据（最多100）", 100)
        m = choose_input("你要生成的str数据的长度（最长30）", 30)
        print(dataSampling(str, string.ascii_letters.format("&*_"), n, m))
    elif x == 4:
        n = choose_input("要生成多少组数据（最多100）", 100)
        a = choose_input("int型数据的个数（最多10）", 10, 0)
        b = choose_input("float型数据的个数（最多10）", 10, 0)
        c = choose_input("str型数据的个数（最多10）", 10, 0)
        data_struct = dict()
        if a + b + c != 0:
            if a != 0:
                data_struct[int] = dict()
                data_struct[int]['datarange'] = list()
                for x in range(a):
                    data_struct[int]['datarange'].append((0, 100))
            if b != 0:
                data_struct[float] = dict()
                data_struct[float]['datarange'] = list()
                for x in range(b):
                    data_struct[float]['datarange'].append((0.0, 5.0))
            if c != 0:
                data_struct[str] = dict()
                data_struct[str]['datarange'] = list()
                for x in range(c):
                    data_struct[str]['datarange'].append((string.ascii_letters.format("&*_"), 10))
            print(structDataSampling(n, data_struct))
        else:
            print("至少有一个数据类型的数据不为0")
    elif x == 5:
        print("<--此作业内容为生成随机数据-->")
        print("<--int类型-->")
        print(dataSampling(int, (0, 100), 3))
        print("<--float类型-->")
        print(dataSampling(float, (0.0, 5.0), 10))
        print("<--str类型-->")
        print(dataSampling(str, string.ascii_letters.format("&*_"), 10))
        print("<--结构体：2个int，1个float，2个str-->")
        print(structDataSampling(2,
                                 {int: {'datarange': [(0, 100), (0, 100)]},
                                  float: {'datarange': [(0, 5.0), ]},
                                  str: {'datarange': [
                                      (string.ascii_letters.format("&*_"), 10),
                                      (string.ascii_letters.format("&*_"), 3)]}}))


@aop2()
def second_work(x):
    return structDataSampling(60,
                              {int: {'datarange': ((0, 100), (0, 100), (0, 100))},
                               float: {'datarange': ((0, 1.1),)}})


def third_work(x):
    if x == 1:
        func(['北京', '上海', '广州', '长春'])
    elif x == 2:
        func(city_input())
