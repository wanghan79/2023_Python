import os


def main():
    # 控制台交互
    while True:
        print("请选择要展示的作业编号：")
        print("1. 实现随机数据结构生成封装函数")
        print("2. 采用修饰器技术对作业1进行修饰")
        print("3. 使用迭代器实现城市天气数据的自动获取")
        print("0. 退出程序")
        choice = input()
        if choice == "1":
            print("-" * 50)
            print("运行作业1")
            os.system('python 作业1.py')
            print("-" * 50)
        elif choice == "2":
            print("-" * 50)
            print("运行作业2")
            os.system('python 作业2.py')
            print("-" * 50)
        elif choice == "3":
            print("-" * 50)
            print("运行作业3")
            os.system('python 作业3.py')
            print("-" * 50)
        elif choice == "0":
            print("感谢使用程序，再见！")
            break
        else:
            print("输入有误，请重新选择")


if __name__ == '__main__':
    main()

