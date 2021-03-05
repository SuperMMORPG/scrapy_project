# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HupuInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hupu_ranking = scrapy.Field()
    hupu_title = scrapy.Field()
    hupu_url = scrapy.Field()
    pass
