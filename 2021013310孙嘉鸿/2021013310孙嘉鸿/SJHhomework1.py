import random

def generate_int(datarange):
    it = iter(datarange)
    return random.randint(next(it), next(it))

def generate_float(datarange):
    it = iter(datarange)
    return random.uniform(next(it), next(it))

def generate_str(datarange, length):
    return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))

def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs.get('num', 0)):
        element = []
        for key, value in kwargs.get('struct', {}).items():
            if value['datatype'] == 'int':
                tmp = generate_int(value['datarange'])
            elif value['datatype'] == 'float':
                tmp = generate_float(value['datarange'])
            elif value['datatype'] == 'str':
                tmp = generate_str(value['datarange'], value['len'])
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

param = {
    "struct": ({"type": int,
                "range": [0, 100]
                },
               {"type": float,
                "range": [0, 100]
                },
               {"type": str,
                "range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                "len": 10
                })
}
dataSampling(**param)