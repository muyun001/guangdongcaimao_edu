import util

util.showMenu()

print("*" * 60)

choose = input("请您选择 : ").strip()
while True:
    if choose in ["1", "2", "3"]:
        if choose == "1":
            util.createCard()
            # util.showMenu()
            choose = input("请您选择").strip()
        elif choose == "2":
            util.queryAll()
            input("查询结束，按任意键返回主菜单：")
            util.showMenu()
            choose = input("请您选择").strip()
        else:
            choose = util.queryByName()
    elif choose == "0":
        print("欢迎下次光临......")
        break
    else:
        choose = input("输入有误，请重新输入 :").strip()
