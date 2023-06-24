import random

import logging


def sum(x):
    result = list()
    sum = 0
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            sum += x[i][j]
    return sum


def avg(x):
    result = sum(x)
    return result / (len(x[0]) * len(x))


def addlogging(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            result = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    a.append(sum(result))
                if item == "avg":
                    a.append(avg(result))
            return a

        return wrapper

    return decorator


@addlogging("sum", "avg")
def structDataSampling(struct):
    result = list()
    print("生成的随机数如下：")
    for i in range(0, struct['num']):
        element = list()
        for key in struct["datatype"]:
            if key == "int":
                it = iter(struct['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(struct['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(struct['datarange']) for _ in range(struct['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
        print(element)
    return result


if __name__ == '__main__':
    struct = {"num": 30, "datatype": ["float", "float", "float", "int", "float"], "datarange": [0, 30]}
    a = structDataSampling(struct)
    print("结果如下：")
    print("sum == ", a[0], "avg == ", a[1])
