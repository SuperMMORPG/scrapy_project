import scrapy


class AeonSpider(scrapy.Spider):
    name = 'aeon'
    allowed_domains = ['www.xx.com']
    start_urls = ['http://www.xx.com/']

    def parse(self, response):
        pass
