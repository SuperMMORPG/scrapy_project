import scrapy
import json
from unsplash_info.items import UnsplashInfoItem

class UnsplashSpider(scrapy.Spider):
    name = 'unsplash'
    start_urls = ('https://unsplash.com/napi/topics/nature/photos?page=%d&per_page=10' %i for i in range(1,5))

    def parse(self, response):
        list_text = json.loads(response.text)

        for text in list_text:
            photo_id = text['id']
            photo_url_small = text['urls']['small']
            photo_user_id = text['user']['id']
            photo_user_name = text['user']['name']
            photo_user_html = text['user']['links']['html']
            item = UnsplashInfoItem()
            item['photo_id'] = photo_id
            item['photo_url_small'] = photo_url_small
            item['photo_user_id'] = photo_user_id
            item['photo_user_name'] = photo_user_name
            item['photo_user_html'] = photo_user_html
            yield item


