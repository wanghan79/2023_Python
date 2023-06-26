import random


def structDatasampling(**kwargs):
    result = list()
    for index in range(0,kwargs['num']):
        element = list()
        for key, value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                temp = random.randint(next(it), next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                temp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                temp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['strlen']))
            else:
                break
            element.append(temp)
        result.append(element)
    return result


a = {
    "datatype": "int",
    "datarange":(0,100)
}

b= {
    "datatyoe": "float",
    "datarange":(-199,200)
}

c= {
    "datatype":"str",
    "datarange" : "qjjdiehaincbcuieudhdh",
    "strlen": 8
}

example = {
    "num":10,
     "struct":{
         "a":{
             "datatype": "int",
             "datarange": (0, 100)
         },
         "b":{
                "datatype": "float",
                "datarange":(-199,200)
         },
         "d":{
                "datatype":"str",
                 "datarange" : "qjjdiehaincbcuieudhdh",
                "strlen": 8
         }
     }
}

print(structDatasampling(**example))