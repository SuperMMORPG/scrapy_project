# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashInfoItem(scrapy.Item):
    # define the fields for your item here like:
    photo_id = scrapy.Field()
    photo_url_small = scrapy.Field()
    photo_user_id = scrapy.Field()
    photo_user_name = scrapy.Field()
    photo_user_html = scrapy.Field()
    pass
