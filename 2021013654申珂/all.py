import work1
import work2
import work3


def ShowWork():
    while True:
        x = input()
        if x == "1":
            work1.showRandom()
        elif x == "2":
            work2.showstructData()
        elif x == "3":
            work3.showWeather()
        elif x == "0":
            break
        else:
            continue


ShowWork()
