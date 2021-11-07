# while循环小题讲解
"""
1、求1～100所有整数的累加值
2、求1～100所有偶数的累加值
3、找出100～999所有的吉利数字：111 222 333...999，123 234 345 ... 987 876 765
    思路：
        1、取整 取余
        2、字符串拆分
"""

"""
1、求1～100所有整数的累加值
思路：
    1）设置变量a，使a从0开始+1，一直加到100
    2）设置变量sum_number，a每增加1，就让a加到sum中去
    3）输出最终到sum_number值
"""

a, sum_number = 0, 0

while a <= 99:
    a += 1
    sum_number += a
print(sum_number)

"""
a = 0, sum_number += 1
a = 1, sum_number += 2
...
a = 99, sum_ber += 100
a = 100, sum_ber += 101
"""

while a <= 100:
    sum_number += a
    a += 1
print(sum_number)

"""
a = 0, sum_number += 0
a = 1, sum_number += 1
...
a = 100, sum_number += 100
"""

# 第三种不实用循环的实现方法：
print(sum(range(0, 101)))

########################################################################
"""
2、求1～100所有偶数的累加值
思路1：
    1）设置变量a，使a从0开始+1，一直加到100
    2）设置变量sum_number,当a是偶数时，讲a加到sum_number中
    3）输出sum_number的值
"""
a, sum_number = 0, 0

while a <= 100:
    if a % 2 == 0:
        print(a)
        sum_number += a
    a += 1
print(sum_number)

"""
2、求1～100所有偶数的累加值
思路2：
    1）设置变量a，使a从0开始+2，一直加到100
    2）设置变量sum_number，a每增加2，就让a加到sum中去
    3）输出最终到sum_number值
"""
while a <= 100:
    sum_number += a
    a += 2
print(sum_number)

"""
3、找出100～999所有的吉利数字：111 222 333...999，123 234 345 ... 987 876 765
    思路：
        1、取整 取余
        2、字符串拆分
    思路：
        1）设置变量a，使a从100，自+1，一直加到999
        2）判断是不是吉利数字，如果是，就输出
            1：分别摘出百位数、十位数、个位数的值 【
                两种方式：1取整取余，2字符串拆分
            2：111、123、321
                111情况判断：百位 = 十位 = 个位
                123情况判断：假如以百位数为基准，那么十位数=百位数+1，个位数=百位数+2。
                321情况判断：假如以百位数为基准，那么十位数=百位数-1，个位数=百位数-2。
"""

# 123取百位数
print("123 // 100 =", 123 // 100)
# 取十位数
print("123 // 10 =", 123 // 10)
print("12 % 10 =", 12 % 10)
# 取个位数
print("123 % 10 =", 123 % 10)

# 方法一，使用取整取余处理
a = 100
while a <= 999:
    bai = a // 100
    shi = a // 10 % 10
    ge = a % 10

    """
    111情况判断：百位 = 十位 = 个位
    123情况判断：假如以百位数为基准，那么十位数=百位数+1，个位数=百位数+2。
    321情况判断：假如以百位数为基准，那么十位数=百位数-1，个位数=百位数-2。
    """
    if bai == shi == ge:
        print(a)
    elif (shi == bai + 1) and (ge == bai + 2):
        print(a)
    elif (shi == bai - 1) and (ge == bai - 2):
        print(a)
    a += 1

# 方法二：使用字符串处理
a = 100
while a <= 999:
    str_a = str(a)
    bai = int(str_a[0])
    shi = int(str_a[1])
    ge = int(str_a[2])

    if bai == shi == ge:
        print(a)
    elif (shi == bai + 1) and (ge == bai + 2):
        print(a)
    elif (shi == bai - 1) and (ge == bai - 2):
        print(a)
    a += 1
