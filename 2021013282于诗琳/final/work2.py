import random
import logging

def sum(a):
    result = list()
    for i in range(0,5):
        sum = 0;
        for j in range(0,49):
            sum += a[j][i]
        result.append(sum)
    return result

def avg(a):
    result = sum(a)
    for i in range (0,5):
        result[i] = result[i]/50
    return result

def addlogging(*order):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            sum_result = sum(result)
            avg_result = avg(result)
            output = {'result': result, 'sum': sum_result, 'avg': avg_result}
            for item in order:
                if item == "sum":
                    output['sum'] = sum_result
                if item == "avg":
                    output['avg'] = avg_result
            return output
        return wrapper
    return decorator

@addlogging("sum", "avg")
def structDataSamping(num,struct):
    result = []
    for i in range(50):
        element = []
        for j in range(5):
            it = iter(struct['datarange'])
            tmp = random.uniform(next(it),next(it))
            element.append(tmp)
        result.append(element)
    return result

def SJwork_2():
    struct = {"datarange": (0, 50)}
    data = structDataSamping(3,struct)
    print("生成的随机数为:")
    print(data['result'])
    print("随机数求和为")
    print(data['sum'])
    print("随机数求平均数为")
    print(data['avg'])
