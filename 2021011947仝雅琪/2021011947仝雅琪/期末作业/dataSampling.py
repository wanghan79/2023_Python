import random
import string

def dataSampling(**kwargs):
    result = []
    for i in range(kwargs.get('num')):
        for index in kwargs["struct"]:
            if index["type"] == int:
                it = iter(index["range"])
                tmp = random.randint(next(it),next(it))
                result.append(tmp)
            elif index["type"] == float:
                it = iter(index["range"])
                tmp = random.uniform(next(it),next(it))
                result.append(tmp)
            elif index["type"] == str:
                result.append(''.join(random.SystemRandom().choice(index["range"]) for _ in range(index["len"])))
    return result


if __name__ == '__main__':
    demo = {"num":2,"struct":({"type":int,"range":[0,100]},
                        {"type":float,"range":[0,100]},
                        {"type":str,"range":['a','b','c','d','e','f','g','e'],"len":10})
            }
    print(dataSampling(**demo))