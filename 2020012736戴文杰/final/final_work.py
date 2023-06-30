import dataprocess
import decorate
import weather
if __name__ == '__main__':
    print("welcome to my homework")
    print("if input is 0 or other, exit\n"
          "if input is 1, display assignment 1\n"
          "if input is 2, display assignment 2\n"
          "if input is 3, display assignment 3\n"
          )
    while True:
        x = int(input("plase input： "))
        if x == 0:
            break
        elif x == 1:
            dataprocess.dataSampling_test()
        elif x == 2:
            decorate.struct_test()
        elif x == 3:
            weather.weather_test()
        else:
            print("sorry,Error input")
            break