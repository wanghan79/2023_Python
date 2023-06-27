import random
import string

def dataSamplingDecorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        sums = 0
        count = 0
        for row in data:
            for element in row:
                if isinstance(element, (int, float)):
                    sums += element
                    count += 1
        avg = sums / count if count > 0 else 0
        return sums, avg
    return wrapper

@dataSamplingDecorator
def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs["num"]):
        element = []
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

# 定义数据结构
struct = {
    'name': {'datatype': 'str', 'datarange': string.ascii_letters, 'len': 5},
    'age': {'datatype': 'int', 'datarange': (18, 30)},
    'height': {'datatype': 'float', 'datarange': (160.0, 180.0)}
}

# 调用修饰后的函数并输出结果
result = structDataSampling(num=5, struct=struct)
print("Sum:", result[0])
print("Avg:", result[1])