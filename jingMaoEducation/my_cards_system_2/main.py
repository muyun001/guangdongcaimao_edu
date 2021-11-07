import utils
import menu

cards = list()

# 举例
cards = [{'id': '1001', 'name': '张三', 'number': '189189189189', 'QQ': '1212121212'},
         {'id': '1002', 'name': '李四', 'number': '1321312312', 'QQ': '32323232323'},
         {'id': '1003', 'name': '王武', 'number': '123123123', 'QQ': '12312312312'},
         {'id': '1004', 'name': '陈六', 'number': '189176156', 'QQ': '12783749'},
         ]


def create_cards():
    """
    添加卡片
    """
    global cards
    print("欢迎添加卡片，接下来请键入'学号、姓名、手机号、QQ'，【id和姓名不可为空】")
    id_num, name, number, qq = input("请输入学号：").strip(), input("请输入姓名：").strip(), \
                               input("请输入手机号：").strip(), input("请输入QQ：").strip()
    if not id_num:
        id_num = input("输入的学号为空，请重新输入：")
    if not name:
        name = input("输入的姓名为空，请重新输入：")
    if utils.create_cards(cards, id_num, name, number, qq) != -1:
        print("添加名片成功！\n")
        return
    print("\n此卡片已经存在，不可重复添加!\n")


def del_cards():
    """
    删除卡片
    先查询此人信息，再确定是否删除
    """
    global cards
    query_result = query_by_name()
    for card in query_result:
        print("\n根据姓名查询到信息为：", card)
        temp_str = input("\n确认是否删除？（y/n）")
        if temp_str == "y" or temp_str == "Y":
            cards = utils.del_cards(cards, card)
            print("\n删除成功！\n")
        elif temp_str == "n" or temp_str == "N":
            print("\n正在退出删除程序。\n")
            return
        else:
            print("\n输入有误，退出删除程序。\n")
            return


def update_cards():
    """
    修改卡片
    先查询此人信息，再确定是否修改
    """
    global cards
    query_result = query_by_name()
    if not query_result:
        print("退出更新程序。\n")
        return

    print("总计查到{}个结果，开始遍历操作。\n".format(len(query_result)))
    for card in query_result:
        temp_str = input("确定修改？（y/n）")
        if temp_str == "y" or temp_str == "Y":
            phone_num, email = input("手机号：").strip(), input("qq号：").strip()
            card = utils.update_cards(card, phone_num=phone_num, email=email)
            print("修改成功！\n")
        elif temp_str == "n" or temp_str == "N":
            print("不修改此卡片信息。\n")
        else:
            print("\n输入信息有误，退出修改程序。\n")


def query_by_name():
    """
    通过姓名查询卡片
    """
    global cards
    name = input("\n请输入想查询/更新/删除的姓名：")

    # 如果输入为空
    if not name:
        name = input("\n输入的姓名为空，请重新输入：")
    query_result = utils.query_by_name(cards, name)

    # 如果查询到的结果为空
    if not query_result:
        print("\n查询的结果为空\n")
        return
    print("查询成功！查询结果：", query_result)
    return query_result


def query_all_cards():
    """
    查询所有卡片
    """
    global cards
    print("查询所有名片成功！\n")
    for card in utils.query_all_cards(cards):
        print(card)


def run():
    """
    入口函数
    """
    print("\n************* 欢迎使用【名片管理系统】V1.0 *************\n")
    while True:
        menu.show_menu()
        input_str = input("请输入序号：")
        if input_str in ["1", "2", "3", "4", "5"]:
            if input_str == "1":
                create_cards()
            elif input_str == "2":
                del_cards()
            elif input_str == "3":
                update_cards()
            elif input_str == "4":
                query_by_name()
            else:
                query_all_cards()
        elif input_str == "0":  # 退出
            print("收到命令，程序即将退出。。。")
            break
        else:
            print("输入有误，请重新输入！\n")


if __name__ == "__main__":
    run()

    # update_cards()
    # print(cards)
