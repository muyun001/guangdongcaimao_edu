def create_cards(cards, id_num, name, number, qq):
    """
    添加名片
    """

    card = {"id": id_num, "name": name, "number": number, "QQ": qq}
    if card not in cards:
        cards.append(card)
        return
    return -1


def del_cards(cards, card):
    """
    通过姓名删除名片
    直接return cards.remove(card)，返回remove函数的返回值，但这个函数没有返回值，所以返回结果就是none
    """
    cards.remove(card)
    return cards


def update_cards(card, **kwargs):
    """
    通过姓名修改名片
    """
    card["number"] = kwargs.get("phone_num")
    card["email"] = kwargs.get("email")
    return card


def query_by_name(cards, name):
    """
    通过姓名查询名片
    return 查询结果组成的列表
    """
    query_result = list()
    for card in cards:
        if card["name"] == name:
            query_result.append(card)
    return query_result


def query_all_cards(cards):
    """
    查询所有名片
    """
    return cards


# 测试入口
if __name__ == "__main__":
    cards = [
        {'name': 'zhangsan', 'phone': '111', 'qq': '111', 'email': '111'},
        {'name': 'lisi', 'phone': '222', 'qq': '222', 'email': '222'},
        {'name': 'wangwu', 'phone': '333', 'qq': '333', 'email': '333'},
        {'name': 'chenliu', 'phone': '444', 'qq': '444', 'email': '444'}
    ]
    card = {'name': 'lisi', 'phone': '222', 'qq': '222', 'email': '222'}
    new_cards = del_cards(cards, card)
    print(new_cards)
