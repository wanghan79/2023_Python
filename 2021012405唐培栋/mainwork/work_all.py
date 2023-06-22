
from homework1 import prac_1
from homework2 import prac_2
from homework3 import prac_3


def control():
    print()
    print()
    print("**************Swimy的Python 结课作业****************")
    print("****输入 1 or 2 or 3 分别查看作业1 、作业2 、 作业3*****")
    while True :
        a = int(input("请输入 1、2、3查看，输入0退出: \n"))
        if a==1:
            prac_1.show()
            print()
        elif a==2:
            prac_2.show()
            print()
        elif a==3:
            prac_3.show()
            print()
        elif a==0:
            print("感谢")
            break
        else:
            continue

control()