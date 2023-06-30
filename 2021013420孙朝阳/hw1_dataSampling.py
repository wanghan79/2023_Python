import random


def dataSampling(**kwargs):
    result_set = list()
    for index in range(len(kwargs["struct"])):
        idxNum = kwargs["struct"][index]
        if idxNum["type"] is int:
            it = iter(idxNum["range"])
            tmp = random.randint(next(it), next(it))
            result_set.append(tmp)
        elif idxNum["type"] is float:
            it = iter(idxNum["range"])
            tmp = random.uniform(next(it), next(it))
            result_set.append(tmp)
        elif idxNum["type"] is str:
            tmp = ''.join(random.SystemRandom().choice(idxNum["range"]) for _ in range(idxNum["len"]))
            result_set.append(tmp)
        else:
            break
    return result_set


def genStructs(num_input, structures):
    return [dataSampling(**structures) for _ in range(num_input)]


structure = {"struct": ({"type": int, "range": [0, 100]}, {"type": float, "range": [0, 100]},
                        {"type": str, "range": ['a', 'b', 'c', 'd', 'e', 'f', 'g'], "len": 10})}

num_structs = 10  # 指定生成10个结构体
results = genStructs(num_structs, structure)
print("生成的随机数据结构如下：")
for struct in results:
    print(struct)
