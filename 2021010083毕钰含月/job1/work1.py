import random
def structDataSampling(**kwargs):
    """

    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key in kwargs['struct']:
            if key['datatype'] == 'int':
                it = iter(key['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key['datatype'] == 'float':
                it = iter(key['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(key['datarange'] )for _ in range(key['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result
def dataSimpling(para):
    print("随机数生成：")
    print(structDataSampling(**para))



def show():
    para = {
        "num": 10,
        "struct": (
            {
                'datatype': "int",
                'datarange': [1, 100]
            },
            {
                'datatype': "int",
                'datarange': [100, 200]
            },
            {
                'datatype': "float",
                'datarange': [1.0, 100.0]
            },
            {
                'datatype': "str",
                'datarange': "ABCDEFGHAAAAABBBB",
                'len': 8
            }
        )
    }
    dataSimpling(para)

if __name__=='__main__':
    show()