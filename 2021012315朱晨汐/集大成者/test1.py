import random
import string



def structDataSampling(**kwargs):
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


testDict = {"num": 4,
            "struct": {
                int: {"datarange": [1, 10]},
                float: {"datarange": [1.0, 10.0]},
                str: {"datarange": string.ascii_letters, "len": 10}
            }
            }

if __name__ == '__main__':
    print(structDataSampling(**testDict))
