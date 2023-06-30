import random

def Decorator(*modes):
    def dataprocess(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            num = 0
            s = 0
            for li in res:
                for x in li:
                    s += x
                    num += 1

            results = {}
            if 'mean' in modes:
                results['mean'] = s / num
            if 'sum' in modes:
                results['sum'] = s

            if results:
                print("Results:")
                for mode, value in results.items():
                    print(f"{mode}: {value}")

            return res, results
        return wrapper
    return dataprocess

@Decorator("mean","sum")
def structDataSampling(n, m):
    res = []

    for _ in range(n):
        x = []
        for _ in range(m):
            x.append(random.uniform(0, 10))
        res.append(x)
    return res
#


class hw02:
    def __init__(self):
        self.name = 'compute'
    def show(self,a,b):
        res, values = structDataSampling(a, b)
        print(res)