import random
import string

def DataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def showRandom():
    struct = {"num": 3, "int": {"datarange": [1, 100]}, "float": {"datarange": [1, 100]},
              "str": {"datarange": string.ascii_uppercase, "len": 5}}
    a = DataSampling(**struct)
    for i in a:
        print(i)
showRandom()
