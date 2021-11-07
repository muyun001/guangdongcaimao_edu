# 抓取搜狗首页


import requests

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Cookie": "",
}

if __name__ == "__main__":
    url = "https://www.sogou.com/web"
    param = {
        "query": "手机"
    }

    response = requests.get(url, params=param, headers=header)
    print(response.text)
