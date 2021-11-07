# xpath解析城市

import requests
from lxml import etree


def main():
    url = "https://www.aqistudy.cn/historydata/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    tree = etree.HTML(response.text)
    li_tags = tree.xpath("//div[@class='all']/div[@class='bottom']//li")
    city_name_list = list()
    for li in li_tags:
        city_href = "https://www.aqistudy.cn/historydata/" + li.xpath("./a/@href")[0]
        city_name = li.xpath("./a/text()")[0]
        city_name_list.append(city_name)
        print(city_name, city_href)


if __name__ == '__main__':
    main()
