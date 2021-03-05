# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuanchaInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    guancha_title = scrapy.Field()
    guancha_ranking = scrapy.Field()
    guancha_url = scrapy.Field()
    pass
