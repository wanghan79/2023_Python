#wy
import random
def structDataSampling_3(**kwargs):
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange'] )for _ in range(value['len']))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result

pra= {"num":10, 'struct': {'data1':{'datatype':'int', 'datarange':[0,100]}, 'data2':{'datatype':'int', 'datarange':[0,100]}, 'data3':{'datatype':'float', 'datarange':[0,100]}}}
a = structDataSampling_3(num=3,struct={'data1':{'datatype':'int', 'datarange':[0,100]}, 'data2':{'datatype':'int', 'datarange':[0,100]}, 'data3':{'datatype':'str', 'datarange':['a','c','f','d'],'len':5}})
print(a)
