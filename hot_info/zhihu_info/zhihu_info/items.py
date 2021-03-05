# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhihu_ranking = scrapy.Field()
    zhihu_url = scrapy.Field()
    zhihu_title = scrapy.Field()
    pass
