from work1_wangb import DataSampling_wangb
from work2_wangb import foo_wangb
from work3_wangb import weather_wangb

def show():
    print(u"请输入数字abc来选择查看作业1~3，输入字母d退出程序")
    while True:
        try:
            x = str(input())
            if x == 'a':
                DataSampling_wangb.show()
            elif x == 'b':
                foo_wangb.show()
            elif x == 'c':
                weather_wangb.show()
            elif x == 'd':
                break
            else:
                print(u'字母的范围是a，b，c')
        except ValueError:
            print(u'请输入一个字母')


if __name__ == '__main__':
    show()