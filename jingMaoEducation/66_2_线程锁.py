"""
因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
也就是可以看成：
x = balance + n
balance = x

由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
初始值 balance = 0

t1: x1 = balance + 5 # x1 = 0 + 5 = 5
t1: balance = x1     # balance = 5
t1: x1 = balance - 5 # x1 = 5 - 5 = 0
t1: balance = x1     # balance = 0

t2: x2 = balance + 8 # x2 = 0 + 8 = 8
t2: balance = x2     # balance = 8
t2: x2 = balance - 8 # x2 = 8 - 8 = 0
t2: balance = x2     # balance = 0

结果 balance = 0

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2      # balance = -8

结果 balance = -8

究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
所以需要给change_it()上锁，在同一时间只允许一个线程运行此函数。
"""
import threading
import time
import random

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

# 给change_it()加锁
def run_thread(n):
    for i in range(100000):
        lock.acquire()

        # 上锁之后一定要释放锁，不然等待锁的线程会成为死线程。
        # 使用try...finally...来确保锁一定会被释放
        try:
            change_it(n)
        finally:
            lock.acquire()

"""
注意加锁的位置：
如果是
try:
        # 此处加锁
        lock.acquire()
        for i in range(100000):
            change_it(n)
    finally:
        # 改完了一定要释放锁:
        lock.release()
那么循环100000次结束前别人都拿不到锁，如果循环100000次要10秒，那其他拿锁线程就必须等10秒，
就是你独享完成后，给别人，就是你要循环200000万后，才轮到别人。
循环内了话，只锁一次，也就是change_it(n)可能会交替进行。
"""

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
