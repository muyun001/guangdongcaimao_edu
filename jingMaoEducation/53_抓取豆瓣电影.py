# 抓取豆瓣电影

import requests
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/new_search_subjects"
    params = {
        "sort": "U",
        "range": "0, 10",
        "tags": "",
        "start": 0
    }

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }

    response = requests.get(url=url, params=params, headers=header)
    # print(response.request.headers)
    print(response.text)
    res_json = json.loads(response.text)


    # 可以继续在网页端向下刷新抓取，修改"status"
    # 如果把status修改为20，就是抓取下一页的数据，改为40就是再抓取下一页的数据。