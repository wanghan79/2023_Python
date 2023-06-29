from data_sampling import dataSampling


def dataOperation(*operations):
    def decorator(func):
        def wrapper(**kwargs):
            random_data = func(**kwargs)
            print(random_data)
            for operation in operations:
                if operation == 'SUM':
                    total_sum = sum(sum(sublist) for sublist in random_data)
                    print("Sum of all elements:", total_sum)
                elif operation == 'AVG':
                    total_count = sum(len(sublist) for sublist in random_data)
                    total_sum = sum(sum(sublist) for sublist in random_data)
                    if total_count > 0:
                        average = total_sum / total_count
                        print("Average of all elements:", average)
        return wrapper
    return decorator

@dataOperation('SUM')
def data_sum(**kwargs):
    return dataSampling(**kwargs)

@dataOperation('AVG')
def data_avg(**kwargs):
    return dataSampling(**kwargs)

# # 调用示例
# data_sum(int=5, float=3)
# data_avg(int=5, float=3)