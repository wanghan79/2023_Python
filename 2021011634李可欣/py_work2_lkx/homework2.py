import random

def SUM(result):
    return sum(sum(row) for row in result)

def AVG(result):
    num_rows = len(result)
    num_cols = len(result[0])
    return sum(sum(row) for row in result) / (num_rows * num_cols)

def data_processor(*metrics):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {}
            for metric in metrics:
                if metric == "SUM":
                    data['SUM'] = SUM(result)
                elif metric == "AVG":
                    data['AVG'] = AVG(result)
            return data
        return wrapper
    return decorator

@data_processor('SUM', 'AVG')
def data(**kwargs):
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
    return result

param = {
    "struct": [{"type": int, "range": (0, 100)}] * 10
}
result = data(**param, num=50)
print(result)