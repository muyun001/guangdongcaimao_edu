"""
进程池
参考教程：https://blog.csdn.net/u013842501/article/details/117717200
"""
import time
from concurrent.futures import ProcessPoolExecutor


def task(sleep_sec=10, tag='test'):
    print('[%s] start sleep' % tag)
    time.sleep(sleep_sec)
    print('[%s] finish sleep' % tag)
    return 100


def main():
    process_pool = ProcessPoolExecutor(max_workers=3)
    future = process_pool.submit(task, 3, tag='TEST')
    ret = future.result()
    print('result is %s' % str(ret))
    process_pool.shutdown()


if __name__ == '__main__':
    main()
