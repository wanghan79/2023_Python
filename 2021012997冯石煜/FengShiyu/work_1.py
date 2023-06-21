#Feng Shiyu
import random
import string
#test 1
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
#             item = '' .join(random.SystemRandom().choice(datarange) for _ in range(strlen))
#             result.add(item)
#         else:
#             continue
#     return result
# s1 = dataSampling (int, (-999, 1000, 123), 10)
# print(s1)
# s1 = dataSampling (float, (-100, 100), 8)
# print(s1)
# s1 = dataSampling (str, ('a', 'b', 'c', 'd', 'g'), 10)
# print(s1)


# test 2
# def structDataSampling(num, struct):
#     result = list()
#     for index in range(0, num):
#         element = set()
#         for key, value in  struct.items():
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
# s = structDataSampling(6, {int: {'datarange': [4,30]}, float: {'datarange': [3.0, 7.9]}, str: {'datarange': 'jdajhwurfjioafjn', 'len':10}})
# print(s)

#Feng shiyu
#test 3

def structDataSampling(**kwargs):
    result = list()
    for index in range(kwargs['num']):
        element = list()
        for key, value in  kwargs.items():
            if key == 'num':
                continue
            for key, value in value.items():
                if key == 'int':
                    it = iter(value['datarange'])
                    tmp = random.randint(next(it), next(it))
                elif key == 'float':
                    it = iter(value['datarange'])
                    tmp = random.uniform(next(it), next(it))
                elif key == 'str':
                    tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
                element.append(tmp)
        result.append(element)
    return result
s = structDataSampling(int1 = {'int':{'datarange': (44,77)}}, int2 = { 'int':{'datarange': (3,6)} }, float1 = {'float':{'datarange': (3.14,5.15)}}, float2 = {'float':{'datarange': (6.17,10.0)}}, str = {'str': {'datarange': 'adbcdefghijklmnopq', 'len':8}},  num = 5)

if __name__ == '__main__':
    print(s)