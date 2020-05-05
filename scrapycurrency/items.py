# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst


class ArticleItemLoader(ItemLoader):
    """自定制ItemLoader，取值都会调用TakeFirst函数 默认的输出处理器为取第一个非空元素"""
    defualt_output_processor = TakeFirst()


def text_filter(text):
    """在item赋值前处理之前xpath定位的text字段并返回"""
    try:
        text = ''.join(text).strip()
    except:
        text = text
    return text

class ScrapycurrencyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    publish_date = scrapy.Field()
    text = scrapy.Field(
        # 对传入到item的值调用指定的函数进行预处理，且自动传入当前字段值
        input_processor=MapCompose(text_filter),
    )
    website = scrapy.Field()
    url = scrapy.Field()

"https://blog.csdn.net/sinat_41622641/article/details/83869173"