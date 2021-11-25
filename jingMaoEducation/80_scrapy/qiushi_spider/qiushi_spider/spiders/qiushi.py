import scrapy
from qiushi_spider.items import QiushiSpiderItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 解析：
        article_tags = response.xpath('//div[starts-with(@class,"article block")]')
        for tag in article_tags:
            author = tag.xpath('./div[@class="author clearfix"]//h2/text()').extract_first().strip()
            articles = tag.xpath('.//div[@class="content"]/span//text()').extract()
            article_url = "https://www.qiushibaike.com" + tag.xpath('./a/@href').extract_first().strip()
            article = "".join(articles).strip() if articles else ""

            # 创建item对象并返回
            item = QiushiSpiderItem()
            item["author"] = author
            item["article"] = article
            item["article_url"] = article_url
            yield item
