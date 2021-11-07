# 如果在list最后再加个"tom",先做做试试
a_list = ["a", "v", "c", "d", "tom", "f", "tom"]
b_list = ["a", "v", "c", "d", "jack", "f", ]

# 课后作业讲解：
for i in range(len(a_list)):
    if a_list[i] == "tom":
        a_list.remove(a_list[i])
        break
print(a_list)

for i in a_list:
    if i == "tom":
        a_list.remove(i)
print("a_list:", a_list)

a = 0
while a < len(b_list):
    if b_list[a] == "jack":
        b_list[a] = "jackson"
    a += 1
print("b_list:", b_list)

# 列表新增知识点：
f = [i for i in range(2)]
print(f)
f = [i for i in range(10) if i != 5]
print(f)
f = [[i, i + 1] for i in range(10)]
print(f)

f = ["a", "b", "c", "d"]
for index, data in enumerate(f):
    if f[index] == "c":
        print("此时索引是：", index)

#####

# a = [1, 2, 3, 4, 5]
# # 报错,越界异常 IndexError: list index out of range
# for i in range(len(a)):
#     if a[i] == 3:
#         a.remove(a[i])
# print(a)

# 解决思路1
# 复制一个新的变量，使用新的变量遍历，删除原变量的元素
a = [1, 2, 3, 4, 5]
b = a
print("id(a)", id(a))
print("id(b)", id(b))

import copy

b = copy.copy(a)
print("id(a)", id(a))
print("id(b):", id(b))

print("b:", b)  # [1, 2, 3, 4, 5]
for i in range(len(b)):
    if b[i] == 3:
        a.remove(b[i])
print("解决思路1:", a)

# 解决思路2
# 不用索引遍历，直接遍历元素
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        a.remove(i)
print("解决思路2:", a)

# 解决思路3
# 列表解析式
a = [1, 2, 3, 4, 5]
b = list()
for i in a:
    if i != 3:
        b.append(i)
a = b
print("解决思路3.1:", a)

# 可以写为
a = [i for i in a]

a = [i for i in a if i != 3]
print("解决思路3.2:", a)

# print(list(map(lambda x: x * x, [1, 2, 3])))

#
# f = lambda a: map(lambda b: a[b:b + 3], range(0, len(a), 3))
# print(f)

print("-------------------- 元组和列表之间的转换 ------------------")
# 列表转换元组
num_list = [1, 2, 3, 4, 5]
num_tuple = tuple(num_list)
print("type(num_tuple):", type(num_tuple))  # type(num_tuple): <class 'tuple'>
print("num_tuple:", num_tuple)  # num_tuple: (1, 2, 3, 4, 5)

# 元组转换列表
num_tuple_01 = (1, 2, 3, 4, 5)
num_list_01 = list(num_tuple_01)
print(type(num_list_01))  # <class 'list'>
print(num_list_01)  # [1, 2, 3, 4, 5]

q = (1,)
print("type(q):", q)
