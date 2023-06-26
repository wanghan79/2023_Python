def sum(temp):
    """
    :description: 求和
    :param temp: list
    :return: 总和
    """
    m = 0
    for i, element in enumerate(temp):
        n = 0
        for j in iter(element):
            n = n + j
        print(f"第{i}组数据的和为{n}")
        m = m + n
    print("------------------------")
    print(f"<---此次数据的总和为{m}--->")


def average(temp):
    """
    :description: 求平均值
    :param temp: list
    :return: 均值
    """
    m = 0
    for i, element in enumerate(temp):
        n = 0
        for j in iter(element):
            n = n + j
        print(f"第{i}组数据的均值为{n / len(element)}")
        m = m + n
    print("------------------------")
    print(f"<---此次数据的总均值为{m / len(temp)}--->")
