from work import work1
from work import work2
from work import work3
def all():
    while(1):
        print("请输入作业1 or 作业2 or 作业3，否则退出程序。")
        x = input("请输入：")
        if x == '1':
            work1.structdataSampling_1()
        elif x =='2':
            work2.data_decorator_2()
        elif x =='3':
            work3.weather_3()
        else:
            print("您输入的不正确，无法获取信息。")
            break

if __name__ == '__main__':
    all()