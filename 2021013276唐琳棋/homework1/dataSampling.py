# -*- coding: utf-8 -*-
"""
# @Time        : 2023/6/30 16:55
# @Author      : tanliqiu
# @FileName    : dataSampling.py
# @Software    : PyCharm
# @ProjectName : python_homework
# @Description : null
"""

import random

def dataSampling(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for item in range(kwargs['num']):
        element = list()
        for key,value in kwargs['struct'].items():
            if value['datatype'] == 'int':
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif value['datatype'] == 'float':
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

if __name__ == '__main__':
    test1 = {"num":2,
             "struct":{
                 "tp1":{
                     "datatype":'int',
                     "datarange":{0,100}
                 },
                 "tp2":{
                     "datatype": 'float',
                     "datarange": {0, 100}
                 },
                 "tp3":{
                     "datatype": 'str',
                     "datarange": "abcde",
                     "len":10
                 }
             }

    }
    print(dataSampling(**test1))