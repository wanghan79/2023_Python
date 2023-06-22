from work2 import Decorator
from work3 import Iter
from work1 import RandomNumber

if __name__ == '__main__':
    while True:
        work_id=input("输入作业编号(输入1，2，3，输入exit退出)：")
        if work_id=='exit':
            break
        elif int(work_id)==1:
            RandomNumber.PrintNumber()
        elif int(work_id)==2:
            Decorator.PrintstructDataSampling()
        elif int(work_id)==3:
            Iter.PrintWeather()
        else:
            print(f"输入数字范围有误，请重新输入")
            print('')