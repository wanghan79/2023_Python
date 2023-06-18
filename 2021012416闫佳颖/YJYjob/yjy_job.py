import yjyfunction1, yjyfuncyion2, yjyfunction3


def show_menu():
    print("*" * 50)
    print("【闫佳颖期末作业主菜单】".center(40) + "")
    print("功能执行结束后会回到主菜单".center(40) + "")
    print("1.随机生成数")
    print("2.修饰器")
    print("3.获取城市天气")
    print("4.结束整个程序")
    print("【说明：可能需要将Urllib3的版本降低到2.0.0\n以下才能正常使用功能3】")
    print("*" * 50)


while True:
    show_menu()

    action = input("请输入操作编号")
    print("您选择的操作是【%s】" % action)

    if action in ["1", "2", "3"]:
        if action == "1":
            yjyfunction1.yfunction1()

        if action == "2":
            yjyfuncyion2.yfunction2()

        if action == "3":
            yjyfunction3.yfunction3()

    elif action == "4":
        print("【感谢老师的使用 再见~】")
        break

    else:
        print("您输入的选项有误 请重新输入")
