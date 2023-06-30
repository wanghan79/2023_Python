##作业二

import random


#1
def dataProcess(*args):
    temp = args[0]
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            num = 0
            s = 0
            for liz in res:
                for x in liz:
                    s += x
                    num += 1
            if temp == 'average':
                print("average:%f"%(s/num))
            elif temp == 'sum':
                print("sum:%f"%s)
            return res
        return wrapper
    return decorator

#2
@dataProcess("sum")

@dataProcess("average")

def DataSampling(struct):
    result = list()
    for i in range(0, struct['num']):
        element = list()
        for key in struct["datatype"]:
            if key == "int":
                it = iter(struct['datarange'])
                tmp = random.randint(next(it), next(it))
            elif key == "float":
                it = iter(struct['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif key == "str":
                continue
            else:
                continue
            element.append(tmp)
        result.append(element)
    return result
def showsumavg():
    struct = {"num": 50, "datatype": ["float", "int"], "datarange": [0, 50]}
    res= DataSampling(struct)
    print(res)

showsumavg()