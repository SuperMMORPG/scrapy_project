# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BkchinaInfoItem(scrapy.Item):
    # define the fields for your item here like:
    area_name = scrapy.Field()
    area_id = scrapy.Field()
    city = scrapy.Field()
    store_num = scrapy.Field()
    city_id = scrapy.Field()
    pass

class BkchinaStoreItem(scrapy.Item):

    store_id = scrapy.Field()
    store_name = scrapy.Field()
    store_opening_hours = scrapy.Field()
    store_address = scrapy.Field()
    store_tel = scrapy.Field()
    
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    store_num = scrapy.Field()