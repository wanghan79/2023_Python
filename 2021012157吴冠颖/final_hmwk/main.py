import dataSampling
import data_sum_avg
import weather
def main():
    while True:
        print(" Enter a number : 1 is dataSampling , 2 is data_sum_avg , 3 is weather , others are exit")
        a = input("请输入：")
        if a == '1':
            datasampling.DataSampling_res()
        elif a == '2':
            data_sum_avg.cal_res()
        elif a == '3':
            weather.putWeather()
        else:
            break

if __name__=='__main__':
    main()
