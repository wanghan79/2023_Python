import DataSampling_hjp
import Sum_Avg_hjp
import Weather_hjp

def show():
    print(u"请输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                DataSampling_hjp.show()
            elif x == 2:
                Sum_Avg_hjp.show()
            elif x == 3:
                Weather_hjp.show()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')