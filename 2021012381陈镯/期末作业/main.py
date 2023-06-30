import sampling
import process
import weather

def final_test(test_num):
    global result
    if test_num == "1":
        sampling.test_sampling()
    elif test_num == "2":
        process.test_process()
    elif test_num == "3":
        weather.test_weather()
    else:
        return

if __name__ == '__main__':
    while True:
        test_n = input("请输入展示的作业号：")
        final_test(test_n)

