# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PythondemoPipeline(object):
    def process_item(self, item, spider):
        item['motoo']='fuck the city'
        return item

class PythondemoPipeline1(object):
    def process_item(self, item, spider):
        print(item)
        return item
