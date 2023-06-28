import logging
import random
import string

def dataProcess(*args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            out = sum(data)
            avg = out/len(data)
            if kwargs.get('average'):
                return avg
            else:
                return out
        return wrapper
    return decorator
@dataProcess()
def DataSampling(datatype, datarange, num, strlen=8):
    result = set()
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
def Random():
    print(DataSampling(int,(1,100),60))
if __name__ == '__main__':
    Random()