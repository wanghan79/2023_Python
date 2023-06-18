"""
@Author: 邓长圣
@Date: 2023/6/9
@Content: python大作业
            对本期python课程中的三次作业进行集成，提供一个操作菜单，按需求查看三次作业
"""
from work_first import workFirst
from work_second import workSecond
from work_third import workThird


def menu():
    # print("######## MENU #######")
    # print("###\t1： 查看作业一 ####\n###\t2： 查看作业二 ####\n###\t3： 查看作业三 ####\n###-1： 退出      ####")
    # print("#####################")
    print("\n--------------------------------------------------------------------------------------------------")
    print("     	 python大作业--MENU")
    print("       ################################################")
    print("       按键1：作业一")
    print("       按键2：作业二")
    print("       按键3：作业三")
    print("       按键4：展示MENU")
    print("       按键0: 退出")
    print("       ################################################")
    print("--------------------------------------------------------------------------------------------------")
    # print("\n ====>>>>>请输入你的选择:")


def myInput():
    while True:
        try:
            operation = int(input("\n====>>>>>请输入你的选择:"))
            if operation == 1:
                # 作业一
                workFirst.show()

            elif operation == 2:
                # 作业二
                workSecond.show()

            elif operation == 3:
                # 作业三
                workThird.show()

            elif operation == 4:
                menu()

            elif operation == 0:
                print('THANKS')
                break

            else:
                print("wrong input, please read the MENU and input again")
        except:
            print("wrong input, please read the MENU and input again")


if __name__ == "__main__":
    menu()
    myInput()
