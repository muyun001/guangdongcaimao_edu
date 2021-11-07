import pymysql

"""
ip代理
1、什么是ip代理？
    - 代理服务器
2、代理的作用？
    - 突破自身ip访问的限制（如果同一个ip地址持续访问次数过多，容易被禁）
    - 隐藏自身的真是ip地址
3、代理网站
    - 快代理
    - 齐云代理 https://proxy.ip3366.net/free/
    - 小幻代理 https://ip.ihuan.me/
    - 66代理 http://www.66ip.cn/
4、代理ip的类型
    - http:应用到http协议对应到url中
    - https:应用到https协议对应到url中
5、代理ip的匿名度，什么是匿名ip？
    - 透明：服务器知道该请求使用了代理，也知道请求对应到真实ip
    - 匿名：服务器知道使用了代理，不知道真实ip
    - 高匿名：服务器既不知道使用了代理，也不知道真实ip
"""

import requests
import random
import time

ip_proxies = """117.94.222.142:3256
60.167.133.181:1133
111.72.25.212:3256
121.232.148.203:3256
60.167.82.129:1133
182.84.145.73:3256
118.117.189.202:3256
175.7.199.231:3256
60.168.206.165:1133
114.98.114.43:3256
118.117.189.228:3256
121.232.148.165:3256
121.232.148.105:3256
118.117.188.74:3256
118.117.189.237:3256
104.129.198.248:8800
121.232.148.198:3256
178.209.51.218:5836
121.232.148.101:3256
103.211.232.44:53281
113.238.142.208:3128
60.168.206.104:8888
104.129.202.98:8800
117.65.1.143:3256
118.117.188.27:3256
104.129.206.79:8800
117.65.1.249:3256
111.72.25.122:3256
104.129.206.67:8800
117.35.254.27:3000
123.171.42.76:3256
104.129.192.183:8800
104.129.198.143:8800
223.214.219.49:3256
121.230.210.220:3256
121.232.148.193:3256
104.129.198.249:8800
118.117.189.184:3256
118.117.188.170:3256
60.168.207.144:1133
175.7.199.223:3256
182.84.145.172:3256
114.98.114.91:3256
175.7.199.124:3256
175.7.199.103:3256
118.117.188.62:3256
182.84.144.17:3256
175.7.199.37:3256
175.7.199.107:3256
118.117.188.69:3256
118.117.188.38:3256
182.84.145.178:3256
182.84.145.26:3256
175.7.199.70:3256
117.69.230.158:3256
60.167.20.20:1133
175.7.199.252:3256
103.99.8.102:83
103.35.135.30:84""".splitlines()


# connection = pymysql.connect(
#     # host='106.12.154.238',
#     host='127.0.0.1',
#     user='root',
#     password='',
#     database='caimao_students',
#     charset='utf8'
# )
# cursor = connection.cursor()


def main():
    url = "http://httpbin.org/get"  # 可以查看访问的ip
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    while True:
        try:
            ip = random.choice(ip_proxies)
            print(ip)
            proxies = {
                # "https": "https://" + ip,
                "http": "http://" + "183.39.155.200:80",
            }
            res = requests.get(url, headers=header, proxies=proxies, timeout=10)
            # res = requests.get(url, headers=header, timeout=10)
            print(res.text)
            break
        except Exception as e:
            print("报错：{}, ip不可用".format(e))
            time.sleep(1)


# def create_table():
#     """创建表格"""
#     create_sql = """
#         create table if not exists `infos`(
#             `id` INT UNSIGNED AUTO_INCREMENT,
#             `ip` VARCHAR(16) NOT NULL comment "ip地址",
#             `port` VARCHAR(16) NOT NULL comment "端口号",
#             `type` varchar(16) not null comment "类型：http/https",
#             `status` int(16) not null comment "状态：-1不可用，1可用，2正在使用",
#             `rps_time` varchar(16) comment "ping时的响应时间",
#             `crawl_time` date comment "抓取时间",
#             `test_time` date comment "检测时间",
#             PRIMARY KEY ( `id` )
#         )
#         """
#     try:
#         cursor.execute(create_sql)
#     except:
#         print("创建表格失败", traceback.print_exc())
#         return -1
if __name__ == '__main__':
    main()
