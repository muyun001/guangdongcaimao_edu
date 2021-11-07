# 字符串

# join
a_list = ["a", "b", "c", "d", "e"]
print(",".join(a_list))

print("a_list[1:3] =", a_list[1:3])

a_str = "abcde "
print(",".join(a_str))

print("a_str[1:3] =", a_str[1:3])

print(a_str.startswith("a"))
print(a_str.endswith("e"))
print(a_str.find("3"))
# print(a_str.index("3"))
print(a_str.replace("a", "v"))
print(a_str.count("3"))
print(a_str.strip())

b_str = """abcde
fghij"""
print(b_str.split("\n"))
print(b_str.splitlines())

# startswith(),endswith()
a_str = "abcde"
print(a_str.startswith("a"))  # 判断是否以某字符串为开始
print(a_str.endswith("e"))  # 判断是否以某字符串为结尾

# find(),index()，获取元素在列表中的索引
print(a_str.find("v"))  # 返回索引值,若查找不到，则返回-1
# print(a_str.index("v"))  # 查找不到则报错

# len()， 返回字符串长度
a_str = "aaabcde"
print(len(a_str))

# replace()  # 元素替换，可确定替换次数
print(a_str.replace("a", "z", 2))

# strip() ,去除字符串两端的空格
b = " abcde "
print(b.strip())
print(len(b.strip()))
print(b.lstrip())  # left 去除左侧空格
print(b.rstrip())  # right 去除右侧空格

# split()  字符串分割
c = "a.b.c.d.e"
print(c.split("."))
d = """abcde
fghij"""
print(d.split("\n"))
print(d.splitlines())

# join()
a_str = "abcde"
print("，".join(a_str))

print(a_str[3:5])  # 左闭右开，能取到左边，取不到右边
print(a_str[:5])  # :左侧省略时，从0开始取
print(a_str[:])  # :两侧都省略，即从0开始，取到最后一个值
print(a_str[:-1])  # :-1，从0开始，取到倒数第二个值
print(a_str[:-2])  # :-2，从0开始，取到倒数第三个值

# str[1:5:2], 从索引为1的元素，取到索引为5的元素，每两个元素取一个
a_str = "123456789"
b_str = "987654321"
print(a_str[::-2])
print(b_str[::2])
