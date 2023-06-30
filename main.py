#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from work1 import dataSampling
from work2 import data_decorator
from work3 import weather
def main():
    while True:
        print("输入1,2,3查看作业，输入其他退出程序")
        a = input("请输入：")
        if a == '1':
            dataSampling.dataSampling_test1()
        elif a == '2':
            data_decorator.data_decorator_test1()
        elif a == '3':
            weather.weather_test1()
        else:
            break

if __name__=='__main__':
    main()

