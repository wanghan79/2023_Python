import random


def structDataSampling(**kwargs):
    global tmp
    result = list()
    num = kwargs.get("num", -1)
    if num == -1:
        raise Exception("Wrong number input")
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result


def example():
    result = structDataSampling(num=3,
                                int={"datarange": [1, 100]},
                                float={"datarange": [1.0, 100.0]},
                                str={"datarange": ['a', 'b', 'c', 'd', 'e'], "len": 3}
                                )
    for i in result:
        print(i)


