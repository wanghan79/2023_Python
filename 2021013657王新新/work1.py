import random
def structDataSampling(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                t = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                t = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                t = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(t)
        result.append(element)
    return result
def dataSampling(para):
    print("随机数为：")
    print(structDataSampling(**para))
if __name__=='__main__':
    para = {
        "num": 5,
        "struct": (
            {
                'datatype': "int",
                'datarange': [1, 10]
            },
            {
                'datatype': "float",
                'datarange': [1.0, 10.0]
            },
            {
                'datatype': "str",
                'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                'len': 5
            }
        )
    }
    dataSampling(para)