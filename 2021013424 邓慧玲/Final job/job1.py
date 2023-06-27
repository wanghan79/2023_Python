import random
import string
import json

def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue

        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue

        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result

def structDataSampling(num,struct):
    result = list()
    for index in range(0,num):
        element = list()
        for key,value in struct.items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key is str:
                it = iter(value['datarange'])
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

inputStruct = {
    'num':6,
    'int':{'datarange': (0, 10), 'len': 8},
    'float':{'datarange': (0, 10), 'len': 8},
    'str':{'datarange': '10', 'len': 8}
}

def varystrctDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key,value in kwargs.items():
                if key == "int":
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it),next(it))
                elif key == "float":
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it),next(it))
                elif key == "str":
                    it = iter(value['datarange'])
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                else:
                    continue
                element.append(tmp)
        result.append(element)
    return result
if __name__ == "__main__":
    print(varystrctDataSampling(**inputStruct))