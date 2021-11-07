"""
作业，抓取药监局企业信息【http://scxk.nmpa.gov.cn:81/xk/】
保存到csv文件中
"""

import requests
import json

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}


def spider():
    """抓取程序"""

    com_ids = spider_comids()
    spider_cominfo_write(com_ids)


def spider_comids():
    """抓取公司的id"""
    comids = list()
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    data = {
        "on": "true",
        "page": 2,  # 可修改页数
        "pageSize": 15,
        "productName": "",
        "conditionType": 1,
        "applyname": "",
        "applysn": "",
    }
    response = requests.post(url=url, data=data, headers=HEADER)
    # response = requests.get(url=url, params=data, headers=HEADER)
    if response.status_code != 200:
        print("访问失败，返回状态码{}，程序即将退出！".format(response.status_code))
        exit()

    if not response.text:
        print("抓到的结果为空，程序即将退出！")
        exit()

    data_json = json.loads(response.text)
    # print(data_json)
    store_list = data_json["list"]
    for store in store_list:
        com_id = store["ID"]
        comids.append(com_id)
    return comids


def spider_cominfo_write(ids):
    """抓取公司信息并写入文件"""
    com_infos = list()
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    data = {"id": ""}

    f = open("55_药监局企业信息.txt", "w", encoding="utf-8")

    for id in ids:
        data["id"] = id
        response = requests.post(url=url, data=data, headers=HEADER)
        if response.status_code != 200:
            print("访问失败，返回状态码{}".format(response.status_code))
            com_infos.append("访问失败，返回状态码{},公司id是：{}".format(response.status_code, id))
            continue

        # info_json = json.loads(response.text)
        f.write(response.text + "\n")
        print("企业信息写入成功", response.text)
    f.close()


# 开始运行
def main():
    spider()


if __name__ == "__main__":
    main()
    # data = {"id": ""}
    # data["id"] = "bbbbb"
    # print(data)
