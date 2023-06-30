import dataSampling #作业1
import decorated #作业2
import iterators #作业3
import sys
def main():
    print("请输入1,2,3查看相应作业，输入0则结束程序")
    while True:
        x = input("请输入作业号：")
        if x == '0':
            sys.exit(0)
        elif x == '1':
            dataSampling.dataSampling()
        elif x == '2':
            decorated.dataSampling1()
        elif x == '3':
            iterators.result()
        else:
            continue
if __name__ == '__main__':
    main()