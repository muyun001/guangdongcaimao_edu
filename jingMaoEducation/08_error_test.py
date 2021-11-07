# 异常

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("错误的参数类型！")
    if x > 0:
        return x
    else:
        return -x


print(my_abs(1))


def aa():
    return 1, 3


a = aa()
print(a[1])
print(type(a))

#################################################################

import math


def quadratic(a, b, c):
    """
    求ax^2 + bx +c =0的两个解。
    求平方根的函数：math.sqrt()
    求解方法：x = [-b+-根号下（b^2-4ac）] / 2a
    """
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


print(quadratic(2, 3, 1))


#####################################################################################

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll("zhangsan", "Fefale", 9, "guangdong")


#################################################################

def add_end(L=list()):
    L.append('END')
    return L


# 最好改写成这种
def add_end(L=None):
    if L is not None:
        L = list()
    L.append("END")
    return L


print(add_end([]))


#################################################################
def calc(*numbers):
    print(type(numbers))
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))

#################################################################

import random
print("random:")
print(random.randint(0, 8))  # 随机整数
print(random.randrange(0, 8))  # 随机整数
