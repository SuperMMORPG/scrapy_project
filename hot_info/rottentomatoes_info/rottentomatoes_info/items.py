# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RottentomatoesInfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    ranking = scrapy.Field()
    rating = scrapy.Field()
    audiencescore = scrapy.Field()
    tomatometerscore = scrapy.Field()
    pass
