import random
import string

def structDataSampling(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if key == "int":
                it = iter(value["datarange"])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(value["datarange"])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

def sum_avg(*decargs):
    def decorator(func):
        def wrapper(*args,**kwargs):
             result=func(*args,**kwargs)
             avg = 0
             sum = 0
             count = 0
             for row in result:
                 for element in row:
                     if isinstance(element,(int,float)):
                         sum=sum+element
                         count=count+1
             avg = sum / count
             if "sum" in decargs:
                print(f"The sum of these numbers is {sum:.3f}")
             if "avg" in decargs:
                print(f"The average of these numbers is {avg:.3f}")
             return result
        return wrapper
    return decorator

@sum_avg('sum')
def structDataSamplingsum(**kwargs):
    return structDataSampling(**kwargs)

@sum_avg('avg')
def structDataSamplingavg(**kwargs):
    return structDataSampling(**kwargs)
para={"num": 3,
      "struct":{"int":{"datarange":(1,30)},
                        "float":{"datarange": (1,10)},
                        "str":{"datarange":" ABCDEFGHIJKLMN", "len":10}}}

print("sum修饰器：" + str(structDataSamplingsum(**para)))
print("avg修饰器：" + str(structDataSamplingavg(**para)))