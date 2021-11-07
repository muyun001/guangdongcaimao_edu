"""
多进程间通信
Process之间是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
"""

import os
import random
import time
from multiprocessing import Process, Queue


def write(queue):
    """向队列中写入数据"""
    print('写入的进程: {}'.format(os.getpid()))
    for value in range(20):
        print('将值 {} 添加到队列中...'.format(value))
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    """从队列中读取数据"""
    print('读取的进程: {}'.format(os.getpid()))
    while True:
        value = queue.get(True)
        print('从队列中读取{}'.format(value))
        time.sleep(random.random() * 2)
        # 读取速度比写入速度慢的情况下，可以加入下列语句。
        if queue.empty():
            break


if __name__ == '__main__':
    print("程序开始运行，开启一个进程，进程id是：", os.getpid())
    # 父进程创建Queue，并传给各个子进程：
    queue = Queue()
    process_write = Process(target=write, args=(queue,))
    process_read = Process(target=read, args=(queue,))
    # 启动子进程pw，写入:
    process_write.start()
    # 启动子进程pr，读取:
    process_read.start()
    # 等待pw结束:
    process_write.join()

    # 如果某个进程是死循环，强行终止的方法:
    # process_read.terminate()
