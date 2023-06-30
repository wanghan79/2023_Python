import random


def sum(data):
    result = list()
    sum = 0
    for i in range(0, len(data[0])):
        for j in range(0, len(data)):
            sum += data[j][i]
    return sum


def avg(data):
    result = sum(data)
    return result / len(data[0])


def dataOperation(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list()
            datas = func(*args, **kwargs)
            for item in oder:
                if item == "SUM":
                    result.append('SUM=' + str(sum(datas)))
                if item == "AVG":
                    result.append('AVG=' + str(avg(datas)))
            return result
        return wrapper
    return decorator


@dataOperation("SUM", "AVG")
def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result


def main2():
    para = structDataSampling(num=3,
                              struct={'data1': {'datatype': 'int', 'datarange': [0, 100]},
                                      'data2': {'datatype': 'int', 'datarange': [0, 100]}})

    print(para)


if __name__ == '__main__':

    main2()