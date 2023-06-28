"""
@Content: python大作业
           采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作，
           以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：
        1.	修饰器类型不限，可以是函数修饰器或类修饰器；
        2.	只能实现一个修饰器，通过修饰器参数（*args）实现SUM和AVG操作的任意组合，即修饰器在接收0、1、2个参数的情况下都可以正常运行；
"""

import random


def dataprocess(*args):
    data_args = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = dict()
            data= func(*args, **kwargs)
            result['data'] = data
            sumAll= sum(sum(_) for _ in data)
            for opt in data_args:
                if opt == 'AVG':
                    result[opt] = sumAll/(len(data) * len(data[0]))
                elif opt == 'SUM':
                    result[opt] = sumAll
                else:
                    raise Exception('wrong operation')
            return result
        return wrapper
    return decorator


@dataprocess('AVG', 'SUM')
def structDataSampling(**kwargs):
    result = list()
    n = kwargs.get('num', -1)
    if n == -1:
        raise ValueError("Invalid data!")
    Item = kwargs.get('struct', None)
    if Item is None:
        raise Exception('Missing Parameter struct!')
    for item in range(0, n):
        element = list()
        for key, value in Item.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''
                for i in range(0, value['len']):
                    tmp = tmp + random.SystemRandom().choice(value['datarange'])
            else:
                raise ValueError(f"Invalid data type: {key}")
            element.append(tmp)
        result.append(element)
    return result


def show():
    result = structDataSampling(num = 3, struct = {"int":{"datarange":(0,100)},"float":{"datarange":(0,1000)},})
    print(result)

try:
    show()
except Exception:
    pass


