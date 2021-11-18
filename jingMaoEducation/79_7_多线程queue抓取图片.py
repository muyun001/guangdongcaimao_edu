import queue
import time
import requests
import threading
from lxml import etree


def crawl_save_imgs(img_src_queue: queue.Queue):
    """解析图片的url"""
    while True:
        img_src = img_src_queue.get()
        print(img_src)
        img_name = img_src.split("/")[-1]
        resp = requests.get(img_src)
        with open(f"./79_多线程queue抓取图片/{img_name}", "wb") as f:
            f.write(resp.content)

        if img_src_queue.empty():
            break


def crawl_img_urls(page_url_queue: queue.Queue, img_src_queue: queue.Queue):
    """获取图片的链接"""
    while True:
        page_url = page_url_queue.get()
        resp = requests.get(page_url)
        tree = etree.HTML(resp.text)
        srcs = ["https:" + src for src in tree.xpath('//ul[@class="ali"]//img/@src')]
        for src in srcs:
            img_src_queue.put(src)
        if page_url_queue.empty():
            break

def run():
    page_url_queue = queue.Queue()
    img_src_queue = queue.Queue()
    for i in range(1, 200 + 1):
        page_url = f"https://www.ivsky.com/tupian/index_{i}.html"
        page_url_queue.put(page_url)

    # 创建5个生产者线程
    for i in range(5 + 1):
        t = threading.Thread(target=crawl_img_urls, args=(page_url_queue, img_src_queue))
        t.start()

    # 创建4个消费者线程
    for i in range(4 + 1):
        t = threading.Thread(target=crawl_save_imgs, args=(img_src_queue,))
        t.start()



if __name__ == '__main__':
    print("程序开始")

    start_time = time.time()
    run()
    end_time = time.time()

    # print(f"图片抓取完成，耗时：{end_time - start_time}秒")

