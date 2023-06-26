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


def SUM(temp):
    sum = 0
    for i, element in enumerate(temp):
        tmp = 0
        for num in iter(element):
            tmp = tmp + num
        sum = sum + tmp
    return sum

def AVG(temp):
    total_sum = SUM(temp)
    length = sum(len(x) for x in temp)
    return total_sum / length


def sum_or_avg(*choice):
    def decorator(function):
        def wrapper(*args, **kwargs):
            res = dict()
            temp = function(*args, **kwargs)
            for choose in choice:
                if choose == "AVG":
                    res['AVG'] = AVG(temp)
                elif choose == "SUM":
                    res['SUM'] = SUM(temp)
                else:
                    continue
            return temp, res
        return wrapper
    return decorator


@sum_or_avg("AVG", 'SUM')
def show(Num):
    return dataSampling(num = Num,
                     int =  {'datarange': (0, 100)},
                    float =  {"datarange": (0, 1.0)})


def show():
    while 1:
        try:
            data = dataSampling(num=50, len=3,
                    int={
                        'datarange': [1, 100]
                    },
                    float={
                        'datarange': [0.1, 10.0]
                    },
                    str={
                        'datarange': ['a', 'b', 'c']
                    }
                    )
            print(f"""
                  函数展示如下：
                  {data}""")
        except (TypeError,KeyError):
            print("请输入正确的参数类型")
        else:
            break\
            

show()