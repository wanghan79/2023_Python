import random

def data_Sampling(**kwargs):
    structure = kwargs.get("struct")
    result = list()
    for index in range(0, kwargs.get("num")):
        element = dict()
        for key, value in structure.items():
            if value["data_type"] == "int":
                it = iter(value['data_range'])
                tmp = random.randint(next(it), next(it))
            elif value["data_type"] == "float":
                it = iter(value['data_range'])
                tmp = random.uniform(next(it), next(it))
            elif value["data_type"] == "str":
                tmp = ''.join(random.SystemRandom().choice(value['data_range']) for _ in range(value['len']))
            else:
                break
            element[key] = tmp
        result.append(element)
    return result

def test_sampling():
    a = data_Sampling(
            num=10,
            struct={
                "a": {
                    "data_type": "int",
                    "data_range": (0, 100)},
                "b": {
                    "data_type": "float",
                    "data_range": (0, 100)},
                "c": {
                    "data_type": "str",
                    "data_range": ('abc', 'xyz'), "len": 10}
            }
        )
    print(a)

