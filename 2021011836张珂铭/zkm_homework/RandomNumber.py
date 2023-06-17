import random
import string
struct1={"num":50,"datastruct":(
    {
        "datatype":int,
        "datarange":(1,5)
    },
    {
        "datatype":float,
        "datarange":(1,5)
    },
    {
        "datatype":str,
        "datarange":('a','b','c','d'),
        "len":4
    },
)}
def structDataSampling2(**kwargs):
    """
    :param num:
    :param kwargs:
    :return:
    """
    result = list()
    # for index in range(0,num):
    for index in range(0,kwargs['num']):
        element = list()
        for e in kwargs['datastruct']:
            if e['datatype'] is int:
                it=iter(e['datarange'])
                tmp=random.randint(next(it),next(it))
            elif e['datatype'] is float:
                it=iter(e['datarange'])
                tmp=random.uniform(next(it),next(it))
            elif e['datatype'] is str:
                tmp=''.join(random.SystemRandom().choice(e['datarange']) for _ in range(e["len"]))
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def PrintNumber():
    print(f'生成随机数据结构：')
    print(structDataSampling2(**struct1))
    print('')
if __name__ == '__main__':
    PrintNumber()

# print(structDataSampling2(num=2,datastruct=({"datatype":int,"datarange":(1,5)},{"datatype":float,"datarange":(1,5)},{"datatype":str,"datarange":('a','b','c','dd'),"len":4})))