# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapycurrencyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    publish_date = scrapy.Field()
    text = scrapy.Field()
    website = scrapy.Field()