# 字典dict

# 初始化字典
dict_data = {6: 9, 10: 5, 3: 11, 8: 2, 7: 6}
print(dict_data)
print(dict_data.items())

# 对字典按值（value）进行排序（默认由小到大）
# test_data_3 = sorted(dict_data.items(), key=lambda x: x[0], reverse=False)
# print(test_data_3)

# 对列表中第一个元素相同的归类，放到dict中
# Message = [[2, 'Mike'], [1, 'Jone'], [2, 'Marry']]
# dict1 = {}
# for number in Message:
#     value = number[0]
#     if value not in dict1.keys():
#         dict1[value] = [number]  # 此句话玄机
#     else:
#         dict1[value].append(number)
# print(dict1)


# list列表
name = ["张三", "李四", "王武", "小明", "小红", "小王"]
age = [19, 18, 34, 33, 22, 13]

for i in range(len(name)):
    if name[i] == "小红":
        print(i)
print(age[4])


# 字典 dict
# key:value 键值对
info = {"张三": 19, "李四": 18, "王武": 34, "小明": 33, "小红": 22, "小王": 13}
print(info["小红"])

print("--------------------------  判断字典中是否含有某key值   ----------------------")
# 判断字典中是否含有某key值
print(info["李四"])
print(info.get("李四", -1))

print("--------------------------   对字典的key进行遍历  ----------------------------")
# 对字典对key进行遍历
for name in info.keys():
    print(name)

print("--------------------------   对字典的value值进行遍历  ------------------------")
# 对字典对value值进行遍历
for age in info.values():
    print(age)

print("--------------------------   对字典的键值对进行遍历  --------------------------")
# 对键值对进行遍历
for name, age in info.items():
    print(name)
    print(age)

info = {"张三": 19, "李四": 18, "王武": 34, "小明": 33, "小红": 22, "小王": 13}
print("--------------------------  对字典进行修改   ----------------------------")
# 对字典进行修改
for name, age in info.items():
    if name == '李四':
        age = 22  # 这样行不行？
print(info)

for name, age in info.items():
    if name == '李四':
        info[name] = 22
print(info)

# 将年龄小于18岁的都改为18岁
for name, age in info.items():
    if age < 18:
        info[name] = 18
print(info)

print("------------------------- popitem() -------------------")

info = {"小王": 13, "张三": 19, "李四": 18, "王武": 34, "小明": 33, "小红": 22}
info = info.popitem()
print(info)

# students_info = {
#     "张三": {
#         "性别": "男",
#         "": "",
#     }
# }
#
