import time
import random
import string

struct2={"num":50,"datastruct":(
    {
        "datatype": float,
        "datarange": (1, 5)
    },
    {
        "datatype":float,
        "datarange":(1,5)
    },
    {
        "datatype":float,
        "datarange":(1,5)
    },{
        "datatype":float,
        "datarange":(1,5)
    },{
        "datatype":float,
        "datarange":(1,5)
    },{
        "datatype":float,
        "datarange":(1,5)
    },
)}
def printData5(*args1):
    def decorator(func):
        def wrapper(*args,**kwargs):
            data = func(*args,**kwargs)
            sum=[]
            for i in range(len(kwargs['datastruct'])):
                sum.append(0)
            for j in range(kwargs['num']):
                for i in range(len(kwargs['datastruct'])):
                    sum[i] = sum[i] + data[j][i]
            if(args1[0]=='sum'):
                pass
            elif(args1[0]=='avg'):
                for i in range(len(kwargs['datastruct'])):
                    sum[i]=sum[i]/kwargs['num']

            return sum
        return wrapper
    return decorator
@printData5('sum')
def structDataSampling_sum(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    result=list()
    for index in range(0, kwargs['num']):
        element = list()
        for e in kwargs['datastruct']:
            if e['datatype'] is int:
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] is float:
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] is str:
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e["len"]))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
@printData5('avg')
def structDataSampling_avg(**kwargs):
    """
    :param num:
    :param struct:
    :return:
    """
    result=list()
    for index in range(0, kwargs['num']):
        element = list()
        for e in kwargs['datastruct']:
            if e['datatype'] is int:
                it = iter(e['datarange'])
                tmp = random.randint(next(it), next(it))
            elif e['datatype'] is float:
                it = iter(e['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif e['datatype'] is str:
                tmp = ''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e["len"]))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def PrintstructDataSampling():
    print(f'生成50组有6个随机float数据组成的list，随机数范围1-5')
    print(f'随机数求和：{structDataSampling_sum(**struct2)}')
    print(f'随机数求平均：{structDataSampling_avg(**struct2)}')
    print('')
if __name__ == '__main__':
    PrintstructDataSampling()