@Calculation('SUM')
def calculate_sum(**kwargs):
    return generate_random_data(**kwargs)


@Calculation('AVG')
def calculate_average(**kwargs):
    return generate_random_data(**kwargs)


@Calculation('SUM', 'AVG')
def calculate_sum_and_average(**kwargs):
    return generate_random_data(**kwargs)


parameters = {
    "num": 3,
    "data_structure": {
        int: {"range": [1, 10]},
        float: {"range": [1.0, 10.0]},
        str: {"range": string.ascii_letters, "length": 10}
    }
}

print("修饰器参数0个，不实现任何操作：")
result1 = generate_random_data(**parameters)
print(str(result1) + "\n")

print("修饰器参数1个，实现SUM操作：")
result2 = calculate_sum(**parameters)
print(str(result2) + "\n")

print("修饰器参数1个，实现AVG操作：")
result3 = calculate_average(**parameters)
print(str(result3) + "\n")

print("修饰器参数2个，同时实现SUM和AVG操作：")
result4 = calculate_sum_and_average(**parameters)
print(str(result4) + "\n")
