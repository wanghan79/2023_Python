# -*- coding: utf-8 -*-
"""
# @Time        : 2023/6/30 16:55
# @Author      : tanliqiu
# @FileName    : wrapper.py
# @Software    : PyCharm
# @ProjectName : python_homework
# @Description : null
"""

import random
from dataSampling import dataSampling

def dataProcess(*args):
    temps=args
    def decorator(func):
        def wrapper(*args,**kwargs):
            data=func(*args,**kwargs)
            count=0
            sum=0
            for li in data:
                for x in li:
                    if type(x) == int or type(x) == float:
                        sum=sum+x
                        count=count+1
            for temp in temps:
                if temp=='average':
                    print(sum/count)
                elif temp=='sum':
                    print(sum)
            return data
        return wrapper
    return decorator

@dataProcess("sum","type")
def foo(**kwargs):
    """
        :param kwargs:
        :return:
        """
    result = dataSampling(**kwargs)
    return result

if __name__ == '__main__':
    test2 = {"num":2,
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
    print(foo(**test2))