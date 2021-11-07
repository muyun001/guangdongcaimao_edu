"""
url = "https://www.umei.cc/weimeitupian/"
要求：获取到所有图片的原图，并保存在文件夹"唯美图片"中
    每张图片以它链接最后的"smallxxxxxxxx.jpg命名"
"""
import requests
from bs4 import BeautifulSoup

HEADER = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
}


def crawl_srcs():
    url = "https://www.umei.cc/weimeitupian/"

    response = requests.get(url, headers=HEADER)
    if response.status_code != 200:
        print(f"状态码出错，{response.status_code}, 程序即将退出")
        exit()
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "lxml")
    # xpath: //li/a[@class="TypeBigPics"]/img/@src
    # bs4: a.TypeBigPics img
    return [s["src"] for s in soup.select("a.TypeBigPics img")]


def crawl_imgs(src):
    response = requests.get(src, headers=HEADER)
    img_name = src.split("/")[-1]
    with open("./58_唯美图片/" + img_name, "wb") as f:
        f.write(response.content)
    print("写入图片成功！", src)


def run():
    srcs = crawl_srcs()
    for s in srcs:
        crawl_imgs(s)


if __name__ == '__main__':
    run()
