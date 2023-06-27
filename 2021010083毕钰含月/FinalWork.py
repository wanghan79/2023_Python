from job1.work1 import show as random_fun
from job2.work2 import show as sum_avg
from job3.work3 import show as weather

if __name__ == "__main__":
    while True:
        choose_num = input("输入作业编号(输入1，job2，job3，输入exit退出)：")
        if choose_num == 'exit':
            break
        elif choose_num == "job1":
            random_fun()
        elif choose_num == "job2":
            sum_avg()

        elif choose_num == "job3":
            weather()
        else:
            print("输入错误，请重新输入")
        print()