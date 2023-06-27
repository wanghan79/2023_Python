import random
import string

def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs["num"]):
        element = {}
        for key, value in kwargs['struct'].items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element[key] = tmp
        result.append(element)
    return result

# 定义数据结构
struct = {
    'int': {'datatype': str, 'datarange': string.ascii_letters, 'len': 5},
    'float': {'datatype': int, 'datarange': (18, 30)},
    'str': {'datatype': float, 'datarange': (160.0, 180.0)}
}

# 调用函数生成数据
data = structDataSampling(num=5, struct=struct)
print(data)

