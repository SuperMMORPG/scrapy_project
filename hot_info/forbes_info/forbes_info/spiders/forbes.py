import scrapy
import json

from scrapy.http import headers
from forbes_info.items import ForbesInfoItem
class ForbesSpider(scrapy.Spider):

    name = 'forbes'
    url = r'https://www.forbes.com/simple-data/editors-picks/'

    def start_requests(self):
        
        HEADERS = {
            'cookie': 'client_id=5a494dbbf7b7077993b9af1180c7b2de2a7; usprivacy=1---; notice_behavior=none',
        }

        yield scrapy.Request(self.url ,callback=self.parse,headers=HEADERS)
    def parse(self, response):

        text_list = json.loads(response.text)
        for text in text_list:

            blogName = text['blogName']
            blogType = text['blogType']
            title = text['title']
            uri = text['uri']
            author = text['author']['name']

            item = ForbesInfoItem()
            item['blogName'] = blogName
            item['blogType'] = blogType
            item['title'] = title
            item['uri'] = uri
            item['author'] = author

            yield item

