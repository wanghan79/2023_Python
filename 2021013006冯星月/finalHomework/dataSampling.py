import random
import string

def structDataSampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key,value in kwargs['struct'].items():
            # print(value['len'])
            if value['datatype'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif value['datatype'] == float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
class hw01:
    def __init__(self):
        self.name = 'dataSampling'
    def show(self,a,b):
        print(structDataSampling(num=a,struct=b))
