import random
import string

def structDataSampling(**kwargs):
    result = list()
    num = kwargs.get("num", -1)
    struct = kwargs.get("dataStruct")
    for i in range(0, num):
        element = list()
        for key, value in struct.items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def dataSampling_test():
    test = structDataSampling(num=3, dataStruct={
        '1': {'datatype': int, 'datarange': [1, 100]},
        '2': {'datatype': float, 'datarange': [1, 1000]},
        '3': {'datatype': str, 'datarange': 'abcde', 'len': 10}
    })
    print(test)

if __name__ == '__main__':
    dataSampling_test()


