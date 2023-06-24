import random

def dataSampling(**kwargs):
    structure = kwargs.get("struct")
    result = list()
    for index in range(0, kwargs.get("num")):
        element = dict()
        for key, value in structure.items():
            if value["datatype"] == "int":
                it = iter(value['data_range'])
                tmp = random.randint(next(it), next(it))
            elif value["datatype"] == "float":
                it = iter(value['data_range'])
                tmp = random.uniform(next(it), next(it))
            elif value["datatype"] == "str":
                tmp = ''.join(random.SystemRandom().choice(value['data_range']) for _ in range(value['len']))
            else:
                break
            element[key] = tmp
        result.append(element)
    return result

def dataSamplingTest():
    a = dataSampling(
        num=5,
        struct={
         "a": {
             "datatype": "int",
             "data_range": (0, 100)},
         "b": {
             "datatype": "float",
             "data_range": (0, 100)},
         "c": {
             "datatype": "str",
             "data_range": ('abc', 'abz'), "len": 5}
         }
         )
    print(a)
