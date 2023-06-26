"""
    Author:Haizhu.Wu
    Title:Assignment1
"""
import random
import string

# 随机数生成

def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for value in kwargs['struct']:
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['length']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

"""
作业一展示
"""
def show():
    kwargs = {
            "num": 5,
            "struct": [
                 {"datatype": int, "datarange": (0, 100)},
                 {"datatype": float, "datarange": (0, 10000)},
                 {"datatype": str, "datarange": string.ascii_uppercase, "length": 5}
            ]
    }
    result = structDataSampling(**kwargs)
    for item in result:
        print(item)

if __name__ == "__main__":
    show()

