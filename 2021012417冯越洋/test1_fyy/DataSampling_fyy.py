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

if __name__ == '__main__':
    try:
        demo = structDataSampling(num=3, struct={'int_1': {'datatype': 'int', 'datarange': [0, 100]},
                                                 'float_1': {'datatype': 'float', 'datarange': [0, 100]},
                                                 'str_1': {'datatype': 'str', 'datarange': ['a','b','c'],'len':5}})
        print(demo)
    except (TypeError, KeyError):
        print("输入格式错误，请重新输入")
    else:
        print('执行成功')
