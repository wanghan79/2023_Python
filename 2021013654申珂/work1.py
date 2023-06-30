import random
import string

def structData(**kwargs):
    result = list()
    for index in range(0, kwargs['num']):
        element = list()
        for e, value in kwargs.items():
            if e == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def showRandom():
    para = {"num": 10, "int": {"datarange": [1,100]}, "float": {"datarange": [1,100]}, "str": {"datarange": string.ascii_uppercase, "len": 8}}
    a = structData(**para)
    for i in a:
        print(i)
showRandom()