# 修饰随机数生成函数，生成50个六维向量，用修饰器求和或求均值，功能由修饰器的参数决定。
import random

def calulate(*calulateTpye):# 传入 “avg” or “sum” 决定修饰器的功能
    def decorator(funcs):
        def wrapper(*args, **kwargs):
            data = funcs(*args, **kwargs)
            sum = 0
            num = 0
            for i in data:
                for j in i:
                    sum += j
                    num += 1
            if calulateTpye[0] == "avg" and calulateTpye[1] == "sum":
                result = [sum/num, sum]
            elif calulateTpye[0] == "sum":
                result = sum
            elif calulateTpye[0] == "avg":
                result = sum / num
            else:
                result = 0
            return result
        return wrapper
    return decorator

@calulate("avg", "sum")
def kwargsDataSapling(**kwargs):
    # **kwargs 是关键字参数
    result = list()
    for _ in range(kwargs["num"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if value[0] == int:
                it = iter(value[1]['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value[0] == float:
                it = iter(value[1]['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value[0] == str:
                tmp = ''.join(random.SystemRandom().choice(value[1]['datarange']) for _ in range(value[1]['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

s = {'dataType1':[float, {'datarange':(0,100)}], 'dataType2':[float, {'datarange':(0,100)}], 'dataType3':[float, {'datarange':(0,100)}], 'dataType4':[float, {'datarange':(0,100)}], 'dataType5':[float, {'datarange':(0,100)}], 'dataType6':[float, {'datarange':(0,100)}]}
result = kwargsDataSapling(num=50, struct=s)
print(result)
