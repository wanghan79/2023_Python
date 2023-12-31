import random
import string


def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange'] )for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def dataSampling_test1():
    a = structDataSampling(num=3, struct={'data_int': {'datatype': int, 'datarange': [0, 100]},
                                          'data_float': {'datatype': float, 'datarange': [0, 100]},
                                          'data_str': {'datatype': str, 'datarange': string.ascii_uppercase, 'len': 5}})
    for i in a:
        print(i)

if __name__ == '__main__':
    dataSampling_test1()