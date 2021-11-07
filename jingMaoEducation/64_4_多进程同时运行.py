import os
import time
import random
from multiprocessing import Process


# 子进程要执行的代码
def run(text):
    print("目前运行的进程是{}, 进程id是：{}, 它的父进程是{}".format(text, os.getpid(), os.getppid()))
    for i in range(10):
        print("{}-{}".format(text, i))
        time.sleep(random.random() * 5)


if __name__ == '__main__':
    print("程序开始运行，开启一个进程，进程id是：", os.getpid())
    process1 = Process(target=run, args=("子进程1",))
    process2 = Process(target=run, args=("子进程2",))
    process3 = Process(target=run, args=("子进程3",))
    process4 = Process(target=run, args=("子进程4",))
    process5 = Process(target=run, args=("子进程5",))
    process6 = Process(target=run, args=("子进程6",))
    process7 = Process(target=run, args=("子进程7",))
    process8 = Process(target=run, args=("子进程8",))
    process9 = Process(target=run, args=("子进程9",))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    process9.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
    process9.join()
    print("所有的子进程都运行完毕")
