import random
import string
import struct
# # 用固定参数
# def dataSapling(datatype, datarange, num, strlen = 8):
#   # datatype, datarange, num  是固定值参数
#   # strlen = 8 是默认值参数
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
#     return result
#
# result = dataSapling(int, (-100, 100), 10)
# print(result)
# result = dataSapling(float, (-100, 100), 8)
# print(result)
# result = dataSapling(str, ('z', 'y', 'c'), 5)
# print(result)
# print()
#
#
# num and struct生成任意类型的随机 结构
# def structDataSapling(num, struct):
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
# s = {int:{'datarange':(0,100)}}
# result = structDataSapling(1, s)
# print(result)
# print()


# kwargs同时满足12中的
def kwargsDataSapling(**kwargs):
    # **kwargs 是关键字参数
    result = list()
    for _ in range(kwargs["n"]):
        element = list()
        for key, value in kwargs["struct"].items():
            if value[0] == int:
                it = iter(value[1]['datarange'])
                tmp = random.randint(next(it), next(it))
            elif value[0] == float:
                it = iter(value[1]['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value[0] == str:
                tmp = ''.join(random.SystemRandom().choice(value[1]['datarange']) for _ in range(value[1]['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result


# s = {'dataType1': [int, {'datarange': (0, 100)}], 'dataType2': [float, {'datarange': (0, 100)}], 'dataType3': [str, {'datarange': ('z', 'y', 'c'), 'len': 3}]}
# result = kwargsDataSapling(n=5, struct=s)
# print(result)