import requests

url = "http://pushplus.hxtrip.com/send"

title = "测试"
content = "我的兼职猫程序搞定了！！！！！！！！"
params = {
    "token": "自己的token",
    "title": title,
    "content": content,
}

response = requests.get(url, params=params)
print(response.text)
