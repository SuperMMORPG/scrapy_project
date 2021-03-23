import scrapy
import re
from redis import Redis
from steam_info.items import SteamInfoItem
class SteamSpider(scrapy.Spider):
    name = 'steam'
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers']

    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):
        a_list = response.xpath('//*[@id="search_resultsRows"]/a')
        ranking = 0
        for a in a_list:

            item = SteamInfoItem()
            ranking = ranking + 1
            name = a.xpath('./div[2]/div[1]/span/text()').extract_first()
            release_date = a.xpath('./div[2]/div[2]/text()').extract_first()
            price = a.xpath('./div[2]/div[4]/div[2]/text()').extract()
            url = a.xpath('./@href').extract_first()
            #强指类型
            price = str(price)
            #找到数字价格，数字字符串拼接
            price2 = re.findall('\d+',price)
            price3 = '.'.join(price2)

            item['name'] = name
            item['release_date'] = release_date
            item['price'] = price3
            item['url'] = url
            item['ranking'] = ranking
            
            ex = self.conn.sadd('steam',url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item





