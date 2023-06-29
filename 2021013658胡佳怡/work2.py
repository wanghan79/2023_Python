
import random
# 随机数生成的修饰器，进行求和或求均值或两者都要



def dataProcess(*arg):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            result = dict()
            result["data"] = data
            s = [0, 0, 0, 0, 0, 0]
            for item in data:
                for i in range(6):
                    s[i] = s[i]+item[i]
            for a in arg:
                if a == "sum":
                    result["sum"] = s
                elif a == "avg":
                    avg = [0, 0, 0, 0, 0, 0]
                    for i in range(6):
                        avg[i] = s[i]/len(data)
                    result["avg"] = avg
            return result
        return wrapper
    return decorator


@dataProcess("sum", "avg")
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


para = {
    "num": 50,
    "struct": (
        {
            'datatype': "float",
            'datarange': [1, 100]
        },
        {
            'datatype': "float",
            'datarange': [100,250]
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
            'datarange': [100,250]
        },
        {
            'datatype': "float",
            'datarange': [100,250]
        }
    )
}

if __name__ == '__main__':
    hw02 = structDataSampling(**para)
    print(hw02)
