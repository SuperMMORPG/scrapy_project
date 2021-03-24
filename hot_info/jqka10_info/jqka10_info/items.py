# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Jqka10InfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    ranking =scrapy.Field()
    code = scrapy.Field()
    up_and_down = scrapy.Field()
    
    pass
