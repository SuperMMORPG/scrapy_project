# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    douban_title = scrapy.Field()
    douban_url = scrapy.Field()
    douban_ranking = scrapy.Field()
    
    pass
