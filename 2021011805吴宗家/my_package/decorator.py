import random
import string


def dataProcess(*action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dataLs = func(*args, **kwargs)
            result = {}
            rSum = 0
            L = 0
            for sublist in dataLs:
                for item in sublist:
                    if isinstance(item, (int, float)):
                        rSum += item
                        L += 1
            rAver = rSum / L if L > 0 else 0
            for i in action:
                if i == 'Sum':
                    result['Sum'] = rSum
                if i == 'Aver':
                    result['Aver'] = rAver
            return result
        return wrapper
    return decorator


@dataProcess('Sum', 'Aver')
def structDataSampling(**kwargs):
    result = []
    for index in range(kwargs['num']):
        element = []
        for key, value in kwargs.items():
            if key == 'num':
                continue
            value_type = value.get('type')
            if value_type == 'int':
                datarange = value['datarange']
                element.append(random.randint(datarange[0], datarange[1]))
            elif value_type == 'float':
                datarange = value['datarange']
                element.append(random.uniform(datarange[0], datarange[1]))
            elif value_type == 'str':
                datarange = value.get('datarange', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                n = value.get('len', 8)
                element.append(''.join(random.choice(datarange) for _ in range(n)))
        result.append(element)
    return result
if __name__ == "__main__":
    s = structDataSampling(num=5,
                       int1={'type': 'int', 'datarange': (44, 77)},
                       int2={'type': 'int', 'datarange': (3, 6)},
                       int3={'type': 'int', 'datarange': (7, 100)})
    t = ''
    print(s)
