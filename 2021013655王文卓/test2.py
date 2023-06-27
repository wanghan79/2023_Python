import random
import logging


def sum(data):
    result = list()
    sum = 0
    for i in range(0, len(data[0])):
        for j in range(0, len(data)):
            sum += data[j][i]
    return sum


def avg(data):
    result = sum(data)
    return result / len(data[0])


def sum_or_avg(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list()
            datas = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    result.append('sum=' + str(sum(datas)))
                if item == "avg":
                    result.append('avg=' + str(avg(datas)))
            return result

        return wrapper

    return decorator


@sum_or_avg("sum", "avg")
def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
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
                break
            element.append(tmp)
        result.append(element)
    print("生成的随机数为:")
    print(result)
    return result

if __name__ == '__main__':
    try:
        demo = structDataSampling(num=3, struct={'data1': {'datatype': 'float', 'datarange': [0, 100]},
                                                 'data2': {'datatype': 'int', 'datarange': [0, 100]}})
        print(demo)
    except (TypeError, KeyError):
        print("请输入正确的参数，格式为:num=整数, struct={'data1':{'datatype':'int or float', 'datarange':[0,100]}")
        print('不能有字符类型')
    else:
        print('修饰器实现成功')
