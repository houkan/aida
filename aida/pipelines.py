# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class AidaPipeline(object):
#     def process_item(self, item, spider):
#         return item




import codecs
import json

# import pymysql
# import pymysql.cursors
#
# from twisted.enterprise import adbapi
# from twisted.internet import reactor


# class MysqlTwistedPipeline(object):
#     def process_item(self, item, spider):
#         return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('aida.json','w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()

