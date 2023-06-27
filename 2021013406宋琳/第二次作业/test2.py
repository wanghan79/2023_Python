#songlin_test2_求随机数的和和平均值

import random
import string

def sum(s):
    result = list()
    sum = 0
    for i in range(0,len(s[0])):
        for j in range(0,len(s)):
            sum  += s[j][i]
        return sum

def avg(s):
    result = sum(s)
    t = len(s[0])
    return result/t

def caculation(*order):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            data = func(*args, **kwargs)
            print("生成的随机数为：\n"+str(data))
            for i in order:
                if i == "sum":
                    a.append('随机数的和为：'+str(sum(data)))
                if i == "avg":
                    a.append('随机数的平均值为：'+str(avg(data)))
            return a
        return wrapper
    return decorator

@caculation("sum","avg")
def DataSampling(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key in kwargs.get("struct"):
            if key["datatype"] == "int":
                it = iter(key["datarange"])
                tmp = random.randint(next(it),next(it))
            elif key["datatype"] == "float":
                it = iter(key["datarange"])
                tmp = random.uniform(next(it), next(it))
            elif key["datatype"] =="str":
                tmp = ''.join(random.SystemRandom().choice(key["datarange"]) for _ in range(key["len"]))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

def result_2():
    s = DataSampling(
            num=5,
            struct=(
                {
                    'datatype': "int",
                    'datarange': (0, 100)
                },
                {
                    'datatype': "float",
                    'datarange': (0, 100)
                },
                {
                    'datatype': "int",
                    'datarange': (0, 20)
                }
            )
        )
    print(s)

if __name__ == '__main__':
    result_2()
