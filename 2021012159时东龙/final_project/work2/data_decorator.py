from work1 import dataSampling

def struct_sum(result):
    sum = 0
    for i in range(0,len(result[0])):
        for j in range(0,len(result)):
            sum += result[j][i]
    return sum

def dataDecorator(*modes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            a=list()
            result = func(*args, **kwargs)
            for item in modes:
                if item == "sum":
                    a.append(struct_sum(result))
                if item == "avg":
                    a.append(struct_sum(result)/len(result)/len(result[0]))
            return a,result
        return wrapper
    return decorator

@dataDecorator("sum", "avg")
def data_decorator(**kwargs):
    result=dataSampling.structDataSampling(**kwargs)
    return result

def data_decorator_test1():
    a ,x= data_decorator(num=10, struct={'a': {'datatype': int, 'datarange': [1, 100]},
                                       'b': {'datatype': float, 'datarange': [1, 100]}})
    print(a)
    #print(x)

if __name__ == '__main__':
    data_decorator_test1()