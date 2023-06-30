import random
import string

def structDataSampling(num, struct):
    result = []
    for _ in range(num):
        element = {}
        for key, value in struct.items():
            if key == 'int':
                it = iter(value['range'])
                element[key] = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['range'])
                element[key] = random.uniform(next(it), next(it))
            elif key == 'str':
                element[key] = ''.join(random.SystemRandom().choice(value['chars']) for _ in range(value['length']))
            else:
                break
        result.append(element)
    return result

testDict = {
    "num": 3,
    "struct": {
        'int': {"range": [1, 10]},
        'float': {"range": [1.0, 10.0]},
        'str': {"chars": string.ascii_letters, "length": 10}
    }
}

res = structDataSampling(testDict['num'], testDict['struct'])
print(res)
