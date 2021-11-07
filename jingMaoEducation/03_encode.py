# encode\unquote

"""
1.导入包
2.提供data
3。编译
4。转换
"""
# from urllib import parse
#
# data = {
#     "kw": "python工程师",
#     "ws": "test",
# }
#
# # encode_str = parse.urlencode(data)
# # print(encode_str)
#
# decode_str = parse.unquote("kw=python%E5%B7%A5%E7%A8%8B%E5%B8%88&ws=test")
# print(decode_str)


##########################################################################################

"""
1。导入包
2。创建Request对象
    1。编码
    2。添加ua
3。发送请求，接收结果
4。打印结果
"""

from urllib import request, parse
import ssl

ua_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
data = {
    "wd": "python工程师",
}
wd = parse.urlencode(data)
url = "http://www.baidu.com/s?" + wd
req = request.Request(url=url, headers=ua_header)
response = request.urlopen(req, context=ssl._create_unverified_context())
req.add_header("Connection", "keep-alive")
html = response.read()
print(html)
