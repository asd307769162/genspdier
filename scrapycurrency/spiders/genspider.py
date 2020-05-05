# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class GenspiderSpider(CrawlSpider):
    name = 'genspider'
    allowed_domains = ['bxjg.circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    '''
            可以定义提取url地址的规则
            LinkExtractor 连接提取器，提取url
            allow : 可以写入正则表达式
            callback: 提取出来的url地址的response交给callback处理
            follow: 表示当前的url地址的响应是否重新经过rules来提取url地址
    '''
    rules = (
        # 匹配需要提取的url
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),
        # 循环翻页
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True),
    )

    # response为请求回来的响应数据
    def parse_item(self, response):
        item = {}
        item['title'] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->", response.body.decode())[0]
        item['publish_date'] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})", response.body.decode())[0]
        item['text'] = response.xpath('//span[@id="zoom"]//p//text()')
        item['website'] = "中国保险监督管理委员会"


        print(item)

        yield item
