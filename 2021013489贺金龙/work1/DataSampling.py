# hejinlong
# def func(*args):
#     for arvg in args:
#         print(arvg)
#
# func([2, 3, 5, 53, 55], ["dfssf", "21342"], (3, 5, 9))
# func("dskfsjlfdk")
import random
import string


# def func(constvalue, *args, defaultvalue = 100, **keyargs):
#     print("固定值 ", constvalue)
#     print("默认值 ", defaultvalue)
#     print("可变参数:")
#     for argv in args:
#         print(argv)
#     print("keyword:")
#     for x, y in keyargs.items():
#         print(x, y)
#
# dia = {'1' : "dksfk"}
# func(10, 1, 3, **dia)
# func(10, 2, 1, 2, 3, 4, a = 1, b = 2)
# func(100, 2)

# def dataSampling(datatype, datarange, num, strlen=8):
#     result = set()
#     for index in range(0, num):
#         if datatype is int:
#             it = iter(datarange)
#             item = random.randint(next(it), next(it))
#             result.add(item)
#             continue
#         elif datatype is float:
#             it = iter(datarange)
#             item = random.uniform(next(it), next(it))
#             result.add(item)
#             continue
#         elif datatype is str:
#             item = ''.join(random.SystemRandom().choice(datarange) for _ in range(strlen))
#             result.add(item)
#             continue
#         else:
#             continue
#     print(result)
#     return result
#
# result = dataSampling(int, [0, 100, 10000, 1000000], 5)
# dataSampling(float, [0, 100, 10000, 1000000], 5)
# dataSampling(str, ['a', 'b', 'v', 'e'], 5)


# def structDataSampling(num, struct):
#     result = list()
#     for index in range(0, num):
#         element = list()
#         for key, value in struct.items():
#             if key is int:
#                 it = iter(value['datarange'])
#                 tmp = random.randint(next(it), next(it))
#             elif key is float:
#                 it = iter(value['datarange'])
#                 tmp = random.uniform(next(it), next(it))
#             elif key is str:
#                 tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
#             else:
#                 break
#             element.append(tmp)
#         result.append(element)
#     return result
#
# # map = {int : {'len': 8, 'datarange': (0, 100, 10000, 100000)}}
# # map = {float : {'len': 8, 'datarange': (0, 100, 1000, 100000)}}
# map = {str: {'len': 8, 'datarange' : ('a', 'b', 'c', 'dwj')}}
# result = structDataSampling(5, map)
# print(result)

# def structDataSampling(**keyargs):
# result = list()
# num = keyargs.get("num", -1)
# if num == -1:
#     raise KeyError("error in num")
# for index in range(0, num):
#     element = list()
#     for key, value in keyargs.items():
#         if key == "int":
#             it = iter(value['datarange'])
#             tmp = random.randint(next(it), next(it))
#         elif key == "float":
#             it = iter(value['datarange'])
#             tmp = random.uniform(next(it), next(it))
#         elif key == "str":
#             tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
#         elif key == "num":
#             continue
#         else:
#             break
#         element.append(tmp)
#     result.append(element)
# return result

# def structDataSampling(**keyargs):
#     result = list()
#     num = keyargs.get("num", -1)
#     if num == -1:
#         raise KeyError("error in num")
#     for index in range(0, num):
#         Oneself = list()
#         for pos, item in keyargs.items():
#             if pos == 'DataType':
#                 for key, value in item.items():
#                     OneDataType = list()
#                     if key == "int":
#                         for cnt in range(0, value['num']):
#                             it = iter(value['datarange'])
#                             tmp = random.randint(next(it), next(it))
#                             OneDataType.append(tmp)
#                     elif key == "float":
#                         for cnt in range(0, value['num']):
#                             it = iter(value['datarange'])
#                             tmp = random.uniform(next(it), next(it))
#                             OneDataType.append(tmp)
#                     elif key == "str":
#                         for cnt in range(0, value['num']):
#                             tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
#                             OneDataType.append(tmp)
#
#                     Oneself.append(OneDataType)
#         result.append(Oneself)
#     return result

def structDataSampling(**keyargs):
    result = list()
    num = keyargs.get("num", -1)
    if num == -1:
        raise KeyError("error in num")
    for index in range(0, num):
        Oneself = list()
        for pos, item in keyargs.items():
            if pos == 'DataType':
                for key1, value1 in item.items():
                    OneDataType = list()
                    for key, value in value1.items():
                        if key == "int":
                            it = iter(value['datarange'])
                            tmp = random.randint(next(it), next(it))
                            OneDataType.append(tmp)
                        elif key == "float":
                            it = iter(value['datarange'])
                            tmp = random.uniform(next(it), next(it))
                            OneDataType.append(tmp)
                        elif key == "str":
                            tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                            OneDataType.append(tmp)

                    Oneself.append(OneDataType)
        result.append(Oneself)
    return result

struct = {'num': 2,'DataType':{
'1':{"str": {'len': 8, 'datarange' : ('a', 'dwj', 'b', 'c', 'd')}, "int" : {'datarange': (0, 10000)}, "float" : {'len': 8, 'datarange': (0, 100, 1000, 100000)}},
'2':{"str": {'len': 8, 'datarange' : ('a', 'dwj', 'b', 'c', 'd')}, "int" : {'datarange': (0, 10000)}, "float" : {'len': 8, 'datarange': (0, 100, 1000, 100000)}},
'3':{"str": {'len': 8, 'datarange' : ('a', 'dwj', 'b', 'c', 'd')}, "int" : {'datarange': (0, 10000)}, "float" : {'len': 8, 'datarange': (0, 100, 1000, 100000)}},
'4':{"str": {'len': 8, 'datarange' : ('a', 'dwj', 'b', 'c', 'd')}, "int" : {'datarange': (0, 10000)}, "float" : {'len': 8, 'datarange': (0, 100, 1000, 100000)}},
    }
}


# struct = {'num': 2, 'DataType' : {"str": {'num' : 10, 'len': 8, 'datarange' : ('a', 'dwj', 'b', 'c', 'd')}, "int" : {'num' : 3, 'datarange': (0, 10000)}, "float" : {'num': 2, 'len': 8, 'datarange': (0, 100, 1000, 100000)}}}
result = structDataSampling(**struct)
print(result)
