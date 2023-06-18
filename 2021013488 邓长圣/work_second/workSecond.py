# 开发者：dengcs
# 开发时间：2023/5/26 18:11
import random


def decorate(*operations):
    def process(func):
        def wrapper(*args, **kwargs):
            result = dict()
            randomNumbers = func(*args, **kwargs)
            result['data'] = randomNumbers
            sumNumbers = sum(sum(_) for _ in randomNumbers)
            for operate in operations:
                if operate == 'AVG':    # 求平均数
                    result[operate] = sumNumbers/(len(randomNumbers) * len(randomNumbers[0]))
                elif operate == 'SUM':
                    result[operate] = sumNumbers
                else:
                    raise Exception('wrong operation')

            return result
        return wrapper
    return process


@decorate('AVG', 'SUM')
def dataSampling(*args, **kwargs):
    result = []
    n = kwargs.get('num', -1)
    if n == -1:
        raise Exception('missing parameter num')
    item = kwargs.get('struct', None)
    if item is None:
        raise Exception('missing parameter struct')
    for _ in range(n):
        element = []
        for data in item:
            if data['datatype'] == 'int':
                it = iter(data['datarange'])
                tmp = random.randint(next(it), next(it))
            elif data['datatype'] == 'float':
                it = iter(data['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif data['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(data['datarange']) for _ in range(data['len']))
            else:
                break

            element.append(tmp)
        result.append(element)

    return result


"""
作业三展示
"""
def show():
    print("作业三：采用修饰器技术对作业1随机数据结构生成函数进行修饰，实现所有生成随机数的求和（SUM），求均值（AVG）操作，以及相应的调用示例。主要考察点是带参数修饰器的使用，具体要求如下：\n" +
            "\t1. 修饰器类型不限，可以是函数修饰器或类修饰器；\n" +
            "\t2. 只能实现一个修饰器，通过修饰器参数（*args）实现SUM和AVG操作的任意组合，即修饰器在接收0、1、2个参数的情况下都可以正常运行；")
    print("示例：生成10组随机数，每组5个int数据，并对生成的随机数求和，求均值")
    print("如下：")
    result = dataSampling(num=10, struct=[{'datatype': 'int', 'datarange': [1, 100]},
                                          {'datatype': 'int', 'datarange': [1, 100]},
                                          {'datatype': 'int', 'datarange': [1, 10]},
                                          {'datatype': 'int', 'datarange': [1, 10]},
                                          {'datatype': 'int', 'datarange': [1, 10]},
                                          ])
    print(result)

if __name__ == "__main__":
    # result = dataSampling(num=10, struct={'one': {'datatype': 'int', 'datarange': [1, 100]},
    #                                       'two': {'datatype': 'int', 'datarange': [1, 100]},
    #                                       'three': {'datatype': 'int', 'datarange': [1, 10]},
    #                                       'four': {'datatype': 'int', 'datarange': [1, 10]},
    #                                       'five': {'datatype': 'int', 'datarange': [1, 10]},
    #                                       'six': {'datatype': 'int', 'datarange': [1, 10]},
    #                                       })


    show()