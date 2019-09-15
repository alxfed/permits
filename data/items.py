# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class InspTableLine(scrapy.Item):
    insp_n      = scrapy.Field()
    insp_date   = scrapy.Field()
    status      = scrapy.Field()
    type_desc   = scrapy.Field()


class InspTable(scrapy.Item):
    pass
