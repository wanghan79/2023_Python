import os


def run():
    while True:
        try:
            choice = int(input("请输入要运行的编号："))
            if choice == 1:
                os.system("structDataSampling.py")
            elif choice == 2:
                os.system("dacorator.py")
            elif choice == 3:
                os.system("weather.py")
            elif choice == 4:
                break
            else:
                print("请输入正确的文件编号！")
                print("如果你想退出当前程序，请输入数字4。")
        except ValueError:
            print("请输入数字实现对应的函数方法:")


if __name__ == "__main__":
    run()
