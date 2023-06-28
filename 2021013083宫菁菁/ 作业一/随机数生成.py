import random
import string
def structDataSampling(**kwargs):
    result = list()
    for index in range(0,10):
        element = list()
        for key,value in kwargs.items():
            if key == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif key == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it),next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

a = {"int":{"datarange":(0,100)}}
b = {"float":{"datarange":(0,10000)}}
c = {"str":{"datarange":string.ascii_letters,"len":5}}
d = structDataSampling(**a)
e = structDataSampling(**b)
f = structDataSampling(**c)
print("int型")
print(d)
print("float型")
print(e)
print("str型")
print(f)