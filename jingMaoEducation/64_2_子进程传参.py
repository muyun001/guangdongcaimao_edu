# 向子进程中传参
import os
import time
import random
from multiprocessing import Process


# 子进程要执行的代码
def run1(text):
    print("2--run函数中的进程id是：{}, 它的父进程是{}".format(os.getpid(), os.getppid()))
    for i in range(10):
        print("{}{}".format(text, i))
        time.sleep(random.random() * 2)


# 子进程要执行的代码
def run2(text):
    print("3--run1函数中的进程id是：{}, 它的父进程是{}".format(os.getpid(), os.getppid()))
    for i in range(10):
        print("- {}-{}".format(text, i))
        time.sleep(random.random() * 2)


if __name__ == '__main__':
    print("程序开始运行，开启一个进程，进程id是：", os.getpid())

    process1 = Process(target=run1, args=("run1test",))
    process2 = Process(target=run2, args=("run2test",))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print("两个子进程都运行完毕")
