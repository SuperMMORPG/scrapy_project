import scrapy
from bilibili_info.items import BilibiliInfoItem
from redis import Redis
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']

    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):

        li_list = response.xpath('//*[@id="app"]/div[2]/div[2]/ul/li')
        
        for i in range(20):

            li = li_list[i]
            title = li.xpath('./div[2]/div[2]/a/text()').extract_first()
            href = li.xpath('./div[2]/div[2]/a/@href').extract_first()
            url = 'https:' + href

            item = BilibiliInfoItem()
            item['title'] = title
            item['url'] = url
            item['ranking'] = str(i+1)

            ex = self.conn.sadd('bilibili',url)
            if ex==1:
                #print('该地址为新地址，可以进行任务获取',url)
                yield item
            else:
                print('地址已经存在',url)
                yield item

