# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douban.items import DoubanItem


class DoubanSpiderSpider(CrawlSpider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250?start=']

    rules = (
        # 匹配规则有坑 top250?start=多写有问题
        Rule(LinkExtractor(allow='start=\d+'), callback="parse_douban", follow=True),
    )

    def parse_douban(self, response):
        print response.url  # response为[url地址] 误以为是个地址 response.url response.body

        for each in response.xpath('//div[@class="info"]'):
            print "for each"
            item = DoubanItem()
            item['title'] = each.xpath('//div[@class="hd"]/a/span[1]/text()').extract()[0]  # div里的class="hd"要加引号
            item['db'] = each.xpath('//div[@class="bd"]/p/text()').extract()[0]
            item['star'] = each.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quoto = each.xpath('.//span[@class="inq"]/text()').extract()
            if len(quoto) != 0:
                item["quoto"] = quoto[0]
            else:
                item["quoto"] = " "

            print item['title'] + item['db'] + item['star']

            yield item
