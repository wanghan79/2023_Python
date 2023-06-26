import random


def dataSampling(**kwargs):
    result = list()
    num = int(kwargs.get("num", 0))
    len = int(kwargs.get("len", 1))
    if num < 0:
        raise ValueError("num cannot be negative")
    if len <= 0:
        raise ValueError("len cannot be less than 1")
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
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(len))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def show():
    print(f"""案例展示
    {dataSampling(num=50, len=3,
                 int={
                     'datarange': [1, 100]
                 },
                 float={
                     'datarange': [0.1, 10.0]
                 },
                 str={
                     'datarange': ['a', 'b', 'c']
                 }
                 )}
                 """)

