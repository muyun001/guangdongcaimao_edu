# xpath解析
from lxml import etree

if __name__ == '__main__':
    """
    # etree.parse(file_path) 读取本地html
    # etree.HTML(html)  解析网页端html
    """
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("./58_parse_test.html", parser=parser)

    # res = tree.xpath("html/head/title")  # 不加"/"就找不到内容
    res = tree.xpath("/html/head/title")  # 一级一级的定位
    res = tree.xpath("//title")  # 跨级定位
    res = tree.xpath("//div")  # 定位到所有的div标签
    res = tree.xpath("//div[@class='cike']")  # 定位到class="cike"的div标签

    """获取文本内容：
    /text()  获取标签中直系的文本内容
    //text() 获取标签中所有文本内容（非直系的文本内容）
    """
    # 获取class = "cike"的第三个p标签的文本内容
    # res = tree.xpath("//body/div[@class='cike']/p[3]/text()")
    # print(res)
    # 获取class='zhanshi'的第6个文本内容,返回值是个list
    # res = tree.xpath("//div[@class='zhanshi']//li[6]/a/text()")
    # 获取div标签下class='zhanshi'的，a标签下class="lu"的文本内容，返回值是个list
    # res = tree.xpath("//div[@class='zhanshi']//a[@class='lu']/text()")
    # res = tree.xpath("//div[@class='zhanshi']//a[@class='lu']/text()")[0]
    # 获取所有文本内容
    # res = tree.xpath('//div[@class="zhanshi"]//a//text()')

    """获取标签值： /@tag_name    如:/@href,/@src"""
    # 获取a标签下class='lu'的所有的href链接
    # res = tree.xpath('//div[@class="zhanshi"]//a[@class="lu"]//@href')
    # 获取div下class='zhanshi'的所有href链接
    # res = tree.xpath('//div[@class="zhanshi"]//@href')
    # 获取div下class='zhanshi'的所有img标签的src链接
    res = tree.xpath('//div[@class="zhanshi"]//img/@src')
    print(res)
