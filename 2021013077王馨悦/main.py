import work1
import work2
import work3
import sys
def main():
    print("请输入1,2,3查看相应作业，输入0则结束程序")
    while True:
        x = input("请输入作业号：")
        if x == '0':
            sys.exit(0)
        elif x == '1':
            work1.dataSumpling()
        elif x == '2':
            work2.Random()
        elif x == '3':
            work3.weather()
        else:
            continue
if __name__ == '__main__':
    main()
