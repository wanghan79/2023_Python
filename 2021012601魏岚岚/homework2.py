import logging
import random
import string

def dataProcess(*args):  # 求和和求均值的组合
    def decorator(func):  # 被修饰的函数func
        def wrapper(*args, **kwargs):  # 万能参数*args **kwargs实现对任何函数任意参数类型的适配
            data = func(*args, **kwargs)  # 获取dataSampling生成的随机数，解析*args的新功能
            total = sum(data)
            avg = total / len(data)
            if not kwargs.get('average'):
                return total
            else:
                return avg
        return wrapper
    return decorator


@dataProcess()
def dataSampling(datatype, datarange, num, strlen=8):
    result: set[int | float | str] = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result


print(dataSampling(int, (1, 100), 60))
