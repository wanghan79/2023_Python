import random

def get_sum(result):
    return sum(sum(row) for row in result)

def get_avg(result):
    num_rows = len(result)
    num_cols = len(result[0])
    return sum(sum(row) for row in result) / (num_rows * num_cols)

def data_processor(*metrics):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {}
            for metric in metrics:
                if metric == "summary":
                    data['summary'] = get_sum(result)
                elif metric == "average":
                    data['average'] = get_avg(result)
            return data
        return wrapper
    return decorator

@data_processor('summary', 'average')
def sample_structured_data(**kwargs):
    result = []
    for i in range(kwargs.get("num")):
        row = []
        for index in kwargs["struct"]:
            index_type = index["type"]
            index_range = index["range"]
            if index_type is int:
                x = random.randint(*index_range)
            elif index_type is float:
                x = random.uniform(*index_range)
            else:
                break
            row.append(x)
        result.append(row)
    print("随机向量如下")
    print(result)
    return result

if __name__ == '__main__':
    params = {
        "struct": [{"type": int, "range": (0, 1000)}] * 6
    }
    calc_result = sample_structured_data(**params, num=50)
    print("计算结果如下")
    print(calc_result)