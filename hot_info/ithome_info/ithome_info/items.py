# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IthomeInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ithome_url = scrapy.Field()
    ithome_title = scrapy.Field()
    ithome_ranking = scrapy.Field()
    ithome_time = scrapy.Field()
    pass
