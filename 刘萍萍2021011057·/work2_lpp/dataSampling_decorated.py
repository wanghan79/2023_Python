import random
from functools import wraps


def dataSampling(*types, num=1, length=10, start=0, end=100, repeat=False):
    result = []
    for i in range(num):
        if 'int' in types:
            result.append(random.randint(start, end))
        if 'float' in types:
            result.append(random.uniform(start, end))
        if 'str' in types:
            result.append(''.join(random.sample("abcdefghijklmnopqrstuvwxyz", length)))
    if not repeat:
        result = list(set(result))
    return result


def sum_avg(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if 'SUM' in args:
            return sum(result)
        if 'AVG' in args:
            return sum(result) / len(result)
        return result

    return wrapper


@sum_avg
def dataSampling_decorated(*types, num=1, length=10, start=0, end=100, repeat=False):
    return dataSampling(*types, num=num, length=length, start=start, end=end, repeat=repeat)


# 调用示例
print(dataSampling_decorated('int', num=5))
print(dataSampling_decorated('float', num=5))
print(dataSampling_decorated('str', num=5))
print(dataSampling_decorated('int', 'float', num=5))
print(dataSampling_decorated('int', 'float', 'str', num=5))
