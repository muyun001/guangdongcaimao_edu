import time
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def download_pic(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    tree = etree.HTML(resp.text)
    src_list = tree.xpath('//ul[@class="ali"]/li/div/a/img/@src')
    for src in src_list:
        img_url = 'https:' + src
        img_content = requests.get(img_url, headers=headers).content
        img_name = src.split('/')[-1]
        with open('./66_img/' + img_name, 'wb') as fp:
            fp.write(img_content)
    fp.close()


if __name__ == '__main__':
    # 创建线程池
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 20):
            # 把下载任务提交给线程池
            print(i)
            t.submit(download_pic, f"https://www.ivsky.com/tupian/index_{i}.html")

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("全部下载完毕!")