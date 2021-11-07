def showMenu():
    """
     显示菜单
    """
    print("*" * 60)
    print("欢迎使用【名片管理系统】V1.0\n")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片\n")
    print("0. 退出系统")


# 定义一个列表，用于存储名片信息
cardList = []


def createCard():
    """
     新增名片
    """
    print("--------------------新建名片-----------------------")
    choose = ""

    while True:
        # 判断后面的选择，如果为2，结束新增功能
        if choose == "2":
            showMenu()
            break
        # 姓名、电话、QQ、邮件
        name = input("请输入姓名：").strip()
        phone = input("请输入电话：").strip()
        qq = input("请输入QQ：").strip()
        email = input("请输入邮件：").strip()

        # 将所有的信息分装到字典中
        infoDic = {"name": name, "phone": phone, "qq": qq, "email": email}
        print("新增成功！！！！！！")
        # 存放名片的列表
        cardList.append(infoDic)
        print(cardList)
        choose = input("请选择  1 继续新增  2 返回主页 :").strip()
        while True:
            if choose in ["1", "2"]:
                break
            else:
                choose = input("输入有误，请重新输入：").strip()


def queryAll():
    """
     查询全部
    """
    if len(cardList) > 0:
        for info in cardList:
            print(info)
    else:
        print("暂无数据")


def queryByName():
    """
     通过姓名查询
    """
    choose = ""
    index = 0
    while True:
        # 判断后面的选择，如果为2，结束新增功能
        if choose == "2":
            showMenu()
            break
        if len(cardList) > 0:
            qName = input("请输入要查询的姓名：").strip()
            for info in cardList:
                if qName == info["name"]:
                    print(info)
                    index += 1
            if index == 0:
                print("查无此人")
            choose = input("请选择  1 继续查询  2 返回主页 :").strip()
            while True:
                if choose in ["1", "2"]:
                    break
                else:
                    choose = input("输入有误，请重新输入：").strip()

        else:
            print("系统暂无数据")
            showMenu()
            shoose = input("请您选择: ")
            return shoose
