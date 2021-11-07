"""递归函数"""
"""
什么是递归？ -- 分而治之
假如我们有这样一个问题A，
如果能把A分解成一系列比A更容易解决的子问题（A0，A1，A2……An），
通过解决子问题（A0，A1，A2……An）来最终达成解决问题A，这个就是「分而治之」

比如：阶乘
如果想计算阶乘：n! = 1 * 2 * 3 * ... * n  =  n * n-1 * n-2 * ... * 2 * 1
分解问题：
    n！= n * (n-1)!
    n! = n * (n-1) * (n-1-1)!
    n! = n * (n-1) * (n-1-1) * (n-1-1-1)!
    ...
    n! = n * (n-1) * (n-1-1) * (n-1-1-1)! * ... 3
    n! = n * (n-1) * (n-1-1) * (n-1-1-1)! * ... 3 * 2
    n! = n * (n-1) * (n-1-1) * (n-1-1-1)! * ... 3 * 2 * 1
"""

"""
计算5的阶乘：
5!
5 * 4！
5 * (4 * 3！)
5 * (4 * (3 * 2！))
5 * (4 * (3 * (2 * 1！)))

5 * (4 * (3 * (2 * 1)))
5 * (4 * (3 * 2))
5 * (4 * 6)
5 * 24
120
"""


def jiecheng(n):
    """
    实现整数的阶乘
    :param n: 整数值
    :return:  阶乘的结果
    """
    # n=1的时候比较例外
    if n == 1:
        return 1
    return n * jiecheng(n - 1)


result = jiecheng(5)
print(result)

########################################################################
"""
计算整数的累加
"""


def leijia(n):
    """
    实现整数的累加
    :param n: 整数值
    :return: 累加的结果
    """
    if n == 1:
        return 1
    return n + leijia(n - 1)


result2 = leijia(5)
print(result2)

"""
测试：
斐波那契数列：
0、1、1、2、3、5、8、13、21、34、55、89、144、233、377、610、987、
1597、2584、4181、6765、10946、17711、28657、46368…

它的规律是：这个数列从第 3 项开始，每一项都等于前两项之和。
F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n≥2，n∈N*）
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(10))

"""
通用概括一下，在面对递归问题时，我们可以用「分而治之」的概念去帮助理解。步骤如下：
1。把问题分解成更容易解决的子问题集合，比如可以把计算斐波那契数列的第n项问题分解转换成计算第n-1项加上第n-2项这两个子问题
2。假设我们有一个函数可以应用在所有的子问题上，比如计算斐波那契数列的fib函数
3。基于步骤2的函数，实现如何把子问题的解拼成最终问题的解，这就是递归部分，
在计算斐波那契数列的例子里，就是fib(n-1) + fib(n-2)部分，
4。递归部分确定了，然后再考虑子问题最终简化到到最底层时该返回什么值。（即n=0时值为0，n=1时值为1）
"""

"""
实现字符串翻转
abcdefg
"""


# print("".join(reversed(s)))

# f + bcdefg的翻转
# print(s[-1] + s[:-1])
# f + g + bcdef的翻转

def reverse(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse(s[:-1])


s = "abcdef"
print(reverse(s))

# 有学生提出另一种思路
# def reverse2(num):
#     print(s[num], end="")
#     if num == -len(s):
#         return ""
#     return reverse2(num - 1)
#
# print(reverse2(-1))

print("-------------- 字符串翻转 ----------------")
s = "abcdef"
new_s = ""
index = 0


def reverse(s):
    global new_s, index

    print("s:{} -- len(s):{}".format(s, len(s)))
    print("s[-1]：{} -- s[0:-1]：{}".format(s[-1], s[0:-1]))

    if len(s) == 1:
        return s

    index += 1
    print("index:", index)

    new_s = s[-1] + reverse(s[0:-1])

    print("new_s:", new_s)

    return new_s


print(reverse(s))


















