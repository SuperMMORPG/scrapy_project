# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Kr36InfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Kr36RenqiItem(scrapy.Item):

    renqi_url = scrapy.Field()
    renqi_title = scrapy.Field()
    renqi_ranking = scrapy.Field()

class Kr36ZongheItem(scrapy.Item):

    zonghe_url = scrapy.Field()
    zonghe_title = scrapy.Field()
    zonghe_ranking = scrapy.Field()

class Kr36ShoucangItem(scrapy.Item):

    shoucang_url = scrapy.Field()
    shoucang_title = scrapy.Field()
    shoucang_ranking = scrapy.Field()