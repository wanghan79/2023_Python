import test1
import test2
import test3

if __name__ == "__main__":
    while(True):
        num = input("输入作业编号(输入1，2，3运行相应test1/2/3，输入-1退出)：\n")
        if num == "-1":
            break
        elif num == "1":
            test1.result_1()

        elif num == "2":
            test2.result_2()

        elif num == "3":
            test3.result_3()
        else:
            print("输入错误，请重新输入")
        print()