import os
# import DataSampling
# import decorate
# import weather
def choose_files():
    while True:
        try:
            print("请输入您想查看的项目:")
            n = input()
            if n=='1':
                 os.system("python DataSampling.py")
            elif n=='2':
                os.system("python decorate.py")
            elif n=='3':
                os.system("python weather.py")
            else:
                print("请输入范围在1-3的数字")
        except ValueError:
            print("输入数字查看对应项目")
if __name__== "__main__":
    choose_files()
