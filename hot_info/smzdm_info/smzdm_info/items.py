# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmzdmInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    smzdm_url = scrapy.Field()
    smzdm_title = scrapy.Field()
    smzdm_ranking = scrapy.Field()
    pass
