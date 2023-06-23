import random
def dataSampling(*args, **kwargs):
    result = []
    for _ in range(kwargs['num']):
        element = []
        for data in kwargs['struct']:
            if data['datatype'] == 'int':
                it = iter(data['datarange'])
                tmp = random.randint(next(it), next(it))
            elif data['datatype'] == 'float':
                it = iter(data['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif data['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(data['datarange']) for _ in range(data['len']))
            else:
                break

            element.append(tmp)
        result.append(element)

    return result

def test():
    result = dataSampling(num=5, struct=[{'datatype':'int', 'datarange':[1, 100]},
                                        {'datatype': 'float', 'datarange':[1, 10]},
                                        {'datatype': 'str', 'datarange': 'caoyiteng', 'len':5}
                                    ])
    print(result)

if __name__ == '__main__':
    result = dataSampling(num=5, struct=[{'datatype':'int', 'datarange':[1, 100]},
                                         {'datatype': 'float', 'datarange':[1, 10]},
                                         {'datatype': 'str', 'datarange': 'caoyiteng', 'len':5}
                                        ])
    print(result)