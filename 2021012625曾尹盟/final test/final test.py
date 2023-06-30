import os


def runFiles():
    files = {
        1: "test1.py",
        2: "test2.py",
        3: "test3.py"
    }

    while True:
        try:
            choice = int(input("请输入要运行的文件编号(输入200退出)："))
            if choice in files:
                file_path = files[choice]
                os.system(file_path)
            elif choice == 200:
                print("作业展示完毕，欢迎下次再来！")
                break
            else:
                print("请输入有效的文件编号")
        except ValueError:
            print("请输入数字")


runFiles()
