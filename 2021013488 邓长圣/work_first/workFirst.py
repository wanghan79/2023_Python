# 开发者：dengcs
# 开发时间：2023/6/17 22:28

import random


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
作业一展示
"""
def show():
    print("实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：\n" +
            "1. 采用关键字参数作为随机数据结构及数量的输入；\n" +
            "2. 在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；\n" +
            "3. 其中随机数涵盖int，float和str三种类型。")
    print("示例：生成5组随机数，每组随机数含有2个int型数据，1个float型数据和一个字符串")
    print("如下：")
    result = dataSampling(num=5, struct=[{'datatype': 'int', 'datarange': [1, 100]},
                                          {'datatype': 'int', 'datarange': [1, 100]},
                                          {'datatype': 'float', 'datarange': [1, 10]},
                                          {'datatype': 'str', 'datarange': "china", 'len': 5},
                                          ])
    print(result)


if __name__ == "__main__":
    show()