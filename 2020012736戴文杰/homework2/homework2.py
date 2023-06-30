
import random


def get_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = sum + matrix[i][j]
    return sum

#print(get_sum(matrix))

def get_mean(matrix):
    sum = 0
    num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum = sum + matrix[i][j]
            num = num +1
    return sum/num

def dataprocess(*para):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            finl_result = list()
            if "SUM" in para:
                finl_result.append('SUM = ' + str(get_sum(result)))
            if "AVG" in para:
                finl_result.append('AVG = ' + str(get_mean(result)))
            return finl_result
        return wrapper
    return decorator

@dataprocess('SUM', 'AVG')
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

def struct_test():
    test = structDataSampling(num=50, dataStruct={
        '1': {'datatype': float, 'datarange': [1, 100]},
        '2': {'datatype': float, 'datarange': [1, 100]},
        '3': {'datatype': float, 'datarange': [1, 100]},
        '4': {'datatype': float, 'datarange': [1, 100]},
        '5': {'datatype': float, 'datarange': [1, 100]},
        '6': {'datatype': float, 'datarange': [1, 100]},
    })
    print(test)

if __name__ == '__main__':
    struct_test()