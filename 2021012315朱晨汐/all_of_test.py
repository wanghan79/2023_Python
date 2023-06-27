import os


def main():
    while True:
        print("请输入要运行的文件编号,输入其他退出程序")
        zcx = input("请输入：")
        if zcx == '1':
            os.system("test1.py")
        elif zcx == '2':
            os.system("test2.py")
        elif zcx == '3':
            os.system("test3.py")
        else:
            break


if __name__ == '__main__':
    main()
