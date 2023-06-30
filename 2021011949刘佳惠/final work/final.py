import randomGeneration
import decorator
import weather

def show():
    print("请输入数字1,2,3来选择查看作业1,2,3，输入数字0退出程序")
    while True:
        x = int(input())
        if x == 1:
            randomGeneration.main1()
        elif x == 2:
            decorator.main2()
        elif x == 3:
            weather.main3()
        elif x == 0:
            print('谢谢使用')
            break
        else:
            print('输入数字为1,2,3,请检查输入！')


if __name__ == '__main__':
    show()