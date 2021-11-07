# 星号（*）和双星号（**）的使用
# * ：可将列表或元组中的数据直接取出来
# ** ： 可将字典中的数据直接取出来

# import numpy as np
#
# print(np.arange(3, 6))
#
# test_list = np.arange(0, 7)
test_list = [1, 2, 3, 4, 5, 6, 7]
print(test_list)
print(*test_list)

test_dict = {"b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
print(test_dict.get("a", None))
print(test_dict.pop("b"))
print(test_dict.items())
print(test_dict)

####################################################################


# def test_one(a, *b):
#     """a是一个普通传入参数，*b是一个非关键字星号参数"""
#     print(a)
#     print(b)
#
#
# test_one(1, 2, 3, 4, 5, 6)
#
#
# def test_two(a, **b):
#     """a是一个普通关键字参数，**b是一个关键字双星号参数
#     (a=1,**b)
#     (a=1,b=2, c=3, d=4, e=5, f=6)
#     **b = (b=2, c=3, d=4, e=5, f=6)
#     **b = {"b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
#     """
#     print(b)
#
#
# test_two(a=1, b=2, c=3, d=4, e=5, f=6)
