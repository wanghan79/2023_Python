import random
import string


def dataSampling(datatype, datarange, num, strlen=8):
    result = set()
    for index in range(0, num):
        if datatype is int:
            it = iter(datarange)
            item = random.randint(next(it), next(it))
            result.add(item)
            continue
        elif datatype is float:
            it = iter(datarange)
            item = random.uniform(next(it), next(it))
            result.add(item)
            continue
        elif datatype is str:
            item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
            result.add(item)
            continue
        else:
            continue
    return result



#=====================================================================================================
def structDataSampling1(num, struct):
    result = list()
    for index in range(0,num):
        element = list()
        for key, value in struct.items():
            if key is int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key is float:
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key is str:
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result



#=====================================================================================================================

def structDataSampling2(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            if key == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result




#==============================================================================================================

def structDataSampling3(**kwargs):
    result = list()
    for index in range(kwargs.get("num")):
        element = list()
        for c in kwargs.get("struct"):
            if c["dataType"] == "int":
                for i in range(c['num']):
                    it = iter(c["dataRange"])
                    tmp = random.randint(next(it), next(it))
                    element.append(tmp)
            elif c["dataType"] == "float":
                for i in range(c['num']):
                    it = iter(c["dataRange"])
                    tmp = random.uniform(next(it), next(it))
                    element.append(tmp)
            elif c["dataType"] == "str":
                for i in range(c['num']):
                    tmp = ''.join(random.SystemRandom().choice(c["dataRange"]) for _ in range(c["len"]))
                    element.append(tmp)
            else:
                break
        result.append(element)
    return result

def show():
    print(dataSampling(int, (0, 2), 10))

    print(structDataSampling1(10, {
        int: {
            'datarange': (0, 10)
        },
        float: {
            'datarange': (0.5, 1.5)
        },
        str: {
            'datarange': ("wake", "hello", "world", "a", "s", "m"),
            'len': 8
        }
    }))

    print(structDataSampling2(10,
          int={
              'datarange': (0, 10)
          },
          float={
              'datarange': (2.4, 10.6)
          },
          str={
              'datarange': ('a', 'c', 'm', 'wake', 'hello'),
              'len': 6
          }
    ))

    print(structDataSampling3(num=10, struct=(
        {
            'dataType': 'int',
            'dataRange': (0, 5),
            'num':2
        },
        {
            'dataType': 'int',
            'dataRange': (10, 15),
            'num':3
        },
        {
            'dataType': 'int',
            'dataRange': (100, 150),
            'num':4
        },
        {
            'dataType': 'float',
            'dataRange': (1.3, 4.9),
            'num':5
        },
        {
            'dataType': 'float',
            'dataRange': (2.6, 7.8),
            'num':1
        },
        {
            'dataType': 'str',
            'dataRange': ('w', 'm', 's', 'f', 'a'),
            'len': 6,
            'num': 1
        },
        {
            'dataType': 'str',
            'dataRange': ('hello', 'world', 'you', 'me', 'hi', ' '),
            'len': 3,
            'num': 1
        }
    )))

if __name__ == '__main__':
    show()