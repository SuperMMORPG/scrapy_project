import scrapy
from hupu_info.items import HupuInfoItem
from redis import Redis
class HupuSpider(scrapy.Spider):
    name = 'hupu'
    #allowed_domains = ['www.xx.com']
    start_urls = ['https://bbs.hupu.com/all-gambia']
    conn = Redis(host='192.168.1.100',port=6379)

    def parse(self, response):
        # 新版本虎扑
        #div_list = response.xpath('//*[@id="container"]/div/div[2]/div/div[2]/div[2]/div')
        # 老版本虎扑
        li_list = response.xpath('//*[@id="container"]/div/div[2]/div[1]/ul/li')
        for i in range(10):
            '''
            div = div_list[i]
            href = div.xpath('./div/div[1]/a/@href').extract_first()
            hupu_url = 'https://bbs.hupu.com' + href
            hupu_title = div.xpath('./div/div[1]/a/span/text()').extract_first()
            '''

            li = li_list[i]
            href = li.xpath('./span[1]/a/@href').extract_first()
            hupu_url = 'https://bbs.hupu.com' + href
            hupu_title = li.xpath('./span[1]/a/span/text()').extract_first()
            hupu_ranking = i + 1

            item = HupuInfoItem()
            item['hupu_url'] = hupu_url
            item['hupu_title'] = hupu_title 
            item['hupu_ranking'] = str(hupu_ranking)
            
            ex = self.conn.sadd('hupu',hupu_url)
            if ex==1:
                print('该地址为新地址，可以进行任务获取',hupu_url)
                yield item
            else:
                print('地址已经存在',hupu_url)
                yield item


