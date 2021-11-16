import requests
import time
import threading

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(50)]


def crawl(url):
    response = requests.get(url)
    print(url, len(response.text))


def single_crawl():
    """单线程抓取"""
    print("开始单线程抓取")
    for url in urls:
        crawl(url)
    print("结束单线程抓取")


def multi_crawl():
    """多线程抓取"""
    print("开始多线程抓取")
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=crawl, args=(url,)))  # 参数必须是元组

    # 把每个线程启动
    for thread in threads:
        thread.start()

    # 等待每个线程
    for thread in threads:
        thread.join()
    print("结束多线程抓取")


if __name__ == '__main__':
    start = time.time()
    single_crawl()
    end = time.time()
    print(f"单线程抓取花了{start - end}秒")

    start = time.time()
    multi_crawl()
    end = time.time()
    print(start - end)
    print(f"多线程抓取花了{start - end}秒")
