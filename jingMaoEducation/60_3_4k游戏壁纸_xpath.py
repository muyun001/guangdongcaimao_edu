# 彼岸图网-4k游戏壁纸
import os
import time
import requests
from lxml import etree

path = "60_4k游戏壁纸"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}


def create_dir(path):
    """创建文件夹"""
    if not os.path.exists(path):
        os.mkdir(path)


def crawl_urls():
    url = "https://pic.netbian.com/4kyouxi/"
    response = requests.get(url, headers=header)
    # 把返回数据的编码格式改为utf-8，但不一定有用
    # response.encoding = "utf-8"
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    # 解析出所有腿片的链接
    tree = etree.HTML(response.text)
    li_tags = tree.xpath('//div[@id="main"]//ul//li')
    for li_tag in li_tags:
        # 在下一次继续进行调用上面的tag对象时，一定要在.xpath()中加个"./"
        src_list = li_tag.xpath("./a/img/@src")
        title_list = li_tag.xpath("./a/b/text()")
        if not len(src_list) and not len(title_list):
            print("解析为空")
            continue
        img_src = "https://pic.netbian.com/" + src_list[0]
        img_name = title_list[0] + ".jpg"
        # 通用处理中文乱码的方式
        img_name = img_name.encode("iso-8859-1").decode("gbk")
        # print(img_name, img_src)
        crawl_imgs(img_name, img_src)
        time.sleep(1)


def crawl_imgs(img_name, img_src):
    # 通过链接抓取每一张图片
    response = requests.get(img_src, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，尝试抓取下一章图片".format(response.status_code))
        return
    with open("./{}/{}".format(path, img_name), "wb") as f:
        f.write(response.content)
        print("下载成功！", img_name)


def main():
    create_dir(path)
    crawl_urls()


if __name__ == '__main__':
    main()
    # gbk_to_utf8()
