from fun import dataSampling, weather, wrap

if __name__ == '__main__':
    while True:
        cmd = int(input("1--dataSampling   2--wrap   3--weather   0--exit\n"))
        print("\n")
        if cmd == 1:
            dataSampling.dataSamplingTest()
            print("\n")
        if cmd == 2:
            wrap.wrapTest()
            print("\n")
        if cmd == 3:
            weather.weatherTest()
            print("\n")
        if cmd == 0:
            break
