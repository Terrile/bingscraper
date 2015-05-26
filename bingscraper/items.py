# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import scrapy
from scrapy.item import  Item,Field

class BingscraperItem(scrapy.Item):
    query = Field()
    title = Field()
    url = Field()
    caption = Field()
    rank = Field()


