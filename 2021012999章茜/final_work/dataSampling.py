import random
import string


def dataSampling(**kwargs):
    result = list()
    for index in range(len(kwargs["struct"])):
        indexNumber = kwargs["struct"][index]
        if indexNumber["type"] is int:
            it = iter(indexNumber["range"])
            tmp = random.randint(next(it), next(it))
            result.append(tmp)
        elif indexNumber["type"] is float:
            it = iter(indexNumber["range"])
            tmp = random.uniform(next(it), next(it))
            result.append(tmp)
        elif indexNumber["type"] is str:
            tmp = ''.join(random.SystemRandom().choice(indexNumber["range"]) for _ in range(indexNumber["len"]))
            result.append(tmp)
        else:
            break
    print(result)
    return result

if __name__ == '__main__':
    param = {
        "struct": ({"type": int,
                    "range": [0, 100]
                    },
                   {"type": float,
                    "range": [0, 100]
                    },
                   {"type": str,
                    "range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                    "len": 10
                    })
    }
    dataSampling(**param)
