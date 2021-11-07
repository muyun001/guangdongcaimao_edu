"""
进程池
"""
import os
import random
import time
from multiprocessing import Pool


def print1(i):
    time.sleep(random.random() * 7)
    print("当前进程id是：", os.getpid(), i)


if __name__ == '__main__':
    print("程序开始运行，开启一个进程，进程id：", os.getpid())
    pool = Pool(5)
    for i in range(20):
        pool.apply_async(print1, args=(i,))
    print("等待执行结束。。。")
    pool.close()  # 关闭pool
    pool.join()  # 等待所有进程执行完毕，再执行下面操作
    print("执行结束")


#############################################################################################
# 另一个例子
def long_time_task(name):
    print('Run task {} ({})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {} runs {time:0.2f} seconds.'.format(name, time=(end - start)))


if __name__ == '__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Pool(9)
    for i in range(12):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
