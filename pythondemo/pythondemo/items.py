# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class demo_item (scrapy.Item):
    title = scrapy.Field()  # 帖子标题
    url = scrapy.Field()  # 帖子网址
    content = scrapy.Field()  # 帖子内容
    post_date = scrapy.Field()  # 发帖日期
    reply_count = scrapy.Field()  # 回复数

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
