import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def spider(i):
    time.sleep(random.random() * 5)
    return i


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as t:
        tasks = [t.submit(spider, i) for i in range(1, 5)]

        # as_completed():每当有一个线程完成任务，会自动用t.result()获取返回结果
        for t in as_completed(tasks):
            data = t.result()
            print(data)
