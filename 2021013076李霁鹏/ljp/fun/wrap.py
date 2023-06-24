import random

def dataProcess(*args):
    mode = args[0]
    def decator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            sum = 0
            num = 0
            if mode == "avg":
                for i in result:
                    for x in i:
                        num += 1
                        sum += x
                print("avg:")
                print(sum/num)
            elif mode == "sum":
                for i in result:
                    for x in i:
                        sum += x
                print("sum:")
                print(sum)
            else:
                for i in result:
                    for x in i:
                        num += 1
                        sum += x
                print("avg:")
                print(sum/num)
                print("sum:")
                print(sum)

            return result
        return wrapper
    return decator

@dataProcess('avg&sum')
def dataSampling(**kwargs):
    res = list()
    structure = kwargs.get('struct')
    structure = structure.items()
    for i in range(kwargs.get('num')):
        element = []
        for key,value in structure:
            if value['type'] == int:
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            else:
                break
            element.append(tmp)
        res.append(element)
    return res

def wrapTest():
    b = dataSampling(num=50, struct={
        'a': {
            "type": int,
            'datarange': (0, 100)},
        'b': {
            "type": int,
            'datarange': (0, 100)},
        'c': {
            "type": int,
            'datarange': (0, 100)},
        'd': {
            "type": int,
            'datarange': (0, 100)},
        'e': {
            "type": int,
            'datarange': (0, 100)},
        'f': {
            "type": int,
            'datarange': (0, 100)}
    })
    # print(b)
