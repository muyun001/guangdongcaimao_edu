"""
使用push_plus进行微信消息推送
官网：http://pushplus.hxtrip.com/message
"""
import requests

url = "http://pushplus.hxtrip.com/send"

title = "测试"
content = "我的兼职猫程序搞定了！！！！！！！！"
params = {
    "token": "e71cb823d3564e939a79a06ffc6e9114",
    "title": title,
    "content": content,
}

response = requests.get(url, params=params)
print(response.text)
