import DataSampling
import Sum
import Weather

def show():
    print(u"请输入数字0~3，其中0为退出，数字1~3分别为查看程序1~3")
    while True:
        try:
            x = int(input())
            if x == 0:
                break
            elif x == 1:
                DataSampling.show()
            elif x == 2:
                Sum.show()
            elif x == 3:
                Weather.show()
            else:
                print(u'输入错误')

if __name__ == '__main__':
    show()
