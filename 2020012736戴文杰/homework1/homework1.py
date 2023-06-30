import random
import string

def structDataSampling(**keyargs):
    result = list()
    num = keyargs.get("num", -1)
    struct = keyargs.get("dataStruct")
    if num == -1:
        raise KeyError("error in num")
    for index in range(0, num):
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
                break
            element.append(tmp)
        result.append(element)
    return result


def dataSampling_test():
    result = structDataSampling(num=5, dataStruct={
        '1': {'datatype': int, 'datarange': [1, 100]},
        '2': {'datatype': float, 'datarange': [1, 100]},
        '3': {'datatype': str, 'datarange': 'abcde', 'len': 10}
    })
    print(result)


if __name__ == '__main__':
    dataSampling_test()
