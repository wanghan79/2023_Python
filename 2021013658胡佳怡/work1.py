
import random
import string


def dataSampling(**kwargs):
    result=list()
    for item in range(kwargs['num']):
        element=list()
        for key,value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it=iter(value['datarange'])
                tmp=random.randint(next(it),next(it))
            elif value['datatype'] == 'float':
                it=iter(value['datarange'])
                tmp=random.uniform(next(it),next(it))
            elif value['datatype'] == 'str':
                tmp=' '.join(random.SystemRandom().choice(value['datarange'])for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

if __name__ == '__main__':
    hw01 = {"num": 5,
            "struct": {
                "data1":
                    {"datatype": 'int',
                     "datarange": {0, 100}},
                "data2":
                    {"datatype": 'int', "datarange": {0, 100}},
                "data3":
                    {"datatype": 'str', "datarange": string.ascii_uppercase, "len": 50}}
            }
    print(dataSampling(**work1))
