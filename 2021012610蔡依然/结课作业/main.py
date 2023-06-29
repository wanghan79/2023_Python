while True:
    user_input = input("请输入要执行的文件编号（输入q退出）：")

    if user_input.lower() == 'q':
        break

    if user_input == '1':
        with open("first_homework.py", encoding="utf-8") as file:
            exec(file.read())
    elif user_input == '2':
        with open("second_homework.py", encoding="utf-8") as file:
            exec(file.read())
    elif user_input == '3':
        with open("third_homework.py", encoding="utf-8") as file:
            exec(file.read())
    else:
        print("无效的输入")