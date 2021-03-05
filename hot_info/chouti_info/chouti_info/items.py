# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chouti_url = scrapy.Field()
    chouti_title = scrapy.Field()
    chouti_ranking = scrapy.Field()
    chouti_hours = scrapy.Field()
    pass
