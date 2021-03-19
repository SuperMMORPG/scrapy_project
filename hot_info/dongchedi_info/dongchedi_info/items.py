# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongchediInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass 

class DongchediVideoItem(scrapy.Item):

    dongchedi_video_title = scrapy.Field()
    dongchedi_video_url = scrapy.Field()
    dongchedi_video_ranking = scrapy.Field()

class DongchediArticleItem(scrapy.Item):

    dongchedi_article_title = scrapy.Field()
    dongchedi_article_url = scrapy.Field()
    dongchedi_article_ranking = scrapy.Field()
