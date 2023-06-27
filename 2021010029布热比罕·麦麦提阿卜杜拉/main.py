from dataSampling import dataSimpling as randomFn
from dataDecorator import decorator as sum_avg
from weather import run as weather

if __name__ == "__main__":
    while(True):
        choose_num = input("输入作业编号(输入1，2，3，输入exit退出)：")
        if choose_num == 'exit':
            break
        elif choose_num == "1":
            randomFn()

        elif choose_num == "2":
            sum_avg()

        elif choose_num == "3":
            weather()
        else:
            print("输入错误，请重新输入")
        print()