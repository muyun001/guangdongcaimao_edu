# 站长之家简历模版下载
import requests
from lxml import etree


def run():
    url = "https://sc.chinaz.com/jianli/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    response.encoding = response.apparent_encoding
    tree = etree.HTML(response.text)
    # jianli_tags = tree.xpath("//div[@class='box col3 ws_block masonry-brick']")
    jianli_tags = tree.xpath("//div[@class='box col3 ws_block']")  # todo 讲解
    print(jianli_tags)
    # for tag in jianli_tags:
    #     href = tag.xpath("./a/@href")[0]
    #     title = tag.xpath("./a/img/@alt")[0]
    #     print(title, href)


if __name__ == '__main__':
    run()
    # with open("60_5简历模版.html", "r", encoding="utf-8") as f:
    #     html = f.read()
    # tree = etree.HTML(html)
    # jianli_tags = tree.xpath("//div[@class='box col3 ws_block']")  # 需要改
    # print(jianli_tags)
