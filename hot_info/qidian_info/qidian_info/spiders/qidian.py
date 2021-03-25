from urllib import parse
import scrapy

from qidian_info.items import QidianInfoItem
import qidian_info.utils as uu

class QidianSpider(scrapy.Spider):
    name = 'qidian'

    start_urls = ('https://www.qidian.com/rank/hotsales?page=%d'% i for i in range(1,6))

    conn = uu.connect()

    def start_requests(self):

        for url in self.start_urls:

            yield scrapy.Request(url,callback=self.parse)
        
    def parse(self, response):

        li_list = response.xpath('//*[@id="rank-view-list"]/div/ul/li')
        for li in li_list:
            ranking = li.xpath('./div[1]/span/text()').extract_first()
            url = 'https:' + li.xpath('./div[2]/h4/a/@href').extract_first()
            name = li.xpath('./div[2]/h4/a/text()').extract_first()
            author = li.xpath('./div[2]/p[1]/a[1]/text()').extract_first()

            item = QidianInfoItem()
            item['ranking'] = ranking
            item['url'] = url
            item['name'] = name
            item['author'] = author

            ex = uu.add(self.conn,'qidian',url)

            yield item

