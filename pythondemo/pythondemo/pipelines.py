# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
class PythondemoPipeline(object):

    def __init__(self):
        self.num=0
        if not os.path.exists("./photo"):
            os.mkdir("./photo")

    def process_item(self, item, spider):
        print(item)
        self.num=self.num+1
        url=str(item['img'])
        name=str(self.num)+'.jpg'
        r=requests.get(url)
        if not os.path.exists('./photo/'+name):
            with open('./photo/'+name,'wb') as f:
                f.write(r.content)
        print(str(self.num)+"*" * 20)

        return item



