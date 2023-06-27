import logging
import random
import string

def dataProcess(*operate):
    def deCorator(func):
        def wrapper(*args, **kwargs):
            sumary = 0
            j = 0
            result = func(*args, **kwargs)
            print("生成的50组六维数组：",result)
            for arg in operate:
                for x in result:
                    for y in x:
                        sumary = 0
                        j = 0
                        for z in y:
                            sumary = sumary + z
                            j = j + 1
                    if (arg == "sum"):
                        print("和sum = ", sumary)
                    if (arg == "avg"):
                        sumary = sumary / j
                        print("平均值avg = ", sumary / j)
                    if (arg == "sum and avg"):
                        print("和sum = ", sumary, ", 平均值avg = ", sumary / j)
            return result
        return wrapper
    return deCorator

@dataProcess("sum","avg","sum and avg")


def decorateStrctDataSampling(**kwargs):
        result = list()

        for index in range(0,kwargs['float']['num']):
            middle = list()
            for key,value in kwargs.items():
                element = list()
                for t in range(0,6):
                    if key == "int":
                        it = iter(value['datarange'])
                        tmp = random.randint(next(it),next(it))
                    elif key == "float":
                        it = iter(value['datarange'])
                        tmp = random.uniform(next(it),next(it))
                    elif key == "str":
                        it = iter(value['datarange'])
                        tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                    else:
                        continue
                    element.append(tmp)
                middle.append(element)
            result.append(middle)
        return result


decorateInputStruct = {
               'float': {'num':50,'datarange': (0, 10), 'len': 8},
}
if __name__ == "__main__":
    decorateStrctDataSampling(**decorateInputStruct)