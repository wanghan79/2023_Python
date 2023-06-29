import os
import weather

def final_test(test_num):
    global result
    if test_num == "1":
        result = os.popen("python sampling.py")
    elif test_num == "2":
        result = os.popen("python process.py")
    elif test_num == "3":
        weather.test_weather()
    else:
        return
    print(result.read())


if __name__ == '__main__':
    while True:
        test_n = input("请输入要求展示的作业号：")
        final_test(test_n)

