# xpath解析
import requests
from lxml import etree


def main():
    url = "https://qingyuan.58.com/ershoufang/?PGTID=0d100000-01c8-7413-5501-bb2c79957f06&ClickID=4"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36", }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    tree = etree.HTML(response.text)
    urls = tree.xpath("//section[@class='list']//div[@class='property']/a/@href")  # 解析所有住房链接
    for url in urls:
        print(url)
    titles = tree.xpath("//div[@class='property-content-title']/h3/@title")  # 解析所有标题
    for title in titles:
        print(title)
    print(len(urls), len(titles))


if __name__ == '__main__':
    main()
