import os

import work1


#import work1
#from work2 import work2
#from work3 import work3

def files():
    while True:
        try:
            num = int(input("请输入要运行的文件编号："))
            if num == 1:
                #print("<work1>")
                work1.work1()
                os.system("work1.py")
            elif num == 2:
                print("<work2>")
                os.system("work2.py")
            elif num == 3:
                print("<work3>")
                os.system("work3.py")
            else:
                print("\\\\\\输入的文件编号无效！\\\\\\")
        except ValueError:
            print("///输入字符无效///")
if __name__ == "__main__":
    files()
