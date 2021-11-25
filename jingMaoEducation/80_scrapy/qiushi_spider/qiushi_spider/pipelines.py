# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiushiSpiderPipeline:
    f = None

    def open_spider(self, spider):
        """开始函数"""
        print("开始抓取。。。")
        self.f = open("qiushi.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        author = item["author"]
        article = item["article"]
        article_url = item["article_url"]
        self.f.write(f'"author":{author},"article_url":{article_url},"article":{article}\n')
        return item

    def close_spider(self, spider):
        """结束函数"""
        print("结束抓取。。。")
        self.f.close()
