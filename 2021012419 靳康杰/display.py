import os


def runFiles():
    while True:
        try:
            choice = int(input("请输入要运行的文件编号(输入200退出)："))
            if choice == 1:
                os.system("assignment1.py")
            elif choice == 2:
                os.system("assignment2.py")
            elif choice == 3:
                os.system("assignment3.py")
            elif choice == 200:
                print("作业展示完毕，欢迎下次再来！")
                break
            else:
                print("请输入有效的文件编号")
        except ValueError:
            print("请输入数字")


runFiles()
