import random
import string
import logging

def dataLogging(*orders):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            data = func(*args, **kwargs)
            s = 0
            num = 0
            for i in range(0, len(data)):
                for j in range(0, len(data[i])):
                    s += data[i][j]
                    num += 1
            for item in orders:
                if item == "sum":
                    a.append(s)
                elif item == "avg":
                    a.append(s/num)
            return a
        return wrapper
    return decorator



@dataLogging("sum", "avg")
def structData(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for e, value in kwargs.items():
            if e == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result


def showstructData():
    struct = {"num": 10, "int": {"datarange": [1, 100]}, "float": {"datarange": [1, 100]}}
    result = structData(**struct)
    print("总和和平均数分别是：")
    for i in result:
        print(i)
showstructData()