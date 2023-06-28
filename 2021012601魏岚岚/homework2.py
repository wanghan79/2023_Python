import logging
import random
import string

def dataProcess(*orders):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            data = func(*args, **kwargs)
            sumnum = 0
            num = 0
            for i in range(0, len(data)):
                for j in range(0, len(data[i])):
                    # print(data[i][j])
                    sumnum += data[i][j]
                    num += 1
            # print(sumnum)
            # print(num)
            for item in orders:
                if item == "sum":
                    a.append(sumnum)
                elif item == "avg":
                    a.append(sumnum/num)
            return a

        return wrapper

    return decorator


@dataProcess("sum", "avg")
def DataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def showDataSampling():
    struct = {"num": 30, "int": {"datarange": [1, 100]}, "float": {"datarange": [1, 100]}}
    result = DataSampling(**struct)
    print("总和和平均数分别是：")
    for i in result:
        print(i)


showDataSampling()
