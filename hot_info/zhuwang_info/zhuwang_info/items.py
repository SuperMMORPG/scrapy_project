# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhuwangInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province_name = scrapy.Field()
    today_price = scrapy.Field()
    yesterday_price = scrapy.Field()
    source_url = scrapy.Field()
    title = scrapy.Field()
    today_date = scrapy.Field()
    yesterday_date = scrapy.Field()
    shengzhu_type = scrapy.Field()
    pass
