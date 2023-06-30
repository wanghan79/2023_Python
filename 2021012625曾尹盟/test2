import random
import string

def structDataSampling(**kwargs):
    result = []
    for _ in range(kwargs['num']):
        element = {}
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = round(random.uniform(next(it), next(it)), value['precision'])
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element[key.__name__] = tmp
        result.append(element)
    return result

def Calculation(*decargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            mean = 0
            total = 0
            count = 0
            for row in result:
                for element in row.values():
                    if isinstance(element, (int, float)):
                        total += element
                        count += 1
            if count > 0:
                mean = total / count
            if 'SUM' in decargs:
                print(f"The sum of the numbers is {total:.3f}")
            if 'AVG' in decargs:
                print(f"The mean of the numbers is {mean:.3f}")
            return result

        return wrapper

    return decorator

@Calculation()
def structDataSamplingRes1(**kwargs):
    return structDataSampling(**kwargs)

@Calculation('SUM')
def structDataSamplingRes2(**kwargs):
    return structDataSampling(**kwargs)

@Calculation('AVG')
def structDataSamplingRes3(**kwargs):
    return structDataSampling(**kwargs)

@Calculation('SUM', 'AVG')
def structDataSamplingRes4(**kwargs):
    return structDataSampling(**kwargs)

para = {
    "num": 3,
    "struct": {
        int: {"datarange": [1, 10]},
        float: {"datarange": [1.0, 10.0], "precision": 2},
        str: {"datarange": string.ascii_letters, "len": 10}
    }
}

print("修饰器参数0个，不实现任何操作：")
result1 = structDataSamplingRes1(**para)
print(result1)

print("修饰器参数1个，实现SUM操作：")
result2 = structDataSamplingRes2(**para)
print(result2)

print("修饰器参数1个，实现AVG操作：")
result3 = structDataSamplingRes3(**para)
print(result3)

print("修饰器参数2个，同时实现SUM和AVG操作：")
result4 = structDataSamplingRes4(**para)
print(result4)
