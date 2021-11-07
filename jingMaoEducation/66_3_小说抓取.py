# 抓取笔趣阁的小说"剑来"
import os
import time
import logging
import requests
from lxml import etree
from functools import reduce
from multiprocessing import Pool

FILE_PATH = "66_小说抓取_剑来.txt"

HEADER = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": 'Hm_lvt_cc13cd690e17410a96647c14d9e29aba=1634483176; Hm_lvt_a6e0e6155afbc85db439c009f957f6d4=1634483176; jieqiVisitId=article_articleviews%3D83997; PHPSESSID=qru29vkfsnc9n565dmvm9dmqfc; jieqiUserInfo=jieqiUserId%3D48687%2CjieqiUserUname%3D18914820987%2CjieqiUserName%3D%C4%BD%D4%C6001%2CjieqiUserGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUserHonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserPassword%3De10adc3949ba59abbe56e057f20f883e%2CjieqiUserUname_un%3D18914820987%2CjieqiUserName_un%3D%26%23x6155%3B%26%23x4E91%3B001%2CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1634483825; jieqiVisitInfo=jieqiUserLogin%3D1634483825%2CjieqiUserId%3D48687; jieqiVisitTime=jieqiArticlesearchTime%3D1634483931; clickbids=83997; Hm_lpvt_cc13cd690e17410a96647c14d9e29aba=1634483932; Hm_lpvt_a6e0e6155afbc85db439c009f957f6d4=1634483932',
    "if-none-match": "1634483559|48686",
    "referer": "https://www.bbiquge.net/",
    "sec-ch-ua": '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari / 537.36",
}
# 通过下面的方式进行简单配置输出方式与日志级别
logging.basicConfig(filename='66_小说抓取_logger.log', level=logging.INFO)


def crawl_urls():
    """抓取每个章节的url, title"""
    url = "https://www.bbiquge.net/book_83999/"
    try:
        response = requests.get(url, headers=HEADER, timeout=5)
        # response.encoding = "gbk"
        # html = response.content.decode("utf-8")
        if response.status_code != 200:
            raise requests.ConnectionError("链接出错， 状态码：", response.status_code)
        tree = etree.HTML(response.text)
        tag_as = tree.xpath("//dd/a")
        urls = list(map(lambda a: "https://www.bbiquge.net/book_83999/" + a.xpath("./@href")[0], tag_as))
        titles = list(map(lambda t: t.xpath("./text()")[0], tag_as))

        # 两个列表组成一个字典
        return dict(zip(titles, urls))
    except Exception as e:
        print(e)
        return {}



def crawl_content(title, url):
    """抓取小说内容"""
    print("开始抓取:", title)
    try:
        response = requests.get(url, headers=HEADER, timeout=5)
    except Exception as e:
        print(f"抓取{title}时报错：{e}, url:{url}")
        return -1
    if response.status_code != 200:
        print("抓取内容时，状态码错误！状态码:{}, url：{}".format(response.status_code, url))
        return -1

    if response.encoding != "utf-8":
        text = response.text.encode("utf-8").decode("utf-8")
    else:
        text = response.text
    tree = etree.HTML(text)
    try:
        con_list = tree.xpath("//div[@id='content']//text()")
        content = reduce(lambda x, y: x + y, con_list)
    except Exception as e:
        print(f"title:{title},url:{url}, 解析时报错：{e}")
        with open(f"66_{title.txt}", "w", encoding="utf-8") as f:
            f.write(response.text)
        return -2
    return {title: content.replace("    ", "").replace("笔趣阁 www.bbiquge.net，最快更新剑来最新章节！", "")}


def run():
    # pool = Pool(5)
    title_url_dicts = crawl_urls()
    if not title_url_dicts:
        print("解析到的内容为空，程序即将退出！")
        exit()
    file = open(FILE_PATH, "w")
    wrong_title = []
    for title, url in title_url_dicts.items():
        # pool.apply_async(crawl_content, )
        try:
            title_content_dict = crawl_content(title, url)
            if title_content_dict == -1 or title_content_dict == -2:
                wrong_title.append(title)
                continue
        except Exception as e:
            print(f"抓取{title}时出现报错:{e}")
        finally:
            try:
                file.write(list(title_content_dict.keys())[0] + "：" + list(title_content_dict.values())[0] + "\n")
            except Exception as e:
                print(f"title:{title},写入数据时报错：{e}")
                file.write(f"{title}: {title_content_dict}\n")
            time.sleep(2)
    file.close()


if __name__ == '__main__':
    run()
    # # d = {"title": "url"}
    # # with open("text.txt", "w") as f:
    # #     f.write(list(d.keys())[0] + list(d.values())[0])
    # # print(list(d.values())[0])
    # title_content = crawl_content("第二百七十一章 宁姑娘，对不起", "https://www.bbiquge.net/book_83999/37560805.html")
    # print(title_content)
