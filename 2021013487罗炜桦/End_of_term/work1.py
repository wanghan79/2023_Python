import random
import string


def structDataSamplingTwo(**kwargs):
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


testDict = {"num": 5,
            "struct": {
                int: {"datarange": [1, 1000]},
                float: {"datarange": [1.0, 10.0]},
                str: {"datarange": string.ascii_letters, "len": 7}
            }
            }
res = structDataSamplingTwo(**testDict)
def work1():
#使用循环遍历res列表打印每一个数据元素
    for element in res:
        print(element)
work1()


