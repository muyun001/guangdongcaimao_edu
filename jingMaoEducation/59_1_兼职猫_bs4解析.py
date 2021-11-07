# 兼职猫数据抓取，并使用bs4解析
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://guangzhou.jianzhimao.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    # 解析
    soup = BeautifulSoup(response.text, "lxml")
    tag_as = soup.select(".content_list_box li a.left")
    hrefs = ["https://guangzhou.jianzhimao.com/" + a["href"] for a in tag_as]
    titles = [a["title"] for a in tag_as]
    print(hrefs)
    print(titles)


if __name__ == '__main__':
    main()
