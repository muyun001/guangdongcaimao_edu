import time
import queue
import random
import requests
import threading
from lxml import etree

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(50)]


def crawl(url):
    """生产者"""
    response = requests.get(url)
    return response.text


def parse(html):
    """消费者"""
    tree = etree.HTML(html)
    titles = tree.xpath('//a[@class="post-item-title"]//text()')
    urls = tree.xpath('//a[@class="post-item-title"]//@href')
    return dict(zip(titles, urls))


def do_crawl(url_queue: queue.Queue, html_queue: queue.Queue):  # 也可以不指定格式：url_queue, html_queue
    while True:
        url = url_queue.get()
        print(f"crawl, {url}")
        html = crawl(url)
        html_queue.put(html)
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, file):
    while True:
        html = html_queue.get()
        results = parse(html)
        for title, url in results.items():
            file.write(f"{title}:{url}\n")
            print(f"parse, {title}:{url}\n")

        time.sleep(random.randint(1, 2))
        # 若列表为空，则退出
        if html_queue.empty():
            break


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in urls:
        url_queue.put(url)

    # 创建3个生产者线程
    for i in range(3):
        t = threading.Thread(target=do_crawl, args=(url_queue, html_queue))
        t.start()

    file = open("66_1_生产者消费者抓取测试.txt", "w")
    # 创建2个消费者线程
    for i in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, file))
        t.start()
