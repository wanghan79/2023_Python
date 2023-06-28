import random

import string


def structDataSampling(**kwargs):
    result = list()
    for index in range(kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def Calculation(*decargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            avg = 0
            total = 0
            for row in result:
                for element in row:
                    if isinstance(element, (int, float)):
                        total += element
                        avg += 1
            #print(avg)
            avg = total / avg
            if 'SUM' in decargs:
                print(f"总和为: {total:.3f}")
            if 'AVG' in decargs:
                print(f"均值为: {avg:.3f}")
            return result

        return wrapper

    return decorator

# 定义输入0、1、2个参数情况下且传递相应参数给修饰器的对应函数
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


para = {"num": 5,
        "struct": {
            int: {"datarange": [1, 1000]},
            float: {"datarange": [1.0, 10.0]},
            str: {"datarange": string.ascii_letters, "len": 7}
        }
        }

print("修饰器参数0个，不实现任何操作：")
result_1 = structDataSamplingRes1(**para)
for element in result_1:
    print(element)


print("修饰器参数1个，实现SUM操作：")
result_2 = structDataSamplingRes2(**para)
for element in result_2:
    print(element)


print("修饰器参数1个，实现AVG操作：")
result_3 = structDataSamplingRes3(**para)
for element in result_3:
    print(element)


print("修饰器参数2个，同时实现SUM和AVG操作：")
result_4 = structDataSamplingRes4(**para)
for element in result_4:
    print(element)

