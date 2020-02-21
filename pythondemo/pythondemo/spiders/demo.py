# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from pythondemo.items import demo_item


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["www.itcast.cn"]
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):  # 提取数据
        #info = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        #print(info)
        li_list=response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item={}
            item['name']=li.xpath(".//h3/text()").extract_first()
            item['title']=li.xpath(".//h4/text()").extract_first()
            yield item