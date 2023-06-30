import random

def kwargsDataSapling(**kwargs):
    # **kwargs 是关键字参数
    result = list()
    for _ in range(kwargs["n"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if value[0] == int:
                it = iter(value[1]['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value[0] == float:
                it = iter(value[1]['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value[0] == str:
                tmp = ''.join(random.SystemRandom().choice(value[1]['datarange']) for _ in range(value[1]['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


s = {'dataType1': [int, {'datarange': (0, 100)}], 'dataType2': [float, {'datarange': (0, 100)}], 'dataType3': [str, {'datarange': ('z', 'y', 'c'), 'len': 3}]}
result = kwargsDataSapling(n=5, struct=s)
print(result)
