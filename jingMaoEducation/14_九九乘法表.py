# 99乘法表的实现

"""
使用while循环实现
"""
row = 1  # 行
while row <= 9:
    col = 1  # 列
    while col <= row:
        print("{col} * {row} = {result}".format(col=col, row=row, result=col * row), end="\t")
        col += 1
    print("")
    row += 1

"""
使用for循环实现
第n行，n*其他值
第m列，其他值*m
"""
for i in range(1, 10):  # 行
    for j in range(1, 10):  # 列
        print("{j} * {i} = {result}".format(i=i, j=j, result=i * j), end="\t")
        if i == j:
            print("")
            break

# 优化
for i in range(1, 10):  # 行
    for j in range(1, i + 1):  # 列
        print("{j} * {i} = {result}".format(i=i, j=j, result=i * j), end="\t")
    print("")
