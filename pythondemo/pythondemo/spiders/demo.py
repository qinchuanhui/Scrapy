# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from pythondemo.items import demo_item
import logging


class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["search.suning.com"]
    start_urls = ['http://search.suning.com/%E5%8E%9F%E7%89%88%E4%B9%A6/']
    num=1

    def getname(self,lis):#原本得到的是列表，此函数将列表连成字符串
        name=""
        for li in lis:
            name=name+str(li)
        return name

    def get_isbn(self,response):#这里的response很可能会被过滤掉，所以要更改dont filter =true

        item=response.meta['item']
        isbn=response.xpath("//div[@id='productDetail']//dd//li/text()").extract()[-2]
        item['isbn']=isbn.split('：')[1] #这里的冒号是中文字符，wtf
        yield item

    def parse(self, response):  # 提取数据
        #info = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        #print(info)
        li_list=response.xpath("//ul[@class='general clearfix']//li")
        #li_list=response.xpath("//div[@class='tea_con']//li")
        self.num=self.num+1
        for li in li_list:

            #if num >=10 :
            #    break
            item=demo_item()
            name=li.xpath(".//div[@class='title-selling-point']/a/text()").extract()
            item['name']= self.getname(name)
            url=li.xpath(".//div[@class='title-selling-point']/a/@href").extract_first()
            item['url']='http:'+str(url)
            price=li.xpath(".//span[@class='def-price']/text()").extract()
            item['price']=self.getname(price)
            item['bookshop']=li.xpath(".//div[@class='store-stock']/a/text()").extract_first()
            item['comment_count']=li.xpath(".//div[@class='info-evaluate']//i/text()").extract_first()
            img=li.xpath(".//div[@class='res-img']//img/@src").extract_first()
            item['img']='http:'+str(img)


            r=scrapy.Request(  #为了进一步获取isbn编号，访问每本书的具体网页
                str(item['url']),
                callback=self.get_isbn,
                meta={'item':item},
                dont_filter=True
            )

            yield r


        #进行跳转下一页的操作
        num_str=str(self.num)
        #因为next页的源代码显示为 void（0），因此只能选择str（num）的做法
        strr="//div[@class='sn-pager']//a[@pagenum='"+num_str+"']/@href"
        next_url=response.xpath(strr).extract_first()
        if next_url:
            url_new='http://search.suning.com/'+str(next_url)
            print(url_new)
            yield scrapy.Request(url_new,callback=self.parse)
