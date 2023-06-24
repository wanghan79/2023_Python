
from hw1 import homework1
from hw2 import homework2
from hw3 import homework3


def control():
    print()
    print()
    print("**************张洋的Python 结课作业****************")
    print("****输入 1 or 2 or 3 分别查看作业1 、作业2 、 作业3*****")
    while True :
        a = int(input("请输入 1、2、3查看，输入0退出: \n"))
        if a==1:
            homework1.show()
            print()
        elif a==2:
            homework2.show()
            print()
        elif a==3:
            homework3.show()
            print()
        elif a==0:
            print("感谢")
            break
        else:
            continue

control()