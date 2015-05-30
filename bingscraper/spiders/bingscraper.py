# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
import string
import re
import math
import urllib
from scrapy import log
from pprint import pprint
import urllib2
from ..items import BingscraperItem
import codecs
TASK_INPUT_FILE = './task/task.txt'
class BingSpider(scrapy.Spider):
    name = "bingspider"
    allowed_domains = ["bing.com"]
    start_urls = []
    target_site = 'pan.baidu.com'
    def __init__(self):
        taskfile = codecs.open(TASK_INPUT_FILE,mode='r',encoding='utf-8')
        query_list=taskfile.readlines()
        for query in query_list:
            query=query.strip('\n\r\t').encode('utf-8')
            title = urllib2.quote(query)
            query_url='http://cn.bing.com/search?q='+title+' site:'+self.target_site
            self.start_urls.append(query_url)
        taskfile.close()

    def parse(self, response):
        html_txt = response.body.decode("utf-8","ignore")
       # print html_txt
        hxs = Selector(text=html_txt)
        items = hxs.xpath('//ol[@id="b_results"]/li[@class="b_algo"]')
        query = urllib2.unquote(response.url)

        if items:
            rank = 0
            for item in items:
                title = item.xpath('.//div[@class="b_title"]/h2/a')
                url = item.xpath('.//div[@class="b_title"]/h2/a/@href')
                caption = item.xpath('.//div[@class="b_caption"]/p')
                search_res = BingscraperItem()
                search_res['query'] = query.encode('utf-8')
                search_res['title'] = title.select('string()').extract()[0]
                search_res['title'] = search_res['title'].encode('utf-8')
                search_res['url'] = url.extract()[0]
                search_res['url'] = search_res['url'].encode('utf-8')
                search_res['caption'] = caption.select('string()').extract()[0]
                search_res['caption'] = search_res['caption'].encode('utf-8')
                search_res['rank'] = rank
                rank+=1
                yield  search_res
        else:
            print 'search results not found'