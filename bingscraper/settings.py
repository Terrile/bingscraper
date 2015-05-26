# -*- coding: utf-8 -*-

# Scrapy settings for bingscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bingscraper'

SPIDER_MODULES = ['bingscraper.spiders']
NEWSPIDER_MODULE = 'bingscraper.spiders'
ITEM_PIPELINES = ['bingscraper.pipelines.DumpSearchResPipeline']
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False


SEARCH_RES_FILE = 'search_result.json'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bingscraper (+http://www.yourdomain.com)'
