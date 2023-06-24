import DataSampling_fyy
import Decorater_fyy
import Weather_fyy

def show():
    print("输入1~3来查看作业1~3，输入0退出")
    while True:
        try:
            x = int(input())
            if x == 1:
                DataSampling_fyy.show()
            elif x == 2:
                Decorater_fyy.show()
            elif x == 3:
                Weather_fyy.show()
            elif x == 0:
                break
            else:
                print('范围是1~3')
        except ValueError:
            print('请输入数字')


if __name__ == '__main__':
    show()