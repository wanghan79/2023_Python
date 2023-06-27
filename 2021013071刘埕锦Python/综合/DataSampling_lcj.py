#刘埕锦
import random
def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange'] )for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def show():
    try:
        demo = structDataSampling(num=3, struct={'data1': {'datatype': 'int', 'datarange': [0, 100]},
                                                 'data2': {'datatype': 'int', 'datarange': [0, 100]},
                                                 'data3': {'datatype': 'str', 'datarange': ['a','b','c'],'len':5}})
        print(demo)
    except (TypeError, KeyError):
        print("请输入正确的参数，格式为:num=整数, struct={'data1':{'datatype':'int or float', 'datarange':[0,100]}")
    else:
        print('程序执行成功')

