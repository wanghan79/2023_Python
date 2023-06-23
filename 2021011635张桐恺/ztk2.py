
import random
import logging

def sum(a):
    result = list()
    sum = 0
    for i in range(0,len(a[0])):
        for j in range(0,len(a)):
            sum += a[j][i]
    return sum


def avg(a):
    result=sum(a)
    return result/len(a[0])


def addlogging(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a = list()
            result = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    a.append(sum(result))
                if item == "avg":
                    a.append(avg(result))
            return a
        return wrapper
    return decorator


@addlogging("sum", "avg")
def structDataSampling(struct):
    result = list()
    for i in range(0, struct['num']):
        element = list()
        for key in struct["datatype"]:
            if key == "int":
                it = iter(struct['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(struct['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(struct['datarange'] )for _ in range(struct['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result


def show2():
    print("第一个数为和，第二个数为均值")
    try:
        result = structDataSampling({"num": 50,
                                    "datatype":["float", "float", "float", "int", "float"], "datarange": [0, 50]
                                    })
        print(result)
    except(TypeError,KeyError):
        print("请输入正确的格式")
    else:
        print('成功')

if __name__ == "__main__":
    show2()