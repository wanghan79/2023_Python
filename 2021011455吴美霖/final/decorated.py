import random


def dataProcess(*arg):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            # print(data)
            result = dict()
            result["data"] = data
            s = [0, 0, 0, 0, 0, 0]
            for item in data:
                for i in range(6):
                    s[i] = s[i]+item[i]
            for a in arg:
                if a == "sum":
                    # print("sum:", s)
                    result["sum"] = s
                elif a == "avg":
                    avg = [0, 0, 0, 0, 0, 0]
                    for i in range(6):
                        avg[i] = s[i]/len(data)
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
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
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
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
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
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
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
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def decorator(para):
    print("生成随机数")
    print(structDataSampling(**para))
    print("生成随机数求和")
    print(structDataSampling_sum(**para))
    print("生成随机数求平均")
    print(structDataSampling_avg(**para))
    print("生成随机数求和求平均")
    print(structDataSampling_sum_avg(**para))


if __name__=='__main__':
    para = {
        "num": 10,
        "struct": (
            {
                'datatype': "int",
                'datarange': [1, 100]
            },
            {
                'datatype': "int",
                'datarange': [100, 250]
            },
            {
                'datatype': "int",
                'datarange': [100, 250]
            },
            {
                'datatype': "int",
                'datarange': [100, 250]
            },
            {
                'datatype': "int",
                'datarange': [100, 250]
            },
            {
                'datatype': "int",
                'datarange': [100, 250]
            }
        )
    }
    decorator(para)