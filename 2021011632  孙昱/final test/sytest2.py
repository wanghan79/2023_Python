import random
import logging

logging.basicConfig(level=logging.INFO)

def sum_data(data):
    result = list()
    sum = 0
    for i in range(0,len(data[0])):
        for j in range(0,len(data)):
            sum += data[j][i]
    return sum

def avg(data):
    result=sum_data(data)
    return result/len(data[0])

def sum_or_avg(*oder):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = list()
            datas = func(*args, **kwargs)
            for item in oder:
                if item == "sum":
                    result.append('sum='+str(sum_data(datas)))
                if item == "avg":
                    result.append('avg='+str(avg(datas)))
            return result
        return wrapper
    return decorator

@sum_or_avg("sum", "avg")
def structDataSampling(**kwargs):
    result = list()
    for index in range(0, kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

def show():
    print(structDataSampling(num=3, struct={'data1':{'datatype':'int', 'datarange':[0,100]}, 'data2':{'datatype':'int', 'datarange':[0,100]}}))

if __name__ == '__main__':
    try:
        demo = structDataSampling(num=3, struct={'data1':{'datatype':'int', 'datarange':[0,100]}, 'data2':{'datatype':'int', 'datarange':[0,100]}})
        print(demo)
    except TypeError as e:
        logging.error(f"参数错误：{e}")
    except KeyError as e:
        logging.error(f"参数错误：{e}")
    except Exception as e:
        logging.error(f"程序异常：{e}")
    else:
        print('成功!')