# 抓百度首页

import requests

url = "http://www.baidu.com"

response = requests.get(url)

if response.status_code != 200:
    print("抓取失败！返回状态码为{}, 即将退出程序！", response.status_code)
    exit()

# print(response.text)
# str.decode("utf-8") 讲byte格式解码为utf-8格式
print(response.content.decode("utf-8"))
with open("baidu.html", "w") as f:
    f.write(response.content.decode("utf-8"))
print("写入文件成功！")

# response.close()