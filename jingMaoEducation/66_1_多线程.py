#
import time
import threading
import random


def print1():
    for i in range(10):
        print(i)
        time.sleep(random.random())


def print2():
    for i in range(10):
        print(-i)
        time.sleep(random.random())


def test1():
    print1()
    print2()


def test_pool():
    """线程池测试"""
    t1 = threading.Thread(target=print1)
    t2 = threading.Thread(target=print2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("所有线程都执行完毕")


if __name__ == '__main__':
    # test1()
    test_pool()
