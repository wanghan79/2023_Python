import random
def get_sum(result):
    sum = 0
    for i in range(0, len(result)):
        for j in range(0, len(result[0])):
            sum += result[i][j]
    return sum

def dataOperation(*parameter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dataProcess = func(*args, **kwargs)
            result = list()
            if 'SUM' in parameter:
                sum = get_sum(dataProcess)
                result.append(sum)
            if 'AVG' in parameter:
                avg = get_sum(dataProcess) / (len(dataProcess) * len(dataProcess[0]))
                result.append(avg)
            return result
        return wrapper
    return decorator

@dataOperation('SUM', 'AVG')
def structDataSampling(*args, **kwargs):
    result = list()
    num = kwargs.get("num", -1)
    struct = kwargs.get("dataStruct")
    for i in range(0, num):
        element = list()
        for key, value in struct.items():
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def wrapper_test():
    test = structDataSampling(num=50, dataStruct={
        '1': {'datatype': float, 'datarange': [1, 100]},
        '2': {'datatype': float, 'datarange': [1, 100]},
        '3': {'datatype': float, 'datarange': [1, 100]},
        '4': {'datatype': float, 'datarange': [1, 100]},
        '5': {'datatype': float, 'datarange': [1, 100]},
        '6': {'datatype': float, 'datarange': [1, 100]},
    })
    print(test)


