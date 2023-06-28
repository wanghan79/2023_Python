import homework1
import homework2
import homework3


def ShowWork():
    while True:
        x = input()
        if x == "1":
            homework1.showRandom()
        elif x == "2":
            homework2.showDataSampling()
        elif x == "3":
            homework3.showWeather()
        elif x == "0":
            break
        else:
            continue


ShowWork()
