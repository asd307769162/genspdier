# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapycurrency.items import ArticleItemLoader, ScrapycurrencyItem


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
        loader = ArticleItemLoader(item=ScrapycurrencyItem(), response=response)
        loader.add_xpath("text", '//span[@id="zoom"]//p//text()')
        loader.add_value("website", '中国保险监督管理委员会')
        # 直接给字段赋值，尤其需要注意，不管赋值的数据是什么，都会自动转换成list类型
        loader.add_value("url", response.url)

        yield loader.load_item()
