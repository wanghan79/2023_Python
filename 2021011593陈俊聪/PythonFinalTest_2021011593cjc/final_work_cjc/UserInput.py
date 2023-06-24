import UserView
from PythonClass.work_1_cjc import RandomDataSampling
from PythonClass.work_2_cjc import AdvancedDataSampling
from PythonClass.work_3_cjc import GetWeather


def mainMenuInput():
    while True:
        try:
            UserView.enterMainMenu()
            # User's choice
            choice = int(input("Please enter your corresponding choice:"))
            if choice == 1:
                UserView.randomDataSampling()
                RandomDataSampling.example()
            elif choice == 2:
                advancedDataSamplingInput()
            elif choice == 3:
                city = getWeatherInput()
                GetWeather.example(city)
            elif choice == 4:
                print("You have exited!")
                break
            else:
                print("Please input again! you have entered a wrong number")
        except:
            print("Wrong input!")


def advancedDataSamplingInput():
    while True:
        try:
            UserView.advancedRandomDataSamplingCalculation()
            choice = int(input("Please enter your corresponding choice:"))
            if choice == 1:
                sample_number = int(input("Please enter the sample number: "))
                AdvancedDataSampling.example(sample_number)
            elif choice == 2:
                break
            else:
                print("Please input again! you have entered a wrong number")
        except:
            print("Wrong input!")


def getWeatherInput():
    while True:
        try:
            UserView.getWeatherViewing()
            choice = int(input("Please enter your corresponding choice:"))
            if choice == 1:
                city = input("Please enter the city you want to enquire about(in Chinese): ")
                return city
            elif choice == 2:
                break
            else:
                print("Please input again! you have entered a wrong number")
        except:
            print("Wrong input!")
