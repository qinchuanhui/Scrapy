# -*- coding: utf-8 -*-
import scrapy


class Demo2Spider(scrapy.Spider):
    name = "demo2"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
