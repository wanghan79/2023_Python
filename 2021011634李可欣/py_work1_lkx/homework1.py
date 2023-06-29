import string
import random

def dataSampling(**kwargs):
    result = list()
    for index in range(len(kwargs["struct"])):
        data = kwargs["struct"][index]
        if data["datatype"] is int:
            it = iter(data["datarange"])
            item = random.randint(next(it), next(it))
            result.append(item)
            continue

        elif data["datatype"] is float:
            it = iter(data["datarange"])
            item = random.uniform(next(it), next(it))
            result.append(item)
            continue

        elif data["datatype"] is str:
            item = ''.join(random.SystemRandom().choice(data["datarange"]) for _ in range(data["len"]))
            result.append(item)
            continue

        else:
            break
    print(result)
    return result

structDataSampling = {
    "struct": ({"datatype": int,
                "datarange": [0, 100]
                },
               {"datatype": float,
                "datarange": [0.0, 100.0]
                },
               {"datatype": str,
                "datarange": ['0','1','2','3','a', 'b', 'c', 'd', 'e', 'f', 'g','h'],
                "len": 10
                })
}
dataSampling(**structDataSampling)