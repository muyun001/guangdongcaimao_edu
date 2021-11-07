"""
作业，抓取肯德基店铺【url = "http://www.kfc.com.cn/kfccda/storelist/index.aspx"】
范围：整个广东省
保存到csv文件中
"""

import requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

data = {
    "cname": "",
    "pid": "",
    "keyword": "清远",
    "pageIndex": 1,
    "pageSize": 10,
}

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}


# 开始运行
def run():
    response = requests.post(url=url, data=data, headers=header)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    data_json = json.loads(response.text)
    # print(data_json)
    store_list = data_json["Table1"]
    for store in store_list:
        print(store)


if __name__ == "__main__":
    run()
