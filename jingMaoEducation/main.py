"""
兼职猫项目步骤：
    - 抓取所有城市的名字和链接，并保存到数据库
    - 根据城市链接，抓取该城市的地区数据（地区名，地区链接...）,并保存
    - 根据地区链接，抓取兼职的列表，和兼职的详情，并保存
"""


def crawl_city():
    """抓取所有城市的名字和链接"""

    citys = {}
    return citys


def insert_city(citys):
    """保存城市数据到数据库"""
    # 保存到数据库


def query_citys():
    """从数据库获取城市数据"""

    result = []
    return result


def crawl_region(data):
    """抓取地区数据"""
    result = []
    return result


def insert_region(region_result):
    """存储地区数据"""
    pass


def run():
    result = crawl_city()  # 抓取城市信息
    insert_city(result)  # 存储城市信息到数据库

    # 从数据库获取城市链接，使用此链接来抓取地区数据
    result = query_citys()
    region_result = crawl_region(result)
    insert_region(region_result)


if __name__ == '__main__':
    run()
