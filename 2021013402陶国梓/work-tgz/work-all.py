import os

def run_files():
    while True:
        try:
            choice = int(input("请输入想运行的文件编号1、2、3："))
            if choice == 1:
                os.system("DataSampling.py")
            elif choice == 2:
                os.system("SumAndAve.py")
            elif choice == 3:
                os.system("Weather.py")
            else:
                print("只能输入1，2，3")
        except ValueError:
            print("error")

if __name__ == "__main__":
    run_files()