

import os
import requests
while(True):
    a = input('输入你想要执行1的工程，工程1为随机数任务，工程2为修饰器任务，工程3为抓取天气任务：')
    print(a)
    print(type(a))
    if a == "1":
        os.system("python ./Task1/randomTask.py")
    elif a == "2":
        os.system("python ./Task2/decratorTask.py")
    elif a == "3":
        os.system("python ./Task3/weatherTask.py")
    elif a == '-1':
        break
    else:
        raise ValueError("没有找到指定的工程")
        break

