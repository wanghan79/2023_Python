
"""

一.
    50个六维数的向量
    修饰器求和或者求均值
    在datasampling 进行修饰
    要求能够用带参数的修饰器，通过一个修饰器
    或者两种都求，或者求其中一种
二.
    三次作业集成
    让在控制台可以通过询问哪次作业而输出相应的result

"""
import random
import string


def dateProcess(*operation):
    def dataconfig(structDataSampling):
        def wrapper(*args,**kwargs):
            dater = structDataSampling(*args,**kwargs)
            result = dict()
            result['data'] = dater
            s=sum(sum(_) for _ in dater)
            if 'ave' in operation:
                result['ave'] = s/(len(dater)*len(dater[0]))
            if 'sum' in operation:
                result['sum'] = s
            return result
        return wrapper
    return dataconfig


@dateProcess('sum','ave')
def structDataSampling(**kwargs):
    result = list()
    for item in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value["datarange"]) for _ in range(value["len"]))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


if __name__ == "__main__":
    result = structDataSampling(num=50, struct={'one':{'datatype':'int',"datarange": (0,100)}, 'two': {'datatype': 'float', 'datarange': [1, 100]}})
    # for item in result:
        # print(item)
    print(result)