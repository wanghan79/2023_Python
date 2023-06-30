import random
import string


def DataSamoling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
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
                break
            element.append(tmp)
        result.append(element)
    return result


if __name__ == '__main__':
    eg = {"num": 3,
                "struct": {
                    int: {"datarange": [0, 100]},
                    float: {"datarange": [0, 100]},
                    str: {"datarange": string.ascii_letters, "len": 10}
                }
                }
    print(DataSampling(**eg))
