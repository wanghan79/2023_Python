import random

def calculate(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list()
            datas = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    result.append('sum='+str(sumx(datas)))
                if item == "avg":
                    result.append('avg='+str(avgx(datas)))
            return result
        return wrapper
    return decorator

@calculate("sum", "avg")

def DataSampling(**kwargs):
    result = []
    for index in range(kwargs['num']):
        element = []
        for key, value in kwargs['struct'].items():
            if value['type'] == 'int':
                a = getint(value['datarange'])
                tmp = a
            elif value['type'] == 'float':
                tmp = getfloat(value['datarange'])
            else:
                break
            element.append(tmp)
        result.append(element)
    print(result)
    return result


def getint(datarange):
    it = iter(datarange)
    return random.randint(next(it), next(it))

def getfloat(datarange):
    it = iter(datarange)
    return random.uniform(next(it), next(it))


def sumx(data):
    result = list()
    sum = 0
    for i in range(0,len(data[0])):
        for j in range(0,len(data)):
            sum += data[j][i]
    return sum

def avgx(data):
    result=sumx(data)
    return result/len(data[0])

x = DataSampling(num=2, struct={'x1':{'type':'int', 'datarange':[0,10]},
                                'x2':{'type':'int', 'datarange':[0,10]},})
print(x)
