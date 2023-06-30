import random

def sumAns(result):
    ans = 0
    for i in range(len(result)):
        for j in range(len(result[0])):
           ans += result[i][j]
    return ans

def avgAns(result):
    ans = 0
    for i in range(len(result)):
        for j in range(len(result[0])):
           ans += result[i][j]
    ans /= (len(result)*len(result[0]))
    return ans

def dataProcess(*args):
    def decorator(func):
        def wrapper(**kwargs):
            ans = {}
            result = func(**kwargs)
            for requst in args:
                if requst == 'sum':
                    ans['sum'] = sumAns(result)
                if requst == 'avg':
                    ans['avg'] = avgAns(result)
            return ans
        return wrapper
    return decorator


@dataProcess('sum','avg')
def structDataSampling2(**kwargs):
    result = list()
    for index in range(kwargs.get('num')):
        elemet = list()
        for c in kwargs.get('struct'):
            if c['dataType'] == 'int':
                for i in range(c['num']):
                    it = iter(c['dataRange'])
                    tmp = random.randint(next(it), next(it))
                    elemet.append(tmp)
            elif c['dataType'] == 'float':
                for i in range(c['num']):
                    it = iter(c['dataRange'])
                    tmp = random.uniform(next(it),next(it))
                    elemet.append(tmp)
            else:
                print("something wrong")
        result.append(elemet)
    for i in range(len(result)):
        print(result[i])
    return result

if __name__ == '__main__':
    # 共21行，每行5个元素。
    result = structDataSampling2(num=21, struct=(
        {
            'dataType': 'int',
            'dataRange': (10, 100),
            'num': 1
        },
        {
            'dataType': 'int',
            'dataRange': (500, 800),
            'num': 1
        },
        {
            'dataType': 'float',
            'dataRange': (1.2, 4.8),
            'num': 3
        }
    ))

    print(result)
