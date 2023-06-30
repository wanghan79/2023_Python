# -*- coding: utf-8 -*-
"""
# @Time        : 2023/6/30 16:56
# @Author      : tanliqiu
# @FileName    : homework_summary.py
# @Software    : PyCharm
# @ProjectName : python_homework
# @Description : null
"""
import dataSampling
import weather
import wrapper

if __name__ == '__main__':
    print("请输入1、2、3中的数字，来使用dataSampling、wrapper和weather")

    x = input()
    try:
        x = int(x)
    except:
        print("非法输入")

    if x == 1:
        print("已选择dataSampling")
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
        print(dataSampling.dataSampling(**test1))

    elif x == 2:
        print("已选择wrapper")
        test2 = {"num": 2,
                 "struct": {
                     "tp1": {
                         "datatype": 'int',
                         "datarange": {0, 100}
                     },
                     "tp2": {
                         "datatype": 'float',
                         "datarange": {0, 100}
                     },
                     "tp3": {
                         "datatype": 'str',
                         "datarange": "abcde",
                         "len": 10
                     }
                 }

                 }
        print(wrapper.foo(**test2))

    elif x == 3:
        print("已选择weather.")
        test3 = weather.show()
        a = ['北京', '长春', '上海', '重庆']
        test3.show(a)