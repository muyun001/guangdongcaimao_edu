"""
bs4解析需要安装包：bs4、lxml
    - pip install bs4
    - pip install lxml
bs4解析的原理：
    - 1、实例化一个BeautifulSoup对象，并将源码加载到对象中
    - 2、通过调用BeautifulSoup对象中相关的属性或方法进行标签定位和数据提取
"""
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("./58_parse_test.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")

    """
    第一种方式：直接soup.tag_name 
    获取到第一个tag_name标签
    """
    # print(soup.div)  # 获取到第一个div标签
    # print(soup.a)  # 获取到第一个a标签
    # print(soup.img)  # 获取到第一个img标签

    """
    第二种方式：soup.find("tag_name") 
    获取到第一个tag_name标签，同soup.tag_name
    """
    # print(soup.find("div"))  # 获取到第一个div标签，同soup.div
    # print(soup.find("img"))  # 获取到第一个img标签，同soup.img
    # print(soup.find("div", class_="cike"))  # 获取到class="cike"的div标签

    """
    第三种方式：soup.findall("tag_name")  
    获取所有tag_name标签，返回值是个列表
    """
    # print(soup.find_all("a"))  # 获取所有a标签
    # for a in soup.find_all("a"):
    #     print(a)
    # print(soup.find_all("img"))  # 获取所有img标签

    """
    # 第四种方式：soup.select("选择器")
    # 解释器中，"."代表class， "#"代表id
    # ">"表示下一个层级，如果在使用">"的情况下跨级获取，将获取不到内容
    # 不使用">"时，可以跨级获取
    """
    # print(soup.select("div.zhanshi"))  # 获取所有的"zhanshi"(战士)标签，返回一个列表
    # print(soup.select(".zhanshi > ul > li > a"))  # 逐级获取zhanshi下的所有a标签，
    # print(soup.select(".zhanshi > ul > li > a")[0])  # 逐级获取，获取zhanshi下所有a标签的第一个标签
    # print(soup.select(".zhanshi > li > a"))  # 在使用">"的情况下跨级获取，获取不到内容
    # print(soup.select(".zhanshi li > a"))  # 在使用">"的情况下跨级获取
    # print(soup.select(".zhanshi a"))  # 跨级获取zhanshi下的所有a标签
    # print(soup.select("#lvbu"))

    """获取到标签中的文本数据
    方法：
        .text           # 用得最多
        .get_text()
        .string
        
        - 区别：
            .text/.get_text() 可以获取到某个标签中所有的文本内容
            .string 只能获取到某标签下直系的文本内容
    """
    # print(soup.select(".zhanshi a")[0].text)
    # print(soup.select(".zhanshi a")[0].string)
    # print(soup.select(".zhanshi a")[0].get_text())
    # print(soup.find("div").text)  # 获取第一个div标签下的所有文本数据
    # print(soup.find("div").get_text())  # 获取第一个div标签下的所有文本数据
    # print(soup.find("div").string)  # 返回None

    """获取标签属性值：["标签"]"""
    # print(soup.select(".zhanshi a")[0]["href"])  # 获取第一个a标签的href值
    # 获取zhanshi下所有a标签的href值
    hrefs = list()
    for tag_a in soup.select(".zhanshi a"):
        hrefs.append(tag_a["href"])
    print(hrefs)
    # 获取zhanshi下所有a标签的title值，如果没有title标签会报错
    titles = list()
    for tag_a in soup.select("div.zhanshi a"):
        try:
            titles.append(tag_a["title"])
        except:
            pass
    print(titles)
