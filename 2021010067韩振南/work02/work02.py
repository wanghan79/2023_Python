# 在上次作业的基础上，生成60个五维向量，修饰器进行求和或者求均值（根据参数决定）
import random


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
    print(f"<---此次数据的总和为{m}--->")


def average(temp):
    m = 0
    for i, element in enumerate(temp):
        n = 0
        for j in iter(element):
            n = n + j
        print(f"第{i}组数据的均值为{n / len(element)}")
        m = m + n
    print("------------------------")
    print(f"<---此次数据的总均值为{m / len(temp)}--->")


def aop(choose):
    def decorator(function):
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            # 修饰的内容
            temp = function(*args, **kwargs)
            print(type(temp))
            if choose == 1:
                sum(temp)
            elif choose == 2:
                average(temp)
            elif choose == 3:
                sum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator


def aop2():
    def decorator(function):
        def wrapper(*args, **kwargs):  # 实际做事的部分，集成了修饰功能和老函数的功能
            choose = args[0]
            # 修饰的内容
            temp = function(*args, **kwargs)
            if choose == 1:
                sum(temp)
            elif choose == 2:
                average(temp)
            elif choose == 3:
                sum(temp)
                print("------------------------")
                average(temp)
            else:
                print("修饰器未工作")
            return temp

        return wrapper  # 返回整体的wrapper，

    return decorator


@aop(1)
def func(num):
    return structDataSampling(num,
                              {int: {'datarange': ((0, 100), (0, 100), (0, 100))},
                               float: {"datarange": ((0, 1.0), (0, 5.0))}})


print(func(60))


@aop2()
def func(choose, num):
    return structDataSampling(num,
                              {int: {'datarange': ((0, 100), (0, 100), (0, 100))},
                               float: {'datarange': ((0, 1.1),)}})


print(func(1, 60))
