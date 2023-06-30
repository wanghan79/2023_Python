import random

def dataProcess(*args):
    # use data_args variable to store args
    data_args = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            result = {}
            result['origin_data'] = data
            for opt in data_args:
                if opt == 'AVG':
                    s = sum(sum(_) for _ in data)
                    result['AVG'] = s / (len(data) * len(data[0]))
                if opt == 'SUM':
                    s = sum(sum(_) for _ in data)
                    result['SUM'] = s
            return result
        return wrapper
    return decorator

@dataProcess('SUM', 'AVG')
def datasampling(**kwargs):
    result = []
    n = kwargs.get('num', -1)
    if n == -1:
        raise Exception('Missing Parameter num!')
    Item = kwargs.get('struct', None)
    if Item is None:
        raise Exception('Missing Parameter struct!')
    for _ in range(n):
        element = []
        for key, value in Item.items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)

    return result

structure = {
    '1': {'datatype': 'float', 'datarange': [18, 65]},
    '2': {'datatype': 'float', 'datarange': [18, 65]},
}

def run():
    f = datasampling(num=2, struct = structure)
    print(f)
