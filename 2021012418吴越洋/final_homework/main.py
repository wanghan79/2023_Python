import functions


if __name__ == '__main__':
    print("Please enter a number from 1 to 3 to use the dataSampling, wrapper and weather.")

    x = input()
    try:
        x = int(x)
    except:
        print("Illegal input.")

    if x == 1:
        print("You choice is dataSampling.")
        x = functions.dataSampling(num=2, struct={
            'x': {
                'datatype': int,
                'range': [1, 10]
            },
            'y': {
                'datatype': float,
                'range': [1, 10]
            },
            'z': {
                'datatype': str,
                'range': "abcde",
                'len': 10
            }
        })
        print(x)

    elif x == 2:
        print("You choice is wrapper.")
        ans, data = functions.foo(num=2, struct={
            'x': {
                'datatype': int,
                'range': [1, 10]
            },
            'y': {
                'datatype': float,
                'range': [1, 10]
            },
            'z': {
                'datatype': str,
                'range': "abcde",
                'len': 10
            }
        })
        print(ans)
        print(data)

    elif x == 3:
        print("You choice is weather.")
        for x in functions.WeatherIterable(['北京', '上海', '广州', '长春']):
            print(x)