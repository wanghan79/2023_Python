import function

if __name__ == '__main__':
    print("输入1展示作业1, 输入2展示作业2, 输入3展示作业3, 输入其他将退出程序")
    while True:
        x = int(input("请输入： "))
        if x == 1:
            function.dataSampling_test()
        elif x == 2:
            function.wrapper_test()
        elif x == 3:
            function.weather_test()
        else:
            break

