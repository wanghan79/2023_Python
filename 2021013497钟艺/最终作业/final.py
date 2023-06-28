import first
import second
import third

if __name__ == "__main__":

    while True:
        operation = input("请输入（1：作业1，2：作业2， 3：作业三， 0：退出）:")
        if operation == '1':
            first.test()

        elif operation == '2':
            second.test()

        elif operation == '3':
            third.test()

        elif operation == '0':
            print("Thanks")
            break;
        else:
            continue