import random

def DataSampling(**kwargs):
    result = []
    for index in range(kwargs['num']):
        element = []
        for key, value in kwargs['struct'].items():
            if value['type'] == 'int':
                a = getint(value['datarange'])
                tmp = a
            elif value['type'] == 'float':
                tmp = getfloat(value['datarange'])
            elif value['type'] == 'str':
                tmp = getstr(value['datarange'], value['len'])
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def getint(datarange):
    it = iter(datarange)
    return random.randint(next(it), next(it))

def getfloat(datarange):
    it = iter(datarange)
    return random.uniform(next(it), next(it))

def getstr(datarange, length):
    return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))


if __name__ == '__main__':
    try:
        x = DataSampling(num=5, struct={
            'x1': {'type': 'int', 'datarange': [0, 10]},
            'x2': {'type': 'float', 'datarange': [0, 1]},
            'x3': {'type': 'str', 'datarange': ['a', 'b', 'c','d'], 'len': 3}
        })
        print(x)
    except (TypeError, KeyError):
        print("error")
