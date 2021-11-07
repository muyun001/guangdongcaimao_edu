"""
"进程和程序的关系"

想象一位有一手好厨艺的计算机科学家正在为他的女儿烘制生日蛋糕。
他有做生日蛋糕的食谱，厨房里有所需的原料：面粉、鸡蛋、糖、香草汁等等。
在这个比喻中，做蛋糕的食谱就是程序(即用适当形式描述的算法)，计算机科学家就是处理机(CPU)，而做蛋糕的各种原料就是输入数据。
** 进程就是厨师阅读食谱、取来各种原料、以及烘制蛋糕的一系列动作的总和。**

现在假设计算机科学家的儿子哭着跑了进来，说他被一只蜜蜂螫了。
计算机科学家就记录下他照着食谱做到哪儿了(保存进程的当前状态)，然后拿出一本急救手册，按照其中的指示处理螫伤。
这里，我们看到处理机从一个进程(做蛋糕)切换到另一个高优先级的进程(实施医疗救治)，每个(进程)拥有各自的程序(食谱和急救书)。
当蜜蜂螫伤处理完之后，计算机科学家又回来做蛋糕，从他离开时的那一步继续做下去。

这里的关键思想是：一个进程是某种类型的一个活动，它有程序、输入、输出、及状态。
单个处理机被若干进程共享，它使用某种调度算法决定何时停止一个进程的工作，并转而为另一个进程提供服务。
"""

import os
import time
import random
from multiprocessing import Process


# 子进程要执行的代码
def run():
    print("2--run函数中的进程id是：{}, 它的父进程是{}".format(os.getpid(), os.getppid()))
    # print("text:{}".format("text"))
    for i in range(10):
        print(i)
        time.sleep(random.random() * 2)


# 子进程要执行的代码
def run1():
    print("3--run1函数中的进程id是：{}, 它的父进程是{}".format(os.getpid(), os.getppid()))
    # print("text:{}".format("text"))
    for i in range(10):
        print(-i)
        time.sleep(random.random() * 2)


if __name__ == '__main__':
    # 当你运行一个程序的时候，你就启动了一个进程
    # os.getpid()是获取当前进程到id
    print("程序开始运行，开启一个进程，进程id是：", os.getpid())

    # 使用此进程运行run函数
    # process = Process(run())
    # process.start()

    # 创建一个子进程，运行run函数
    process = Process(target=run)
    # 再创建一个子进程，运行run1函数
    process1 = Process(target=run1)
    # 两个子进程开始运行
    process.start()
    process1.start()
    process.join()  # 等待子进程运行结束
    process1.join()  # 等待子进程运行结束
    print("两个子进程都运行结束")
