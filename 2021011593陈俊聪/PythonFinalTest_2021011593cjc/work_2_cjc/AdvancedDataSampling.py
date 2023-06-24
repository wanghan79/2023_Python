# 在上次作业的基础上，生成60个五维向量，修饰器进行求和或者求均值（根据参数决定）  第二次作业
import random
from functools import wraps


def structDataSampling(num, struct):
    result = list()
    for index in range(0, num):
        element = list()
        for key, values in struct.items():
            for value in values["datarange"]:
                if key is int:
                    it = iter(value)
                    tmp = random.randint(next(it), next(it))
                elif key is float:
                    it = iter(value)
                    tmp = random.uniform(next(it), next(it))
                elif key is str:
                    tmp = ''.join(random.SystemRandom().choice(values['datarange']) for _ in range(value['len']))
                else:
                    break
                element.append(tmp)
        result.append(element)
    return result


def sum(temp):
    m = 0
    for i, element in enumerate(temp):
        n = 0
        for j in iter(element):
            n = n + j
        print(f"第{i}组数据的和为{n}")
        m = m + n
    print("------------------------")
    print(f"数据总和为{m}")


def average(temp):
    m = 0
    for i, element in enumerate(temp):
        n = 0
        for j in iter(element):
            n = n + j
        print(f"第{i}组数据的均值为{n / len(element)}")
        m = m + n
    print("------------------------")
    print(f"数据的总均值为{m / len(temp)}")


def Calculation(choose):
    def decorator(function):
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            # 修饰的内容
            temp = function(*args, **kwargs)
            if choose == "sum":
                sum(temp)
            elif choose == "avg":
                average(temp)
            elif choose == "sum and avg":
                sum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator


@Calculation("sum and avg")
def func(num):
    return structDataSampling(num,
                              {int: {'datarange': ((0, 100), (0, 100), (0, 100))},
                               float: {"datarange": ((0, 1.0), (0, 5.0), (0, 6.0))}})


def example(num):
    print(func(num))

# 老师要求的例子，函数修饰器
# def calculation(*args):#[sum,avg]
#     def decorater(func):
#         @wraps #
#         def wrapper(*args,**kwargs):#功能老代码添加新功能
#             return sum or average
#
#         return wraps
#
#     return decorater
