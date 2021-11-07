import re


def check_url(url):
    """
    判断url是否合法
    """
    # result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+', url)  # 也可以写成这种格式
    re_g = re.compile('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    print(re_g)
    result = re_g.findall(url)
    if not result:
        return False
    return True


def get_url(url):
    """
    通过组获取url中的某一部分
    :param url:
    :return:
    """
    re_g = re.compile('[https://|http://](\w*\.*\w+\.\w+)')
    result = re_g.findall(url)
    if not result:
        return ""
    return result[0]


def get_email(data):
    # result = re.findall('[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+', data)
    re_g = re.compile('.+@.+\.[a-zA-Z]+')
    result = re_g.findall(data)
    return result


def get_img_srcs(data):
    """
    使用非贪婪模式
    """
    re_g = re.compile('src="(.*?)"')
    result = re_g.findall(data)
    return result


def get_titles(data):
    """
    使用非贪婪模式匹配所有title
    """
    re_g = re.compile('title="(.*?)"')
    result = re_g.findall(data)
    return result


def get_all_data_html(data):
    """
    获取html中所有等号后双引号内的字符
    """
    re_g = re.compile('="(.+?)"')
    result = re_g.findall(data)
    return result


if __name__ == '__main__':
    result = check_url('https://www.baidu.com')
    print(result)

    result = get_url('https://www.baidu.com')
    print(result, 'https')

    result = get_url('http://www.baidu.com')
    print(result, 'http')

    result = get_email('insane@163.net')
    print(result)

    with open("58_parse_test.html", "r", encoding="utf-8") as f:
        html = f.read()

    result = get_img_srcs(html)
    print(result)

    result = get_titles(html)
    print(result)

    re_g = re.compile('class="(.*?)"', re.S)  # re.S匹配所有字符（包括换行符）
    result = re_g.match(html)  # 从最开始匹配，匹配不到返回None
    print(result)

    re_g = re.compile("<!DOCTYPE (.*?)>", re.S)
    result = re_g.match(html)
    print(result)
    print(result.group())

    re_g = re.compile('class=".*?"', re.S)  # 加不加()，结果都一样
    # re_g = re.compile('class="(.*?)"', re.S)  # 加不加()，结果都一样
    result = re_g.search(html)  # 全文查找，返回找到的第一个结果的Match对象
    print(result)
    print(result.group())  # 返回第一个结果

    re_g = re.compile('\s')  # \s匹配任意空白字符
    result = re_g.split(html)
    print(result)

    html2 = """
    <div class='chenglong'> <span id='1'>成龙</span> </div>
    <div class='liyd'> <span id='2'>李云迪</span> </div>
    <div class='wuyf'> <span id='3'>吴亦凡</span> </div>
    <div class='fangzm'> <span id='4'>房祖名</span> </div>
    <div class='fanbb'> <span id='5'>范冰冰</span> </div>
    """
    # 编译正则表达式，获取pattern对象
    re_g = re.compile(r"<div class='(.*?)'> <span id='(\d)'>(.*?)</span> </div>", re.S)
    re_g_2 = re.compile(r"<div class='(?P<classValue>.*?)'> <span id='(?P<idValue>\d)'>(?P<name>.*?)</span> </div>",
                        re.S)
    result = re_g_2.finditer(html2)
    for it in result:
        # print(it.group("classValue"))
        # print(it.group("idValue"))
        print(it.group(3))

    result = re_g.findall(html2)
    print(list(map(lambda s: s[2], result)))
