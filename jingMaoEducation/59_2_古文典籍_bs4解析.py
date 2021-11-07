# 古文典籍，使用bs4解析
# http://www.gushiju.org/book/
import requests
from bs4 import BeautifulSoup


def main():
    url = "http://www.gushiju.org/book/"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    # 解析
    soup = BeautifulSoup(response.text, "lxml")
    tagas = soup.select(".left li strong a")
    hrefs = ["gushiju.org" + a["href"] for a in tagas]
    book_names = [a.text for a in tagas]
    print(hrefs)
    print(book_names)
    
    # 可以继续向深处抓取书籍内容


if __name__ == '__main__':
    main()
