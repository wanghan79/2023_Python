
import random

def structDataSampling(**kwargs):
    """
       :param num:
       :param struct:
       :return:
    """
    result = []
    for index in range(0, kwargs['num']):
        element = []
        for key, value in kwargs['struct'].items():
            if value['datatype'] == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


def structDataSamplinga(**kwargs):
    """
       :param num:
       :param struct:
       :return:
    """
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break;
            element.append(tmp)
        result.append(element)
    return result


def out_1():
    para = {"num": 4, "struct": {"int": {"datarange": (0, 100)},
                                 "float": {"datarange": (0, 1000)}}}
    t = structDataSamplinga(**para)
    print(t)
    parb = {"num": 4, "struct": {"int": {"datarange": (0, 90)}, "str": {"datarange": "ABCD", "len": 2},
                                 "float": {"datarange": (0, 100)}}}
    m = structDataSamplinga(**parb)
    print(m)

    parc = {"num": 3, "struct": {
        "field1": {"datatype": 'int', "datarange": [100, 140]},
        "field2": {"datatype": 'float', "datarange": [100, 150]},
        "field3": {"datatype": 'str', "datarange": "ABCDEFG", "len": 3}
    }}
    n = structDataSampling(**parc)
    print(n)

if __name__ == '__main__':
    out_1()
