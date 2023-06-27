import random


def dataProcess(*arg):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            # print(data)
            result = dict()
            result["data"] = data
            w = [0, 0, 0, 0, 0, 0]
            for item in data:
                for i in range(6):
                    w[i] = w[i]+item[i]
            for a in arg:
                if a == "sum":
                    # print("sum:", w)
                    result["sum"] = w
                elif a == "avg":
                    avg = [0, 0, 0, 0, 0, 0]
                    for i in range(6):
                        avg[i] = w[i]/len(data)
                    # print("avg:", avg)
                    result["avg"] = avg
            return result
        return wrapper
    return decorator


@dataProcess()
def structDataSampling(**kwargs):
    """

    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key in kwargs['struct']:
            if key['datatype'] == 'int':
                it = iter(key['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key['datatype'] == 'float':
                it = iter(key['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(key['datarange'])for _ in range(key['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

@dataProcess("sum")
def structDataSampling_sum(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key in kwargs['struct']:
            if key['datatype'] == "int":
                it = iter(key['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key['datatype'] == "float":
                it = iter(key['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(key['datarange']) for _ in range(key['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


@dataProcess("avg")
def structDataSampling_avg(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key in kwargs['struct']:
            if key['datatype'] == "int":
                it = iter(key['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key['datatype'] == "float":
                it = iter(key['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(key['datarange']) for _ in range(key['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


@dataProcess("sum","avg")
def structDataSampling_sum_avg(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key in kwargs['struct']:
            if key['datatype'] == "int":
                it = iter(key['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key['datatype'] == "float":
                it = iter(key['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(key['datarange']) for _ in range(key['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def decorator():
    para = {
        "num": 10,
        "struct": (
            {
                'datatype': "int",
                'datarange': [1, 100]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            }
        )
    }
    print("生成随机数:")
    print(structDataSampling(**para))
    print("随机数求和:")
    print(structDataSampling_sum(**para))
    print("随机数求平均:")
    print(structDataSampling_avg(**para))
    print("随机数求和求平均:")
    print(structDataSampling_sum_avg(**para))


if __name__ == '__main__':

    decorator()