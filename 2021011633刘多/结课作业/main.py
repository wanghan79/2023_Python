from homeworks import homework1, homework2, homework3

def main():
    while True:
        print("请选择要展示的作业号：")
        print("1. 作业一")
        print("2. 作业二")
        print("3. 作业三")
        print("0. 退出")
        choice = input("请输入选择的作业号：")

        if choice == "1":
            struct = {"num": 10, "datatype": ["int", "float", "str"], "datarange": [0, 100]}
            generated_data = homework1.dataSampling(**struct)
            print("生成的随机数据结构如下：")
            for data in generated_data:
                print(data)

        elif choice == "2":
            struct = {"num": 30, "datatype": ["float", "float", "float", "int", "float"], "datarange": [0, 30]}
            result = homework2.structDataSampling(struct)
            print("结果如下：")
            print("sum == ", result[0], "avg == ", result[1])

        elif choice == "3":
            cities = [u'北京', u'上海', u'广州', u'长春', u'鄂尔多斯']
            print("获取城市天气数据如下：")
            for weather_data in homework3.WeatherIterable(cities):
                print(weather_data)

        elif choice == "0":
            break

        else:
            print("无效的选择，请重新输入。")

        print("=================")

if __name__ == "__main__":
    main()

