import random

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


def logging(*oder):
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

@logging("sum", "avg")
def DataSampling(struct):
    result = list()
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
                continue
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def showsumavg():
    struct = {"num": 50, "datatype": ["float", "int"], "datarange": [0, 30]}
    a = DataSampling(struct)
    print("总和和平均数分别是：")
    print(a)

showsumavg()