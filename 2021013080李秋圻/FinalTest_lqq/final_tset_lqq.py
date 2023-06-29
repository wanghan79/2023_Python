import DataSampling_lqq
import Sum_Avg_lqq
import Weather_lqq

def show():
    print(u"输入数字1~3来选择查看作业1~3，输入数字0退出程序")
    while True:
        try:
            x = int(input())
            if x == 1:
                DataSampling_lqq.show()
            elif x == 2:
                Sum_Avg_lqq.show()
            elif x == 3:
                Weather_lqq.show()
            elif x == 0:
                break
            else:
                print(u'数字的范围是1~3')
        except ValueError:
            print(u'请输入一个数字')


if __name__ == '__main__':
    show()