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


if __name__ == '__main__':
    zcx = structDataSampling(num = 4, struct= {"int_type": {"datatype": int, "datarange": [0, 100]},
                                 "float_type": {"datatype": float, "datarange": [0, 100]},
                                 "str_type": {"datatype": str, "datarange": "abcde", "len": 20}
            })
    print(zcx)