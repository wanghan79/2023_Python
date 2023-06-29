import random

def dataSampling(**kwargs):
    result = []
    for _ in range(kwargs['num']):
        element = []
        for field_name, field_config in kwargs['struct'].items():
            if field_config['type'] == 'int':
                value = get_random_int(field_config['range'])
            elif field_config['type'] == 'float':
                value = get_random_float(field_config['range'])
            elif field_config['type'] == 'str':
                value = get_random_str(field_config['range'], field_config['length'])
            else:
                break
            element.append(value)
        result.append(element)
    return result


def get_random_int(datarange):
    it = iter(datarange)
    return random.randint(next(it), next(it))

def get_random_float(datarange):
    it = iter(datarange)
    return random.uniform(next(it), next(it))

def get_random_str(datarange, length):
    return ''.join(random.SystemRandom().choice(datarange) for _ in range(length))


x = dataSampling(num=5, struct={
            'x1': {'type': 'int', 'range': [0, 10]},
            'x2': {'type': 'float', 'range': [0, 1]},
            'x3': {'type': 'str', 'range': ['a', 'b', 'c', 'd'], 'length': 3}
        })
print(x)
