import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def spider(i, j):
    time.sleep(random.random() * 5)
    return i, j


def run_demo1():
    with ThreadPoolExecutor(max_workers=5) as t:
        tasks = [t.submit(spider, i=i, j=1) for i in range(1, 5)]

        # as_completed():每当有一个线程完成任务，会自动用t.result()获取返回结果
        for t in as_completed(tasks):
            data = t.result()
            print(data)


def demo2():
    """测试线程池是否有效。本以为会运行10次，其实只运行了1次"""
    for i in range(10):
        print(i)


def run_demo2():
    with ThreadPoolExecutor(10) as t:
        t.submit(demo2)


if __name__ == '__main__':
    # run_demo1()
    run_demo2()
