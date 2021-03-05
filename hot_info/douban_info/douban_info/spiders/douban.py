import scrapy
from douban_info.items import DoubanInfoItem
from redis import Redis
class DoubanSpider(scrapy.Spider):

    name = 'douban'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://www.douban.com/group/explore/tech']

    conn = Redis(host='127.0.0.1',port=6379)

    def parse(self, response):

        douban_ranking = 0
        div_list = response.xpath('//*[@id="content"]/div/div[1]/div[1]/div')
        for div in div_list:
            douban_ranking = douban_ranking + 1
            douban_title = div.xpath('./div[2]/h3/a/text()').extract_first()
            douban_url = div.xpath('./div[2]/h3/a/@href').extract_first()

            item = DoubanInfoItem()
            item['douban_ranking'] = str(douban_ranking)
            item['douban_title'] = douban_title
            item['douban_url'] = douban_url

            ex = self.conn.sadd('douban',douban_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',douban_url)
                yield item
            else:
                print('地址已经存在',douban_url)
                yield item

