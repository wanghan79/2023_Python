from test1_yx.DataSampling import run as random_fun
from test2_yx.Sum_Avg import run as sum_avg
from test3_yx.Weather import run as weather

if __name__ == "__main__":
    while(True):
        choose_num = input("输入作业编号(输入1，2，3，输入exit退出)：")
        if choose_num == 'exit':
            break
        elif choose_num == "1":
            random_fun()

        elif choose_num == "2":
            sum_avg()

        elif choose_num == "3":
            weather()
        else:
            print("输入错误，请重新输入")
        print()
