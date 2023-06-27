import random
def dataProcess(*arg):
    def decorator(func):
        def wrapper(**kwargs):
            data = func(**kwargs)
            result = dict()
            result["data"] = data
            s = [0, 0, 0, 0, 0]
            for item in data:
                for i in range(5):
                    s[i] = s[i]+item[i]
            for a in arg:
                if a == "sum":
                    result["sum"] = s
                elif a == "avg":
                    avg = [0, 0, 0, 0, 0]
                    for i in range(5):
                        avg[i] = s[i]/len(data)
                    result["avg"] = avg
            return result
        return wrapper
    return decorator
@dataProcess()
def structDataSampling(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                t = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                t = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                t = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(t)
        result.append(element)
    return result
@dataProcess("sum")
def structDataSampling_sum(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                t = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                t = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                t = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(t)
        result.append(element)
    return result
@dataProcess("avg")
def structDataSampling_avg(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
@dataProcess("sum","avg")
def structDataSampling_sum_avg(**kwargs):
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for e in kwargs['struct']:
            if e['datatype'] == "int":
                it = iter(e['datarange'])
                t = random.randint(next(it), next(it))
            elif e['datatype'] == "float":
                it = iter(e['datarange'])
                t = random.uniform(next(it), next(it))
            elif e['datatype'] == "str":
                t = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e['len']))
            else:
                break
            element.append(t)
        result.append(element)
    return result
def decorator(para):
    print("生成的随机数")
    print(structDataSampling(**para))
    print("求和")
    print(structDataSampling_sum(**para))
    print("平均数")
    print(structDataSampling_avg(**para))
    print("求和求平均数")
    print(structDataSampling_sum_avg(**para))
if __name__=='__main__':
    para = {
        "num": 5,
        "struct": (
            {
                'datatype': "int",
                'datarange': [1, 10]
            },
            {
                'datatype': "int",
                'datarange': [1, 10]
            },
            {
                'datatype': "int",
                'datarange': [1, 10]
            },
            {
                'datatype': "int",
                'datarange': [1, 10]
            },
            {
                'datatype': "int",
                'datarange': [1, 10]
            }
        )
    }
    decorator(para)