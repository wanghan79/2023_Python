"""
@Content: python大作业
            实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
    1.	采用关键字参数作为随机数据结构及数量的输入；
    2.	在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
    3.	其中随机数涵盖int，float和str三种类型。
"""
import random

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
    randomResult = structDataSampling(num = 3, struct = {"int":{"datarange":(0,100)},"float":{"datarange":(0,1000)},"str":{"datarange":"ASWEDEFFY!@#$%^&*&^%$#RHRFHNJFDYKHBJFKGVDLKJU","len":8}})
    for item in randomResult:
        print(item)


try:
    show()
except Exception:
    pass

