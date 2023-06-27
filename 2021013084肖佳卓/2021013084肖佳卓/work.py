import os


def run_files():
    while True:
        try:
            choice = int(input("请输入要运行的文件编号："))
            if choice == 1:
                os.system("test1.py")
            elif choice == 2:
                os.system("test2.py")
            elif choice == 3:
                os.system("test3.py")
            else:
                print("请输入有效的文件编号！")
        except ValueError:
            print("请输入数字！")


if __name__ == "__main__":
    run_files()
