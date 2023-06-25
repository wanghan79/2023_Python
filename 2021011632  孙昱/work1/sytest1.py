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

if __name__ == '__main__':
    try:
        demo = structDataSampling(num=3, struct={
            'data1': {'datatype': 'int', 'datarange': [0, 100]},
            'data2': {'datatype': 'int', 'datarange': [0, 100]},
            'data3': {'datatype': 'str', 'datarange': ['a', 'b', 'c'], 'len': 5}
        })
        print(demo)
    except (TypeError, KeyError):
        print("输入正确的参数，格式为:num=整数, struct={'data1':{'datatype':'int or float', 'datarange':[0,100]}")
