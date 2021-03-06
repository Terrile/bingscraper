# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import settings
from items import BingscraperItem
class BingscraperPipeline(object):
    def process_item(self, item, spider):
        return item

class DumpSearchResPipeline(object):
    def __init__(self):
        self.search_result = codecs.open(settings.SEARCH_RES_FILE, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item,BingscraperItem):
            return self.process_searchRes(item,spider)

    def process_searchRes(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)
        self.search_result.write(line)
        self.search_result.write("\n")

    def spider_closed(self, spider):
        self.search_result.close()