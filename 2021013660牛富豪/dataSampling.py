import random
import string

def dataSampling(**kwargs):
    '''
    :param kwargs
    :return
    '''
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.sample(range(0, 100), value))
        elif key == 'float':
            result.append([round(random.uniform(0, 100), 2) for _ in range(value)])
        elif key == 'str':
            result.append([''.join(random.sample(string.ascii_letters + string.digits, 6)) for _ in range(value)])
    return result
result = dataSampling(int=5, float=3, str=4)
print(result)