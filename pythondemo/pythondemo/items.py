# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class demo_item (scrapy.Item):
    name = scrapy.Field()  # 书名
    url = scrapy.Field()  # 详细网址
    price = scrapy.Field()  # 价格
    bookshop = scrapy.Field()  # 店名
    comment_count = scrapy.Field()  # 评价数
    img=scrapy.Field() #图片信息
    isbn=scrapy.Field()#图书刊号
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
